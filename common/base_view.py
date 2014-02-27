from django.views.generic import TemplateView
from common.login_required_mixin import LoginRequiredMixin

__author__ = 'jesuejunior'

class BaseView(LoginRequiredMixin, TemplateView):
    #fica pra depois
    pass