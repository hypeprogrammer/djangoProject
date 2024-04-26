import pandas as pd
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import CSVUploadForm
from .models import Iris

def home(request):
    return render(request, 'mainPage.html')

@require_http_methods(["GET", "POST"])
def upload_file(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            # CSV 파일을 pandas DataFrame으로 읽기
            df = pd.read_csv(file)
            instances = [
                Iris(
                    sepal_length=row['sepal_length'],
                    sepal_width=row['sepal_width'],
                    petal_length=row['petal_length'],
                    petal_width=row['petal_width'],
                    species=row['species']
                )
                for index, row in df.iterrows()
            ]
            # bulk_create를 사용하여 한 번에 데이터베이스에 인스턴스 저장
            Iris.objects.bulk_create(instances)
            return redirect('success_url')  # 성공 URL로 리디렉트
    else:
        form = CSVUploadForm()
    return render(request, 'Data.html', {'form': form})