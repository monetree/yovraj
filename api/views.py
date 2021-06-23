from .models import Users, Customers
from django.http import JsonResponse

def users(request):
    res = list(Users.objects.using('default').values())
    return JsonResponse(res, safe=False)

def customers(request):
    res = list(Customers.objects.using('customers').values())
    return JsonResponse(res, safe=False)