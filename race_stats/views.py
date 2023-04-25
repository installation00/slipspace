from django.shortcuts import render
# import django_tables2 as tables2
# from .tables import get_table
# from django.forms import ChoiceField, Form
# from django.forms import ModelChoiceField
# from django_tables2 import RequestConfig

from .models import races
from .models import drivers
from .models import constructors
from .models import circuits
from .models import seasons
from .models import status
from .models import constructor_standings
from .models import constructor_results
from .models import driver_standings
from .models import sprint_results
from .models import qualifying
from .models import pit_stops
from .models import lap_times
from .models import results
from .tables import racesTable
from .tables import driversTable
from .tables import constructorsTable
from .tables import circuitsTable
from .tables import seasonsTable
from .tables import statusTable
from .tables import constructor_standingsTable
from .tables import constructor_resultsTable
from .tables import driver_standingsTable
from .tables import sprint_resultsTable
from .tables import qualifyingTable
from .tables import pit_stopsTable
from .tables import lap_timesTable
from .tables import resultsTable

# def home(request):
#     models = ['races', 'drivers', 'constructors', 'circuits', 'seasons', 'status', 'constructor_standings', 'constructor_results', 'driver_standings', 'sprint_results', 'qualifying', 'pit_stops', 'lap_times', 'results']
#     context = {}
#     context['races'] = list(races.objects.all())
#     context['models'] = models
#     return render(request, 'home.html', context)

def home(request):
    models = ['races','drivers','constructors','circuits','seasons','status','constructor_standings','constructor_results','driver_standings','sprint_results','qualifying','pit_stops','lap_times','results']
    return render(request, 'home.html', {'models': models})

def stats(request):
    model_name = request.POST.get('model-name')
    if model_name == 'races':
        table = racesTable(races.objects.all())
    elif model_name == 'drivers':
        table = driversTable(drivers.objects.all())
    elif model_name == 'constructors':
        table = constructorsTable(constructors.objects.all())
    elif model_name == 'circuits':
        table = circuitsTable(circuits.objects.all())
    elif model_name == 'seasons':
        table = seasonsTable(seasons.objects.all())
    elif model_name == 'status':
        table = statusTable(status.objects.all())
    elif model_name == 'constructor_standings':
        table = constructor_standingsTable(constructor_standings.objects.all())
    elif model_name == 'constructor_results':
        table = constructor_resultsTable(constructor_results.objects.all())
    elif model_name == 'driver_standings':
        table = driver_standingsTable(driver_standings.objects.all())
    elif model_name == 'sprint_results':
        table = sprint_resultsTable(sprint_results.objects.all())
    elif model_name == 'qualifying':
        table = qualifyingTable(qualifying.objects.all())
    elif model_name == 'pit_stops':
        table = pit_stopsTable(pit_stops.objects.all())
    elif model_name == 'lap_times':
        table = lap_timesTable(lap_times.objects.all())
    elif model_name == 'results':
        table = resultsTable(results.objects.all())
    else:
        table = None
    if table is not None:
        # table.paginate(page=request.GET.get("page", 1), per_page=50)
        return render(request, 'stats.html', {'table': table})
    else:
        return render(request, 'home.html')

# def racesFunc(request):
#     table = racesTable(races.objects.all())

#     return render(request, "races.html", {
#         "table": table
#     })

# def driversFunc(request):
#     table = driversTable(drivers.objects.all())

#     return render(request, "drivers.html", {
#         "table": table
#     })

# def constructorsFunc(request):
#     table = constructorsTable(constructors.objects.all())

#     return render(request, "constructors.html", {
#         "table": table
#     })

# def circuitsFunc(request):
#     table = circuitsTable(circuits.objects.all())

#     return render(request, "circuits.html", {
#         "table": table
#     })

# def seasonsFunc(request):
#     table = seasonsTable(seasons.objects.all())

#     return render(request, "seasons.html", {
#         "table": table
#     })

# def statusFunc(request):
#     table = statusTable(status.objects.all())

#     return render(request, "status.html", {
#         "table": table
#     })

# def constructor_standingsFunc(request):
#     table = constructor_standingsTable(constructor_standings.objects.all())

#     return render(request, "constructor_standings.html", {
#         "table": table
#     })

# def constructor_resultsFunc(request):
#     table = constructor_resultsTable(constructor_results.objects.all())

#     return render(request, "constructor_results.html", {
#         "table": table
#     })

# def driver_standingsFunc(request):
#     table = driver_standingsTable(driver_standings.objects.all())

#     return render(request, "driver_standings.html", {
#         "table": table
#     })

# def sprint_resultsFunc(request):
#     table = sprint_resultsTable(sprint_results.objects.all())

#     return render(request, "sprint_results.html", {
#         "table": table
#     })

# def qualifyingFunc(request):
#     table = qualifyingTable(qualifying.objects.all())

#     return render(request, "qualifying.html", {
#         "table": table
#     })

# def pit_stopsFunc(request):
#     table = pit_stopsTable(pit_stops.objects.all())

#     return render(request, "pit_stops.html", {
#         "table": table
#     })

# def lap_timesFunc(request):
#     table = lap_timesTable(lap_times.objects.all())

#     return render(request, "lap_times.html", {
#         "table": table
#     })

# def resultsFunc(request):
#     table = resultsTable(results.objects.all())

#     return render(request, "results.html", {
#         "table": table
#     })

# class racesListView(ListView):
#     model = races
#     table_class = racesTable
#     template_name = 'races.html'

# class driversListView(ListView):
#     model = drivers
#     table_class = driversTable
#     template_name = 'drivers.html'

# class constructorsListView(ListView):
#     model = constructors
#     table_class = constructorsTable
#     template_name = 'constructors.html'

# class circuitsListView(ListView):
#     model = circuits
#     table_class = circuitsTable
#     template_name = 'circuits.html'

# class seasonsListView(ListView):
#     model = seasons
#     table_class = seasonsTable
#     template_name = 'seasons.html'

# class statusListView(ListView):
#     model = status
#     table_class = statusTable
#     template_name = 'status.html'

# class constructor_standingsListView(ListView):
#     model = constructor_standings
#     table_class = constructor_standingsTable
#     template_name = 'constructor_standings.html'

# class constructor_resultsListView(ListView):
#     model = constructor_results
#     table_class = constructor_resultsTable
#     template_name = 'constructor_results.html'

# class driver_standingsListView(ListView):
#     model = driver_standings
#     table_class = driver_standingsTable
#     template_name = 'driver_standings.html'

# class sprint_resultsListView(ListView):
#     model = sprint_results
#     table_class = sprint_resultsTable
#     template_name = 'sprint_results.html'

# class qualifyingListView(ListView):
#     model = qualifying
#     table_class = qualifyingTable
#     template_name = 'qualifying.html'

# class pit_stopsListView(ListView):
#     model = pit_stops
#     table_class = pit_stopsTable
#     template_name = 'pit_stops.html'

# class lap_timesListView(ListView):
#     model = lap_times
#     table_class = lap_timesTable
#     template_name = 'lap_times.html'

# class resultsListView(ListView):
#     model = results
#     table_class = resultsTable
#     template_name = 'results.html'