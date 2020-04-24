from django.http.response import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from api.models import Company


@csrf_exempt
def company_list(request):
    companies = Company.objects.all()
    json_companies = [c.to_json() for c in companies]
    return JsonResponse(json_companies, safe=False)


@csrf_exempt
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
