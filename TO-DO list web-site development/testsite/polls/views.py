from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.db import connections

from .models import To_do


def index(request, pk):
    to_do_list = get_object_or_404(To_do, pk=pk)
    template = loader.get_template('polls/index.html')
    context = { 'to_do_list':to_do_list }
    return HttpResponse(template.render(context, request))

