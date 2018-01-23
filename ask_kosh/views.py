from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from ask_kosh.core.forms import SignUpForm, SignInForm, QuestionForm, ProfileForm, UserForm, AnswerForm
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from ask_kosh.models import Question, Answer


# Create your views here.


def index(request):
	questions = Question.objects.all()
	paginator = Paginator(questions, 5)
	page = request.GET.get('page')
	context = {}
	try:
		# Если существует, то выбираем эту страницу
		context['questions'] = paginator.page(page)
	except PageNotAnInteger:
		# Если None, то выбираем первую страницу
		context['questions'] = paginator.page(1)
	except EmptyPage:
		# Если вышли за последнюю страницу, то возвращаем последнюю
		context['questions'] = paginator.page(paginator.num_pages)

	return render(request, 'ask_kosh/index.html', context)




def ask_kosh(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			question  = form.save()
			return redirect(f'/question/{question.id}')
	else:
		form = QuestionForm()
	return render(request, 'ask_kosh/ask_kosh.html', {'form': form})


def question(request, question_id):
	question = Question.objects.get(id=question_id)
	if request.method == "POST":
		answer_form = AnswerForm(request.POST)
		if answer_form.is_valid():
			question_id = answer_form.cleaned_data.get('question_id')
			question = Question.objects.get(id=question_id)
			user = User.objects.get(id=request.user.id)
			answer = Answer(question=question, user=user, text=answer_form.cleaned_data.get('text'))
			answer.save()
	context = {}
	context['question'] = question
	context['answer_form'] = AnswerForm(initial={'question_id':question_id})
	context['answers'] = Answer.objects.filter(question=question)
	return render(request, 'ask_kosh/question.html', context)


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


@login_required
@transaction.atomic
def settings(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('/settings/')
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
	return render(request, 'ask_kosh/settings.html', {
		'user_form': user_form,
		'profile_form': profile_form
		})

# def paginate(query_set, request):
#
# 	return object_page, Paginator
