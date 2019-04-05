from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db import models
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import SuspiciousOperation

from users.models import CustomUser
from .models import UserSession


class IndexView(LoginRequiredMixin, generic.TemplateView):

    template_name = 'audit/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sessions'] = UserSession.objects.all().filter(loggedout=None)\
            .values('user_id').annotate(count=models.Count('user_id'))\
            .values('user_id__username', 'count')
        context['users'] = CustomUser.objects.all().order_by('username')
        return context


class SessionsView(LoginRequiredMixin, generic.TemplateView):

    template_name = 'audit/sessions.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        if pk:
            u = get_object_or_404(CustomUser, pk=pk)
            if (u == self.request.user) or (self.request.user.is_superuser):
                context['sessions'] = UserSession.objects.filter(user_id=pk).order_by('-id')
                context['subtitle'] = "Sessions for %s" % u.username
            else:
                raise SuspiciousOperation("Access denied for %s (you are logged as %s)" % (u, self.request.user))
        else:
            context['sessions'] = [u for u in UserSession.objects.all().order_by('-id') if u.is_active()]
            context['subtitle'] = "Active Sessions"
        return context
