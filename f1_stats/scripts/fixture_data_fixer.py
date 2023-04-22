import os
import json

fixture_dir = 'C:\\Users\\hmkur\\Desktop\\coding\\f1_stats\\race_stats\\fixtures'

for filename in os.listdir(fixture_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(fixture_dir, filename)
        with open(filepath, 'r+', encoding='utf-8') as f:
            fixture_data = json.load(f)
            for obj in fixture_data:
                for field, value in obj['fields'].items():
                    if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
                        try:
                            date_obj = json.loads(value)
                            if isinstance(date_obj, str) and '-' in date_obj:
                                obj['fields'][field] = date_obj.strip('"')
                        except ValueError:
                            pass
                    # if isinstance(value, str) and value.startswith('"') and len(value) == 10 and value.count('-') == 2:
                    #     obj['fields'][field] = value.strip('"')
                    if value.startswith('\"') or value.endswith('\"'):
                        value = value.strip('\"')
                        obj['fields'][field] = value
                    if value.startswith('\\'):
                        value = value.strip('\\')
                        obj['fields'][field] = value
            
            for obj in fixture_data:
                for field, value in obj['fields'].items():
                    if isinstance(value, str) and value == 'N':
                        obj['fields'][field] = None
                    if isinstance(value, str) and value == '\\N':
                        obj['fields'][field] = None
                    if isinstance(value, str) and value == '\\\\N':
                        obj['fields'][field] = None
                    if isinstance(value, str) and value == '':
                        obj['fields'][field] = None

            f.seek(0)
            f.truncate()
            json.dump(fixture_data, f, indent=4, ensure_ascii=False)