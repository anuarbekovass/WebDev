from django.contrib import admin
from django.urls import path
from api import views
from api.views import VacancyDetailAPIView, VacancyListAPIView, VacancyTopTenAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('companies/', views.company_list),
    path('companies/<int:id>/', views.company_detail),
    path('companies/<int:id>/vacancies/', views.company_vacancy),

    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:id>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/', VacancyTopTenAPIView.as_view()),
]