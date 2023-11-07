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
    Cloth_ID = list(ClothDescription.objects.all().order_by('id').values_list('Clothing ID', flat=True))
    Rating = list(ClothDescription.objects.all().order_by('id').values_list('Rating', flat=True))
    X = np.array(Cloth_ID).reshape(-1, 1)
    y = np.array(Rating).reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X)
    json_output = {
        'Clothing_ID': Cloth_ID,
        'Rating': Rating,
        'predict_rating': list(y_pred.flat)
        }
    return JsonResponse(json_output)