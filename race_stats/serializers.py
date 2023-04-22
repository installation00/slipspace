from rest_framework import serializers
from .models import races, drivers, constructors, circuits, seasons, status, constructor_standings, constructor_results, driver_standings, sprint_results, qualifying, pit_stops, lap_times, results

class RacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = races
        fields = '__all__'


class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = drivers
        fields = '__all__'


class ConstructorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = constructors
        fields = '__all__'


class CircuitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = circuits
        fields = '__all__'


class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = seasons
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = status
        fields = '__all__'


class ConstructorStandingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = constructor_standings
        fields = '__all__'


class ConstructorResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = constructor_results
        fields = '__all__'


class DriverStandingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = driver_standings
        fields = '__all__'

class SprintResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sprint_results
        fields = '__all__'

class QualifyingSerializer(serializers.ModelSerializer):
    class Meta:
        model = qualifying
        fields = '__all__'

class PitStopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = pit_stops
        fields = '__all__'

class LapTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = lap_times
        fields = '__all__'

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = results
        fields = '__all__'