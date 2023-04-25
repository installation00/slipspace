# from django_tables2 import Table
import django_tables2 as tables
# from django.apps import apps

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

class racesTable(tables.Table):
    class Meta:
        model = races
        # fields = ('raceId', 'year', 'round', 'circuitId', 'name', 'date',
        #           'time', 'url', 'fp1_date', 'fp1_time', 'fp2_date',
        #           'fp2_time', 'fp3_date', 'fp3_time', 'quali_date',
        #           'quali_time', 'sprint_date', 'sprint_time')

class driversTable(tables.Table):
    class Meta:
        model = drivers
        # fields = ('driverId', 'driverRef', 'number', 'code', 'forename',
        #           'surname', 'dob', 'nationality', 'url')

class constructorsTable(tables.Table):
    class Meta:
        model = constructors
        # fields = ('constructorId', 'constructorRef', 'name', 'nationality', 'url')

class circuitsTable(tables.Table):
    class Meta:
        model = circuits
        # fields = ('circuitId', 'circuitRef', 'name', 'location', 'country',
        #           'lat', 'lng', 'alt', 'url')

class seasonsTable(tables.Table):
    class Meta:
        model = seasons
        # fields = ('year', 'url')

class statusTable(tables.Table):
    class Meta:
        model = status
        # fields = ('statusId', 'status')

class constructor_standingsTable(tables.Table):
    class Meta:
        model = constructor_standings
        # fields = ('constructorStandingsId', 'raceId', 'constructorId',
        #           'points', 'position', 'positionText', 'wins')

class constructor_resultsTable(tables.Table):
    class Meta:
        model = constructor_results
        # fields = ('constructorResultsId', 'raceId', 'constructorId', 'points', 'status')

class driver_standingsTable(tables.Table):
    class Meta:
        model = driver_standings
        # fields = ('driverStandingsId', 'raceId', 'driverId', 'points',
        #           'position', 'positionText', 'wins')

class sprint_resultsTable(tables.Table):
    class Meta:
        model = sprint_results
        # fields = ('resultId', 'raceId', 'driverId', 'constructorId', 'number',
        #           'grid', 'position', 'positionText', 'positionOrder',
        #           'points', 'laps', 'time', 'milliseconds', 'fastestLap',
        #           'fastestLapTime', 'statusId')

class qualifyingTable(tables.Table):
    class Meta:
        model = qualifying
        # fields = ('qualifyingId', 'raceId', 'driverId', 'constructorId',
        #           'number', 'position', 'q1', 'q2', 'q3')

class pit_stopsTable(tables.Table):
    class Meta:
        model = pit_stops
        # fields = ('raceId', 'driverId', 'stop', ' lap', 'time', 'duration',
        #           'milliseconds')

class lap_timesTable(tables.Table):
    class Meta:
        model = lap_times
        # fields = ('raceId', 'driverId', 'lap', 'position', 'time',
        #           'milliseconds')

class resultsTable(tables.Table):
    class Meta:
        model = results
        # fields = ('resultId', 'raceId', 'driverId', 'constructorId', 'number',
        #           'grid', 'position', 'positionText', 'positionOrder',
        #           'points', 'laps', 'time', 'milliseconds', 'fastestLap',
        #           'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId')