from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.list_companies, name='list_companies'),
    path('companies/<int:id>/', views.get_company,  name='get_company'),
    path('companies/<int:id>/vacancies/', views.company_vacancies, name='company_vacancies'),
    path('vacancies/', views.list_vacancies, name='list_vacancies'),
    path('vacancies/<int:id>/', views.get_vacancy, name='get_vacancy'),
    path('vacancies/top_ten/', views.top_ten_vacancies, name='top_ten_vacancies'),
]
