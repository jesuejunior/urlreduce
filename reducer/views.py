#encoding: utf-8
from django.template.response import TemplateResponse
from reducer.forms import ReduceURLForm
from django.views.generic import View

class HomeTemplateView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        cxt = self.get_context_data()
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        cxt = self.get_context_data()
        req = request.POST

        if request.user.is_authenticated():
            req = req.copy()
            req[u'user'] = request.user.pk

        form = ReduceURLForm(req)

        if form.is_valid():
            link = form.save()
            cxt['link'] = link.to_dict()
        else:
            cxt['link'] = '500'

        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def get_context_data(self, **kwargs):
        cxt = {}
        cxt['form_url'] = ReduceURLForm
        return cxt



class MyLinksTemplateView(View):
    template_name = 'my-links.html'