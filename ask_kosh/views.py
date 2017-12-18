from django.shortcuts import render, redirect, resolve_url
from django.template import RequestContext
from django.contrib.auth.models import User
from ask_kosh.core.forms import SignUpForm, SignInForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def index(request):
	print("INDEX")
	# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
	return render(request, 'ask_kosh/index.html')


def ask_kosh(request):
	return render(request, 'ask_kosh/ask_kosh.html')


def question(request, question):
	return render(request, 'ask_kosh/question.html')


def signin(request):
	if request.method == "POST":
		form = SignInForm(request.POST)
		if form.is_valid():
			print(form)
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')
			else:
				return render(request, 'ask_kosh/signin.html', {'form': form, 'user': user})
	else:
		form = SignInForm()
	return render(request, 'ask_kosh/signin.html', {'form': form})


def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			# user = User.objects.create_user(username, email, password)
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index', {'user': user})
	else:
		form = SignUpForm()

	return render(request, 'ask_kosh/signup.html', {'form': form})


def signout(request):
	logout(request)
	return redirect('index')



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

