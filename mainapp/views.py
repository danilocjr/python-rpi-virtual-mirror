from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


def index(request):
    template = loader.get_template('index.html')
    context = {
        'flag': 5,
    }
    return HttpResponse(template.render(context, request))