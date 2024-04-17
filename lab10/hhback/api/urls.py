# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.list_companies, name='list_companies'),
    path('companies/<int:id>/', views.get_company, name='get_company'),
    path('companies/<int:id>/vacancies/', views.company_vacancies, name='company_vacancies'),
    path('vacancies/', views.list_vacancies, name='list_vacancies'),
    path('vacancies/<int:id>/', views.get_vacancy, name='get_vacancy'),
    path('vacancies/top_ten/', views.top_ten_vacancies, name='top_ten_vacancies'),
    path('class/companies/', views.CompanyList.as_view(), name='company-list'),
    path('class/companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
    path('class/vacancies/', views.VacancyList.as_view(), name='vacancy-list'),
    path('class/vacancies/<int:pk>/', views.VacancyDetail.as_view(), name='vacancy-detail'),
    path('class/vacancies/top_ten/', views.TopTenVacancies.as_view(), name='top-ten-vacancies'),
]
