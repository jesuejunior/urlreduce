#encoding: utf-8
import urllib2
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.template.response import TemplateResponse
from django.views.defaults import page_not_found
from common.login_required_mixin import LoginRequiredMixin
from reducer.forms import ReduceURLForm
from django.views.generic import View, TemplateView, RedirectView
from reducer.models import Link, Owner


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
        authenticated = request.user.is_authenticated()
        if authenticated:
            req = req.copy()
            req[u'user'] = request.user.pk

        form = ReduceURLForm(req)
        #Não deixar cadastrar URL repetida economia de disco/memoria
        if form.is_valid():
            link = Link.objects.filter(url=form.cleaned_data['url'])
            link = link[0] if link else None
            if not link:
                link = form.save()

            if authenticated:
                owner, created = Owner.objects.get_or_create(link=link)
                owner.owners.add(request.user)

            cxt['link'] = link.to_dict()
        else:
            cxt['link'] = '500'
        #TODO - Se a url já estiver cadastrada o dono não muda e as urls existente só
        #TODO - aparece para a primeira pessoa, pensar como corrigir isso
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
        links = Link.objects.filter(owner__owners=request.user)
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
        url_hash = kwargs.get('url_hash')
        try:
            link = Link.objects.decode(url_hash)
            self.url = urllib2.unquote(link)
            return super(GoToRedirectView, self).get(request, *args, **kwargs)
        except Link.DoesNotExist:
            return page_not_found(request)
