from django.conf.urls import url 

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^ask_kosh/$', views.ask_kosh, name='ask_kosh'),
	url(r'^question/$', views.question, name='question'),
	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	# url(r'^hot/$', views.hot, name='hot'),
	# url(r'^articles/(?P<year>[0-9]{4})/$', views.year, name="year"),

]