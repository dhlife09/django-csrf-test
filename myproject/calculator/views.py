# calculator/views.py

from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    if request.method == "POST":
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        result = val1 + val2
        return render(request, 'result.html', {'result': result})
    return render(request, 'index.html')
