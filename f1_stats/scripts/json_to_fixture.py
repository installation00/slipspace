import json

models = ['races', 'drivers', 'constructors', 'circuits', 'seasons', 'status', 'constructor_standings', 'constructor_results', 'driver_standings', 'sprint_results', 'qualifying', 'pit_stops', 'lap_times', 'results']

for model in models:
    filepath = f'C:\\Users\\hmkur\\Desktop\\coding\\f1_stats\\race_stats\\unconverted_fixtures\\{model}.json'
    with open(filepath, encoding='utf-8') as f:
        data = f.readlines()

    headers = data[0].strip().split(',')
    objects = []
    for line in data[1:]:
        fields = line.strip().split(',')
        obj = {
            'model': f'race_stats.{model}', # replace with your app and model name
            'fields': {headers[i]: fields[i] for i in range(len(headers))}
        }
        objects.append(obj)

    writepath = f'C:\\Users\\hmkur\\Desktop\\coding\\f1_stats\\race_stats\\fixtures\\{model}.json'
    with open(writepath, 'w') as f:
        json.dump(objects, f)