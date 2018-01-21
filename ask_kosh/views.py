from django.shortcuts import render, redirect, resolve_url
from django.template import RequestContext
from django.contrib.auth.models import User
from ask_kosh.core.forms import SignUpForm, SignInForm, QuestionForm, ProfileForm
from django.contrib.auth import login, authenticate, logout

from ask_kosh.models import Question


# Create your views here.


def index(request):
	# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

	return render(request, 'ask_kosh/index.html')


# if request.method == "POST":
# 	# form = NewQuestionForm(request.POST)
# 	print(request.POST)
# 	# question_id = Question(form)
# 	return render(request, 'ask_kosh/ask_kosh.html', {'form': form})
#
# else:


def ask_kosh(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			question  = form.save()
			return redirect(f'/question/{question.id}')
	else:
		form = QuestionForm()
	print(request.user)
	return render(request, 'ask_kosh/ask_kosh.html', {'form': form})


def question(request, question_id):
	# if request.method == "POST":
	question = Question.objects.get(id=question_id)
	# form = QuestionForm(question)
	return render(request, 'ask_kosh/question.html', {'question': question})


def signin(request):
	if request.method == "POST":
		form = SignInForm(request.POST)
		if form.is_valid():
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
			if user is not None:
				if user.is_active:
					login(request, user)
			return redirect('/signin/')
	else:
		form = SignUpForm()

	return render(request, 'ask_kosh/signup.html', {'form': form})


def signout(request):
	logout(request)
	return redirect('index')


def hot(request):
	return render(request, 'ask_kosh/hot.html')


def year(request, n):
	return render(request, 'ask_kosh/index.html')


def tag(request, tag):
	return render(request, 'ask_kosh/tag.html')


def settings(request):
	if request.method == "POST":
		form = ProfileForm(request.POST)
	else:
		form = ProfileForm()
	print(request.user.profile)
	return render(request, 'ask_kosh/settings.html', {'form': form})

# def paginate(query_set, request):
#
# 	return object_page, Paginator
