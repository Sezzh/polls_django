from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = 'results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
    url(r'^sezzh', views.sezzh, name = 'sezzh'),
    url(r'^sezzh-form-send$', views.sezzh_form_send, name="sezzh_form_send"),
]
