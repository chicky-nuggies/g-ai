from django.shortcuts import render
from django.http import HttpResponse





def company(request):

            
    return render(request, "company/company.html")