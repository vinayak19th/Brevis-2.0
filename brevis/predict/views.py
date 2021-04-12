from django.shortcuts import render,redirect
from django.http import HttpResponse

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
    return render(request,'predict/index.html',{'trending_terms':trends[0],'trending_urls':trends[1],'form': form})

def summariser(request):
    newsurl = request.session.get('weblink')
    source,text = get_text(newsurl)
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            request.session['weblink'] = form.cleaned_data['weblink']
            return redirect('summariser')
    form = WebsiteForm()
    model = SummaryModel()
    summary = model.pred(text)[0]
    return render(request,'predict/output.html',{'text':source,'form': form,'text_summary':summary})