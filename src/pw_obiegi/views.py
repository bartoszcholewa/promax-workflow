from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Obieg
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import ObiegCreateForm

class PwObiegiListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Obieg.objects.filter(
				Q(zamawiajacy__iexact=slug) |
				Q(zamawiajacy__icontains=slug)
				)
		else:
			queryset = Obieg.objects.all()
		return queryset
		
class PwObiegiDetailView(DetailView):
	queryset = Obieg.objects.all()


class ObiegCreateView(LoginRequiredMixin, CreateView):
	form_class = ObiegCreateForm
	template_name = 'pw_obiegi/normalny.html'
	#success_url = "/pw_obiegi/"
		
	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.handlowiec = self.request.user
		return super(ObiegCreateView, self).form_valid(form)
