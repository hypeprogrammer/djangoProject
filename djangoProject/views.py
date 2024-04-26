import pandas as pd
import csv
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import CSVUploadForm

def home(request):
    return render(request, 'MainPage.html')

def data(request):
    return render(request, 'Data.html')


def upload(request):
    # uploads 폴더가 있는지 확인하고, 없으면 생성
    upload_dir = './uploads'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    if request.method == 'POST' and 'csv_file' in request.FILES:
        file = request.FILES['csv_file']
        file_path = os.path.join(upload_dir, file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # 파일 내용을 읽어 화면에 출력
        data = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        return render(request, 'Data.html', {'data': data})

    return render(request, 'Data.html')