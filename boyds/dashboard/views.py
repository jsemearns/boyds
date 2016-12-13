from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        context = {}
        return HttpResponse(render(request, self.template_name, context))
