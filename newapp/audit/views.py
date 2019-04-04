from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db import models
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserSession


class IndexView(LoginRequiredMixin, generic.TemplateView):

    template_name = 'audit/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = UserSession.objects.filter(loggedout=None)\
            .values('user_id').annotate(count=models.Count('user_id'))\
            .values('user_id__username', 'count')

        return context

class SessionsView(LoginRequiredMixin, generic.TemplateView):

    template_name = 'audit/sessions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actives'] = UserSession.objects.filter(loggedout=None).order_by('-id')
        print(context)
        return context
