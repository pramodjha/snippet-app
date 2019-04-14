from django.conf.urls import include,url
from . import views

urlpatterns = [
	url(r'^home/', views.home, name='home'),
	url(r'^about/', views.about, name='about'),
	url(r'^learn/', views.learn, name='learn'),
	url(r'^blog/', views.blog, name='blog'),
	url(r'^snippet/', views.snippet, name='snippet'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^home_add_form/', views.home_add_form, name='homeaddform'),
	url(r'^home_edit_form/(?P<home_id>\d+)$', views.home_edit_form, name='homeeditform'),
	url(r'^about_add_form/', views.about_add_form, name='aboutaddform'),
	url(r'^about_edit_form/(?P<about_id>\d+)$', views.about_edit_form, name='abouteditform'),
	url(r'^snippet_add_form/(?P<snippet_topics_id>\d+)$', views.snippet_add_form, name='snippetaddform'),
	url(r'^snippet_edit_form/(?P<snippet_data_id>\d+)$', views.snippet_edit_form, name='snippeteditform'),
	url(r'^snippet_topics/(?P<snippet_topics_id>\d+)$', views.snippet_topics, name='snippettopics'),
	url(r'^learn_add_form/(?P<learn_topics_id>\d+)$', views.learn_add_form, name='learnaddform'),
	url(r'^learn_edit_form/(?P<learn_data_id>\d+)$', views.learn_edit_form, name='learneditform'),
	url(r'^learn_topics/(?P<learn_topics_id>\d+)$', views.learn_topics, name='learntopics'),
	url(r'^blog_add_form/', views.blog_add_form, name='blogaddform'),
	url(r'^blog_edit_form/(?P<blog_id>\d+)$', views.blog_edit_form, name='blogeditform'),
	url(r'^blog_topics/(?P<blog_id>\d+)$', views.blog_topics, name='blogtopics'),

    ]
