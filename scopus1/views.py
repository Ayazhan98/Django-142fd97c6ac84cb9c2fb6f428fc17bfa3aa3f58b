from django.shortcuts import render
from .models import *


def paper (request):
    publications = Paper.objects.all()
    authored = Authored.objects.all()
    authors = Authors.objects.all()
    publication_types = P_type.objects.all()
    authored1 = Authored.objects.all().order_by('author')
    return render(request, 'scopus1/index.html', context={'authors':authors,'paper':publications,'authored1':authored1 ,'authored':authored})