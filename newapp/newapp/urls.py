from django.contrib import admin
from django.urls import include, path, Resolver404
from django.views.generic.base import TemplateView
from django.core import exceptions
from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required


def raiseError403(request):
    raise exceptions.PermissionDenied("Trial Error")


def raiseError404(request):
    raise Resolver404("Trial Error")


def raiseError500(request):
    raise Exception("Trial Error")


# Root Patterns:
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('protected/', raiseError403),
    path('not-found/', raiseError404),
    path('error/', raiseError500),
    # -----
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # -----
    path('polls/', include('polls.urls')),
    path('audit/', include('audit.urls')),
]


# Errors Handler:
def handleErrors(request, exception, *args, **kwargs):
    context = {
        'url': request.build_absolute_uri(),
        'errortype': type(exception).__name__,
        'message': str(exception)
    }

    if isinstance(exception, exceptions.PermissionDenied):
        context['status'] = 403
    elif isinstance(exception, Resolver404):
        context['status'] = 404
    else:
        context['status'] = 500

    return render(request, 'errors.html', status=context['status'], context=context, content_type='text/html')


# Handler binding:
handler400 = handleErrors
handler403 = handleErrors
handler404 = handleErrors
#handler500 = handleErrors
