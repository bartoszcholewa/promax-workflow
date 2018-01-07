from django.conf.urls import url
from pw_obiegi.views import PwObiegiListView, PwObiegiDetailView, ObiegCreateView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', PwObiegiListView.as_view(), name='list'),
    url(r'^dodaj/$', TemplateView.as_view(template_name='pw_obiegi/dodaj.html'), name='dodaj'),
    url(r'^dodaj/normalny/$', ObiegCreateView.as_view(), name='dodaj-normalny'),
    url(r'^dodaj/pozasystemowy/$', ObiegCreateView.as_view(), name='dodaj-pozasystemowy'),
    url(r'^(?P<slug>[\w-]+)/$', PwObiegiDetailView.as_view(), name='detail'),

]
