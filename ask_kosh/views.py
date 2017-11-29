from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def index(request):
	return render(request, 'ask_kosh/index.html')


def ask_kosh(request):
	return render(request, 'ask_kosh/ask_kosh.html')

def question(request):
	return render(request, 'ask_kosh/question.html')


def login(request):
	return render(request, 'ask_kosh/login.html')


def register(request):
	return render(request, 'ask_kosh/register.html')


def year(request, n):
	print(n)
	return render(request, 'ask_kosh/index.html')