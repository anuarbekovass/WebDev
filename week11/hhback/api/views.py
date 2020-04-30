from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company, Vacancy
from django.http import Http404
from heapq import nlargest


def company_list(request):
    companies = Company.objects.all()
    json_companies = [c.to_json() for c in companies]
    return JsonResponse(json_companies, safe=False)


def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        raise Http404
    return JsonResponse(company.to_json())


def company_vacancy(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        raise Http404
    vacancies = company.vacancy_set.all()
    json_vacancies = [v.to_json() for v in vacancies]
    return JsonResponse(json_vacancies, safe=False)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        raise Http404
    return JsonResponse(vacancy.to_json())


def vacancy_top_ten(request):
    try:
        vacancies = Vacancy.objects.order_by("-salary").all()[:10]
    except Vacancy.DoesNotExist as e:
        raise Http404
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

