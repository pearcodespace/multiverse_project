from django.shortcuts import render
from datetime import datetime
from django.http.response import HttpResponse

all_reports = [
    {
        'id': 1, 'title': 'Report1',
        'start_date': datetime(2022, 2, 28, 12, 30)
    },
    {   'id': 2, 'title': 'Report2',
        'start_date': datetime(2022, 2, 28)
    },
    {   'id': 3, 'title': 'Report3',
        'start_date': datetime(2022, 2, 28)
    },
]

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def app_general(request):
    context = {}
    return render(request, "app_general/home.html", context=context)

def app_general_docs(request):
    context = {}
    return render(request, "app_general/docs.html", context=context)

def app_reports(request):
    context = {'reports': all_reports}
    return render(request, "app_reports/reports.html", context=context)

def app_reports_report(request, report_id):
    one_report = None
    try:
        one_report = [r for r in all_reports if r['id'] == report_id][0]
    except IndexError:
        print('Report Not Found')
    context = {'report': one_report}
    return render(request, 'app_reports/report.html', context)

def app_textsentiment(request):
    context = {}
    return render(request, "app_textsentiment/text_sentiment.html", context=context)

def app_textsentiment(request):
    context = {}
    return render(request, "app_textsentiment/text_sentiment.html", context=context)  

from django.http import JsonResponse
from app_reports.models import ClothDescription
import pandas as pd

def import_data_csv(request):
    csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRczZZCFn9DCaHfOUFm_8wnJ7ymFjOCvtOoLWp2mxz09Bzn3WmOuESWVCzTOd8_radP43cJH_uARyui/pub?output=csv'
    df = pd.read_csv(csv_url)
    data_sets = df[["Clothing ID", "Age", "Review Text", "Rating","Department Name"]]
    success_indices = []
    error_indices = []
    for index, row in data_sets.iterrows():
        instance = ClothDescription(
            Cloth_ID = row['Clothing ID'],
            Age = row['Age'],
            Review_Text = row['Review Text'],
            Rating = row['Rating'],
            Department_Name = row['Department Name']
        )
        try:
            instance.save()
            success_indices.append(index)
        except:
            error_indices.append(index)
    return JsonResponse({"success_indices": success_indices, "error_indices": error_indices})


import requests
def call_external_api(request):
    api_url = 'https://api.aiforthai.in.th/ssense'
    text = 'สาขานี้พนักงานน่ารักให้บริการดี'
    params = {'text':text}
    headers = {
        'Apikey': "QVGlFjHSWzTOpIPL8AQWtDbSyajhXYSU"
        }
    response = requests.get(api_url, headers=headers, params=params)
    print (response.json())
    return JsonResponse(response.json())

import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def linear_regression(request):
    Cloth_ID = list(ClothDescription.objects.all().order_by('id').values_list('Cloth_ID', flat=True))
    Rating = list(ClothDescription.objects.all().order_by('id').values_list('Rating', flat=True))
    X = np.array(Cloth_ID).reshape(-1, 1)
    y = np.array(Rating).reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X)
    json_output = {
        'Cloth_ID': Cloth_ID,
        'Rating': Rating,
        'predict_rating': list(y_pred.flat)
        }
    return JsonResponse(json_output)

import requests
import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from app_textsentiment.models import CSVFile, Text

def save_csv_and_texts(request):
    if request.method == 'POST' and request.FILES.get('file'):
        # Assume 'file' is the uploaded CSV file
        uploaded_file = request.FILES['file']
        
        # Save the CSV file to the database
        csv_obj = CSVFile.objects.create(file=uploaded_file)

        # Read the contents of the file and create Text objects
        csv_text = uploaded_file.read().decode('utf-8')
        text_contents = csv_text.split('\n')  # Assuming each line is a separate text

        text_objects = [Text(csv_file=csv_obj, text_content=text) for text in text_contents]
        Text.objects.bulk_create(text_objects)

    return render(request, 'app_textsentiment/text_sentiment.html')

from django.shortcuts import render
from app_textsentiment.models import Text, APIResponse
import requests

API_URL = "https://api-inference.huggingface.co/models/lxyuan/distilbert-base-multilingual-cased-sentiments-student"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def import_and_send_to_api(request):
    # Retrieve the first 100 Text objects
    text_objects = Text.objects.all()[:100]

    # Create a list to store the text content of each Text object
    text_content_list = [text.text_content for text in text_objects]

    # Join the text content into a single string (assuming the API expects a single string)
    input_text = " ".join(text_content_list)

    # Use the query function to send the input text to the API
    output = query({
        "inputs": input_text,
    })

    # Process the API response and save it to the APIResponse model
    api_responses = []
    for key, value in output.items():
        api_response = APIResponse(result_key=key, result_value=value)
        api_response.save()
        api_responses.append(api_response)

    # Render the API responses in a template
    context = {"api_responses": api_responses}
    return render(request, 'app_textsentiment/text_sentiment.html', context)

def analyze_api(request):
    # Trigger API processing and return the API response in a format suitable for the template
    # This could be similar to the code in import_and_send_to_api
    # For simplicity, this example returns a static response
    return HttpResponse("<tr><td>Result Key</td><td>Result Value</td></tr>")
