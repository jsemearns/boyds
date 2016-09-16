from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from userprofile.forms import LoginForm


class LoginView(TemplateView):
	template_name = 'login.html'

	def get(self, request, *args, **kwargs):
		context = {}
		form = LoginForm()
		context['form'] = form
		return HttpResponse(render(request, self.template_name, context))

	def post(self, request, *args, **kwargs):
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		if username and password:
			user = authenticate(username=username, password=password)
			if user.is_active:
				login(request, user)
		return HttpResponse()