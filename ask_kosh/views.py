from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from ask_kosh.core.forms import SignUpForm
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
	# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
	return render(request, 'ask_kosh/index.html')


def ask_kosh(request):
	return render(request, 'ask_kosh/ask_kosh.html')

def question(request, question):
	return render(request, 'ask_kosh/question.html')


def login(request):
	return render(request, 'ask_kosh/login.html')


def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = SignUpForm()

	return render(request, 'ask_kosh/signup.html', {'form': form})


def hot(request):
	return render(request, 'ask_kosh/hot.html')
	

def year(request, n):
	print(n)
	return render(request, 'ask_kosh/index.html')


def tag(request, tag):

	return render(request, 'ask_kosh/tag.html')


# def paginate(query_set, request):
#
# 	return object_page, Paginator

