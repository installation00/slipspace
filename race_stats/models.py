from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class races(models.Model):
    raceId = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    round = models.IntegerField(null=True, blank=True)
    circuitId = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=25, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add= False, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    fp1_date = models.DateField(null=True, blank=True)
    fp1_time = models.TimeField(auto_now=False, auto_now_add= False, null=True, blank=True)
    fp2_date = models.DateField(null=True, blank=True)
    fp2_time = models.TimeField(auto_now=False, auto_now_add= False, null=True, blank=True)
    fp3_date = models.DateField(null=True, blank=True)
    fp3_time = models.TimeField(auto_now=False, auto_now_add= False, null=True, blank=True)
    quali_date = models.DateField(null=True, blank=True)
    quali_time = models.TimeField(auto_now=False, auto_now_add= False, null=True, blank=True)
    sprint_date = models.DateField(null=True, blank=True)
    sprint_time = models.TimeField(auto_now=False, auto_now_add= False, null=True, blank=True)

class drivers(models.Model):
    driverId = models.IntegerField(null=True, blank=True)
    driverRef = models.CharField(max_length=25, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=5, null=True, blank=True)
    forename = models.CharField(max_length=20, null=True, blank=True)
    surname = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=25, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)

class constructors(models.Model):
    constructorId = models.IntegerField(null=True, blank=True)
    constructorRef = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    nationality = models.CharField(max_length=25, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)

class circuits(models.Model):
    circuitId = models.IntegerField(null=True, blank=True)
    circuitRef = models.CharField(max_length=25, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=25, null=True, blank=True)
    lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)], null=True, blank=True)
    lng = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)], null=True, blank=True)
    alt = models.IntegerField(null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)

class seasons(models.Model):
    year = models.IntegerField(null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)

class status(models.Model):
    statusId = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=25, null=True, blank=True)

class constructor_standings(models.Model):
    constructorStandingsId = models.IntegerField(null=True, blank=True)
    raceId = models.IntegerField(null=True, blank=True)
    constructorId = models.IntegerField(null=True, blank=True)
    points = models.FloatField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    positionText = models.CharField(max_length=10, null=True, blank=True)
    wins = models.IntegerField(null=True, blank=True)

class constructor_results(models.Model):
    constructorResultsId = models.IntegerField(null=True, blank=True)
    raceId = models.IntegerField(null=True, blank=True)
    constructorId = models.IntegerField(null=True, blank=True)
    points = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)

class driver_standings(models.Model):
    driverStandingsId = models.IntegerField(null=True, blank=True)
    raceId = models.IntegerField(null=True, blank=True)
    driverId = models.IntegerField(null=True, blank=True)
    points = models.FloatField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    positionText = models.CharField(max_length=10, null=True, blank=True)
    wins = models.IntegerField(null=True, blank=True)

class sprint_results(models.Model):
    resultId = models.IntegerField(null=True, blank=True)
    raceId = models.IntegerField(null=True, blank=True)
    driverId = models.IntegerField(null=True, blank=True)
    constructorId = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    grid = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    positionText = models.CharField(max_length=10, null=True, blank=True)
    positionOrder = models.IntegerField(null=True, blank=True)
    points = models.FloatField(null=True, blank=True)
    laps = models.IntegerField(null=True, blank=True)
    time = models.CharField(max_length=15, null=True, blank=True)
    milliseconds = models.IntegerField(null=True, blank=True)
    fastestLap = models.IntegerField(null=True, blank=True)
    fastestLapTime = models.DurationField(null=True, blank=True)
    statusId = models.IntegerField(null=True, blank=True)

class qualifying(models.Model):
    qualifyId = models.IntegerField(null=True, blank=True)
    raceId = models.IntegerField(null=True, blank=True)
    driverId = models.IntegerField(null=True, blank=True)
    constructorId = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    q1 = models.DurationField(null=True, blank=True)
    q2 = models.DurationField(null=True, blank=True)
    q3 = models.DurationField(null=True, blank=True)

class pit_stops(models.Model):
    raceId = models.IntegerField(null=True, blank=True)
    driverId = models.IntegerField(null=True, blank=True)
    stop = models.IntegerField(null=True, blank=True)
    lap = models.IntegerField(null=True, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add= False, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    milliseconds = models.IntegerField(null=True, blank=True)

class lap_times(models.Model):
    raceId = models.IntegerField(null=True, blank=True)
    driverId = models.IntegerField(null=True, blank=True)
    lap = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    time = models.DurationField(null=True, blank=True)
    milliseconds = models.IntegerField(null=True, blank=True)

class results(models.Model):
    resultId = models.IntegerField(null=True, blank=True)
    raceId = models.IntegerField(null=True, blank=True)
    driverId = models.IntegerField(null=True, blank=True)
    constructorId = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    grid = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    positionText = models.CharField(max_length=10, null=True, blank=True)
    positionOrder = models.IntegerField(null=True, blank=True)
    points = models.FloatField(null=True, blank=True)
    laps = models.IntegerField(null=True, blank=True)
    time = models.CharField(max_length=15, null=True, blank=True)
    milliseconds = models.IntegerField(null=True, blank=True)
    fastestLap = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    fastestLapTime = models.DurationField(null=True, blank=True)
    fastestLapSpeed = models.FloatField(null=True, blank=True)
    statusId = models.IntegerField(null=True, blank=True)