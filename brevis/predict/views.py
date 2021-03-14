from django.shortcuts import render
from django.http import HttpResponse

from .apps import PredictConfig, NewsConfig
from .paper import *
from .bart import SummaryModel
from .forms import WebsiteForm

def index(request):
    trends = trending()
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            request.session['weblink'] = form.cleaned_data['weblink']
            return redirect('summariser')
    form = WebsiteForm()
    return render(request,'main/index.html',{'trending_terms':trends[0],'trending_urls':trends[1],'form': form})
