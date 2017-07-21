from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpRequest, HttpRequest, Http404
from django.template import RequestContext
from .models import Literature

# Create your views here.

def texts(request):
    text = Literature.objects.order_by('date_posted')
    "Renders the Literature page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'literature/literature.html',
        {'texts':text}
    )

def text(request, slug):
    text = get_object_or_404(Literature, slug=slug)
    title = text.title
    return render(request, 'text.html', {'text': text, 'title': title})
