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