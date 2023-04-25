from django.urls import path
from . import views

# from .views import races
# from .views import drivers
# from .views import constructors
# from .views import circuits
# from .views import seasons
# from .views import status
# from .views import constructor_standings
# from .views import constructor_results
# from .views import driver_standings
# from .views import sprint_results
# from .views import qualifying
# from .views import pit_stops
# from .views import lap_times
# from .views import results

app_name = 'race_stats'

urlpatterns = [
    path('', views.home, name='home'),
    path('stats/', views.stats, name='stats'),
    # path("admin/", admin.site.urls),
    # path("races/", races, name='races.html'),
    # path("drivers/", drivers, name='drivers.html'),
    # path("constructors/", constructors, name='constructors.html'),
    # path("circuits/", circuits, name='circuits.html'),
    # path("seasons/", seasons, name='seasons.html'),
    # path("status/", status, name='status.html'),
    # path("constructor_standings/", constructor_standings, name='constructor_standings.html'),
    # path("constructor_results/", constructor_results, name='constructor_results.html'),
    # path("driver_standings/", driver_standings, name='driver_standings.html'),
    # path("sprint_results/", sprint_results, name='sprint_results.html'),
    # path("qualifying/", qualifying, name='qualifying.html'),
    # path("pit_stops/", pit_stops, name='pit_stops.html'),
    # path("lap_times/", lap_times, name='lap_times.html'),
    # path("results/", results, name='results.html'),
]