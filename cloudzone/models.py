#from django.db import models
#from django.contrib.gis.db import models
from django.contrib.gis.db import models


class Cloud(models.Model):
    name = models.CharField(max_length=70)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NonSmokingArea(models.Model):
    id = id = models.AutoField(primary_key=True)
    area_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    area_detail = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    sigungu = models.CharField(max_length=50)
    eupmyundong = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
    area_size = models.FloatField()
    fine = models.CharField(max_length=50)
    address_doromyung = models.CharField(max_length=50)
    address_jibeon = models.CharField(max_length=50)
    manage_office = models.CharField(max_length=50)
    latitude = models.DecimalField(default=0, max_digits=12, decimal_places=8)
    longitude = models.DecimalField(default=0, max_digits=12, decimal_places=8)
    image = models.CharField(max_length=50)
    radius = models.FloatField()

    def __str__(self):
        return self.name


class SmokingArea(models.Model):
    id = id = models.AutoField(primary_key=True)
    area_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    area_detail = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    sigungu = models.CharField(max_length=50)
    eupmyundong = models.CharField(max_length=50)
    area_size = models.FloatField()
    address_doromyung = models.CharField(max_length=50)
    address_jibeon = models.CharField(max_length=50)
    manage_office = models.CharField(max_length=50)
    latitude = models.DecimalField(default=0, max_digits=12, decimal_places=8)
    longitude = models.DecimalField(default=0, max_digits=12, decimal_places=8)
    image = models.CharField(max_length=50)
    radius = models.FloatField()

    def __str__(self):
        return self.name

class Manner(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.GeometryField()  # This field type is a guess.
    fid = models.FloatField(blank=True, null=True)
    dn = models.IntegerField(db_column='DN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cloudzone_mannerrr'






