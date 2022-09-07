import json

from django.conf import settings
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from mobility.models import Post
from mobility.forms import MetricForm, CountyForm, CountyCompareForm

def index(request):
    template = loader.get_template('mobility/index.html')
    context = {
        'filler': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))

def county_details(request):
    fips = request.GET.get('fips', None)
    form = CountyForm(initial={'fips': request.GET.get('fips', None)})
    context = {'fips': fips, 'form': form, 'streamlit_url': settings.STREAMLIT_URL}
    template = loader.get_template('mobility/county_details.html')
    return HttpResponse(template.render(context, request))


def national_view(request):
    metric = request.GET.get('metric', 'population')
    metric_form = MetricForm(initial={'metric': request.GET.get('metric', 'population')})
    template = loader.get_template('mobility/national_view.html')
    context = { 'form': metric_form, 'metric': metric, 'streamlit_url': settings.STREAMLIT_URL}
    return HttpResponse(template.render(context, request))

def county_finder(request):
    template = loader.get_template('mobility/county_finder.html')
    return HttpResponse(template.render({'streamlit_url': settings.STREAMLIT_URL}, request))

class PostListView(ListView):
    model = Post
    ordering = ['-published_date']

    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(published_date__isnull=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):

    model = Post

class CountyComparison(TemplateView):
    template_name = 'mobility/county_comparison.html'

    def get_context_data(self, **kwargs):
        context = super(CountyComparison, self).get_context_data(**kwargs)  
        fips1 = self.request.GET.get('fips1', None)
        fips2 = self.request.GET.get('fips2', None)

        form = CountyCompareForm(initial={'fips1': fips1, 'fips2': fips2})
        context.update({
            'form': form, 
            'fips1': fips1,
            'fips2': fips2, 
            'streamlit_url': settings.STREAMLIT_URL
        })
        return context
