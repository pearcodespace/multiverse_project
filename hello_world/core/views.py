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
from app_reports.models import FlipkartProduct
import pandas as pd

# def import_data_csv(request):
#     csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT8UatbG7-DJ76bijnpp-s_DrZXdY7FW5IZ8Ogq7tBL9u8sG97yudyPN1xVqiDetT1kIHqdh2Fi5dBR/pub?output=csv"
#     df = pd.read_csv(csv_url)
#     data_sets = df[["Cothing ID", "Age", "Review Text", "Rating","Department_Name"]]
#     success_indices = []
#     error_indices = []
#     for index, row in data_sets.iterrows():
#         instance = ClothDescription(
#             Cloth_ID = row['Cothing ID'],
#             Age = row['Age'],
#             Review_Text = row['Review Tex'],
#             Rating = row['Rating'],
#             Department_Name = row['Department_Name'],
#         )
#         try:
#             instance.save()
#             success_indices.append(index)
#         except:
#             error_indices.append(index)
#     return JsonResponse({"success_indices": success_indices, "error_indices": error_indices})

def import_data_csv(request):
    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTbzeN16b1uQgbDBi2_BxVSs8S0cOuToXCZeCOl3laitVgSFd4WAum7IoTBFRrfnYQT8hPpWt9K9Acs/pub?output=csv"
    df = pd.read_csv(csv_url)
    data_sets = df[["product_name", "product_price", "Rate", "Review","Summary","Sentiment"]]
    success_indices = []
    error_indices = []
    for index, row in data_sets.iterrows():
        instance = FlipkartProduct(
            product_name = row['product_name'],
            product_price = row['product_price'],
            rate = row['Rate'],
            review = row['Review'],
            summary = row['Summary'],
            sentiment = row['Sentiment']
        )
        try:
            instance.save()
            success_indices.append(index)
        except:
            error_indices.append(index)
    return JsonResponse({"success_indices": success_indices, "error_indices": error_indices})