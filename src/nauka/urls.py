"""nauka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pw_obiegi.views import PwObiegiListView, PwObiegiDetailView, ObiegCreateView
from blog.views import blog
from urlfiller.views import JoinFormView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='homepage/index.html'), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^contact/$', TemplateView.as_view(template_name='homepage/contact.html'), name='contact'),
    url(r'^pw_obiegi/', include('pw_obiegi.urls', namespace='obiegi')),
    #url(r'^pw_obiegi/$', PwObiegiListView.as_view(), name='obiegi'),
    #url(r'^pw_obiegi/dodaj/$', TemplateView.as_view(template_name='pw_obiegi/dodaj.html'), name='dodaj-obieg'),
    #url(r'^pw_obiegi/dodaj/normalny/$', ObiegCreateView.as_view(), name='dodaj-obieg-normalny'),
    #url(r'^pw_obiegi/dodaj/pozasystemowy/$', ObiegCreateView.as_view(), name='dodaj-obieg-pozasystemowy'),
    #url(r'^pw_obiegi/(?P<slug>[\w-]+)/$', PwObiegiDetailView.as_view(), name='obieg-detail'),
    url(r'^urlfiller/$', JoinFormView.as_view()),
    url(r'^blog/$', blog, name='blog'),
]
