#encoding: utf-8
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.template.response import TemplateResponse
from common.login_required_mixin import LoginRequiredMixin
from reducer.forms import ReduceURLForm
from django.views.generic import View, TemplateView, RedirectView
from reducer.models import Link


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



class MyLinksTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'my-links.html'
    def get(self, request, *args, **kwargs):
        links = Link.objects.owner(request.user)
        paginator = Paginator(links, 2)

        page = request.GET.get('page')
        try:
            links = paginator.page(page)
        except PageNotAnInteger:
            links = paginator.page(1)
        except (EmptyPage, InvalidPage):
            links = paginator.page(paginator.num_pages)

        cxt = {'links': links}
        return self.render_to_response(cxt)

class GoToRedirectView(RedirectView):
    def get(self, request, *args, **kwargs):
        url_hash = kwargs.get()
