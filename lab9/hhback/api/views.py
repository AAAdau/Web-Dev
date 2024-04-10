from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy

def list_companies(request):
    companies = Company.objects.all()
    data = {'companies': list(companies.values())}
    return JsonResponse(data, safe=False)

def get_company(request, id):
    company = get_object_or_404(Company, id=id)
    data = {'company': {
        'name': company.name,
        'description': company.description,
        'city': company.city,
        'address': company.address
    }}
    return JsonResponse(data)

def company_vacancies(request, id):
    company = get_object_or_404(Company, id=id)
    vacancies = company.vacancies.all()
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)

def list_vacancies(request):
    vacancies = Vacancy.objects.all()
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)

def get_vacancy(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    data = {'vacancy': {
        'name': vacancy.name,
        'description': vacancy.description,
        'salary': vacancy.salary,
        'company': vacancy.company.name
    }}
    return JsonResponse(data)

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)
