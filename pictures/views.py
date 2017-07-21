from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpRequestm HttpRequest, Http404
from django.template import RequestContext
from .models import PictureArt

# Create your views here.

def pictures(request):
    # gets the picture art page
    picture = PictureArt.objects.order_by('date_posted').reverse
    "Renders the Picture Art page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'picture_art.html',
        {'pictures': picture},
        context_instance=RequestContext(request,
        {
            'title': 'Picture Art Timeline'
        })
    )

def picture(request, slug):
    picture = get_object_or_404(PictureArt, slug=slug)
    title = picture.title
    return render(request, 'picture.html', {'picture': picture, 'title': title})
