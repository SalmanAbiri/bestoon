from django.shortcuts import render
from django.http import JasonResponse
from utils.jason import JASONEncoder

# Create your views here.
def submit_expense(request):
    """ user submit request an expense """
    return JasonResponse({'status':'ok'}, encoder=JASONEncoder)