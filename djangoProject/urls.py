from django.contrib import admin
from django.urls import path
from .views import home  # views를 가져오는 부분

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # 메인 페이지로 설정
]
