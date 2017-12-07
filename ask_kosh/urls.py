from django.conf.urls import url 

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^ask_kosh/$', views.ask_kosh, name='ask_kosh'),
	url(r'^login/$', views.login, name='login'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^hot/$', views.hot, name='hot'),
	url(r'^articles/(?P<n>[0-9]{1,4})/$', views.year, name="year"),
	url(r'^tag/(?P<tag>[0-9]{1,4})/$', views.tag, name="tag"),
	url(r'^question/(?P<question>[0-9]{1,4})/$', views.question, name="question"),

]