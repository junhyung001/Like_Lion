from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myView(request):
    
    return HttpResponse('Hello World!')

def oneView(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    opearator = request.GET.get('opearator')
    
    if opearator == '+':
        result = int(num1) + int(num2)
    elif opearator == '-':
        result = int(num1) - int(num2)
    elif opearator == '*':
        result = int(num1) * int(num2)
    elif opearator == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
    return render(request, 'firstapp/one.html', {'result' : result})

def twoView(request):
    name = '홍길동'
    return render(request, 'firstapp/two.html', {'name' : name})

def threeView(request):
    
    return render(request, 'firstapp/three.html')