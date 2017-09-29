from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def index(request):
	return render(request, 'app/index.html')


def ask(request):
	return render(request, 'app/ask.html')

def question(request):
	return render(request, 'app/question.html')