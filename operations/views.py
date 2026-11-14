from django.shortcuts import render

from django.views.generic import View
from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class AdditionView(View):
    def post(self,request):
        json_data = request.body
        
        form_data = loads(json_data)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1+n2
        response_data = {
            "addition_result":result,
        }

        return JsonResponse(response_data)
    
    
@method_decorator(csrf_exempt,name="dispatch")
class SubtractionView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1-n2
        response_data = {
            "subtraction_result":result
        }
        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class MultiplicationView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result = n1*n2
        response_data = {
            "multiplication_result":result
        }
        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class DivitionView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result = n1/n2
        response_data = {
            "division_result":result
        }
        return JsonResponse(response_data)