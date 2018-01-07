from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView
from .forms import JoinForm
from .mixins import AjaxFormMixin

class JoinFormView(AjaxFormMixin, FormView):
	form_class = JoinForm
	template_name = 'urlfiller/urlfiller.html'
	success_url = '/form-success/'
