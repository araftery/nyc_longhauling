from django.db import models


class Trip(models.Model):
    pickup_time = models.DateTimeField()
    dropoff_time = models.DateTimeField()
    passenger_count = models.IntegerField()
    distance = models.FloatField()
    pickup_longitude = models.FloatField()
    pickup_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    fare_amount = models.FloatField()
    extra = models.FloatField()
    mta_tax = models.FloatField()
    tip_amount = models.FloatField()
    tolls_amount = models.FloatField()
    pickup_lat_coord = models.IntegerField()
    pickup_lng_coord = models.IntegerField()
    dropoff_lat_coord = models.IntegerField()
    dropoff_lng_coord = models.IntegerField()
    pickup_day_hour = models.CharField(max_length=100)

    def __unicode__(self):
        return u'Trip from ({}, {}) to ({}, {}) on {}.'.format(
            self.pickup_lat_coord,
            self.pickup_lng_coord,
            self.dropoff_lat_coord,
            self.dropoff_lng_coord,
            self.pickup_time.strftime('%m/%D/%Y %I:%M %p'),
        )
