from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import SuspiciousOperation

from .models import CustomUser


class ProfileView(LoginRequiredMixin, generic.TemplateView):

    template_name = 'users/profile.html'
    model = CustomUser

    def get_context_data(self, *args, **kwargs):
        pk = kwargs.get('pk')
        u = get_object_or_404(CustomUser, id=pk)
        if (u == self.request.user) or (self.request.user.is_superuser):
            context = super().get_context_data(**kwargs)
            context['user_map'] = model_to_dict(u, exclude=['password', 'is_superuser', 'is_staff', 'groups', 'user_permissions'])
            return context
        else:
            raise SuspiciousOperation("Access denied for %s (you are logged as %s)" % (u, self.request.user))
