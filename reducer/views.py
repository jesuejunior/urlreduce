from django.template.response import TemplateResponse
from reducer.forms import ReduceURLForm


def HomeTemplateView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        cxt = self.get_context_data()
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

@login_required
def my_links(r):
    data = {}
    return render_to_response('my-links.html',data, context_instance=RequestContext(r))

def reduce(r):
    if r.get('POST'):
        if r.user.is_authenticated():
            pass

    data = {}
    return render_to_response('my-links.html',data, context_instance=RequestContext(r))