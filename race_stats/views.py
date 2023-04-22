from django.shortcuts import render
# from django.apps import apps
from race_stats.models import races

def home(request):
    models = ['races']
    context = {}
    context['races'] = list(races.objects.all())
    context['models'] = models
    # for model in models:
    #     context[model] = list(model.objects.all())
    # print(context[races])
    context['test'] = 0
    return render(request, 'home.html', context)