import time
import requests
from django.apps import apps

from race_stats.models import races
from race_stats.models import drivers
from race_stats.models import constructors
from race_stats.models import circuits
from race_stats.models import seasons
from race_stats.models import status
from race_stats.models import constructor_standings
from race_stats.models import constructor_results
from race_stats.models import driver_standings
from race_stats.models import sprint_results
from race_stats.models import qualifying
from race_stats.models import pit_stops
from race_stats.models import lap_times
from race_stats.models import results

models = ['races', 'drivers', 'constructors', 'circuits', 'seasons', 'status', 'constructor_standings', 'constructor_results', 'driver_standings', 'sprint_results', 'qualifying', 'pit_stops', 'lap_times', 'results']
models_count = models.count()

model_fields = {
    races: ['raceId', 'year', 'round', 'circuitId', 'name', 'date', 'time', 'url', 'fp1_date', 'fp1_time', 'fp2_date', 'fp2_time', 'fp3_date', 'fp3_time', 'quali_date', 'quali_time', 'sprint_date', 'sprint_time'],
    drivers: ['driverId', 'driverRef', 'number', 'code', 'forename', 'surname', 'dob', 'nationality', 'url'],
    constructors: ['constructorsId', 'constructorRef', 'name', 'nationality', 'url'],
    circuits: ['circuitId', 'circuitRef', 'name', 'location', 'country', 'lat', 'lng', 'alt', 'url'],
    seasons: ['year', 'url'],
    status: ['statusId', 'status'],
    constructor_standings: ['constructorStandingsId', 'raceId', 'constructorId', 'points', 'position', 'positionText', 'wins'],
    constructor_results: ['constructorResultsId', 'raceId', 'constructorId', 'points', 'status'],
    driver_standings: ['driverStandingsId', 'raceId', 'driversId', 'points', 'position', 'positionText', 'wins'],
    sprint_results: ['resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'position', 'positionText', 'positionOrder', 'points', 'laps', 'time', 'milliseconds', 'fastestLap', 'fastestLapTime', 'statusId'],
    qualifying: ['qualifyId', 'raceId', 'driverId', 'constructorId', 'number', 'position', 'q1', 'q2', 'q3'],
    pit_stops: ['raceId', 'driverId', 'stop', 'lap', 'time', 'duration', 'milliseconds'],
    lap_times: ['raceId', 'driverId', 'lap', 'position', 'time', 'milliseconds'],
    results: ['resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'position', 'positionText', 'positionOrder', 'points', 'laps', 'time', 'milliseconds', 'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId']
}

data_check_count = 0

for model_name in models:
    response = requests.get(f'https://ergast.com/api/f1/{model_name}?limit={limit}&offset={offset}')
    data = response.json()

    print(f'JSON data received for the ->{model_name}<- model')
    time.sleep(5)
    
    model = apps.get_model(app_label='race_stats', model_name=model_name)
    total = 0
    offset = 0
    limit = 500

    print(f'Total: {total}\nOffset: {offset}\nLimit: {limit}')
    time.sleep(5)
    
    while offset < total:
        for obj in data:
            if not model.objects.filter(id=obj['id']).exists():
                fields = {}
                for field in model_fields[model]:
                    fields[field] = obj.get(field)
                model.objects.create(**fields).save()
                print('Data Added')
            else:
                print("Data Found")

        offset += limit
    data_check_count += 1
    print(f'******MODEL {model_name} COMPLETE******')
    time.sleep(5)

print(f'Model Count: {models_count}\nCompleted Models: {data_check_count}')