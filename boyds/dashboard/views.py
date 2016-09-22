from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class DashboardView(TemplateView):
	template_name = ''
	def get(self, request, *args, **kwargs):
		return HttpResponse()