from django.shortcuts import render

from .models import  *


def paper (request):
    obj3 = Paper.objects.all()
    o=Authored.objects.all().prefetch_related ('p_title')
    obj1 = Authors.objects.all()
    obj2 = P_type.objects.all()
    obj4=Authored.objects.all()


    return render(request, 'scopus1/index.html', context={'authors':obj1,'paper':obj3,'ptype':obj2,'authored':o})