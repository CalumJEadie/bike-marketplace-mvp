from django.db import models


class Seller(models.Model):

    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)
    facebook = models.URLField(blank=True)
    phone = models.CharField(max_length=11, blank=True)

    def __unicode__(self):
        return self.full_name

class Bike(models.Model):

    seller = models.ForeignKey(Seller)

    name = models.CharField(max_length=100)
    # types from bikesoup.co.uk
    # BMX
    # Cruiser / Beach
    # Cyclocross / CX
    # Delivery / Cargo
    # Dutch / Classic
    # E-bike / Electric
    # Folding
    # Hybrid / City
    # Jump
    # Kids / Childrens
    # MTB - Downhill
    # MTB - Full suspension
    # MTB - Hardtail
    # Recumbent
    # Road / Racing
    # Singlespeed / Fixie
    # Tandem
    # Touring / Trekking
    # Trials
    # Triathlon / Time Trial
    # Unicycle
    type = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    # cm
    frame_size = models.PositiveSmallIntegerField(blank=True)
    # materials from bikesoup.co.uk
    # Any
    # Aluminium
    # Carbon
    # Steel
    # Titanium
    # Other
    frame_material = models.CharField(max_length=50, blank=True)
    # disc brakes
    # rim brakes
    # other
    brakes = models.CharField(max_length=50, blank=True)
    model_year = models.PositiveSmallIntegerField(blank=True)
    mileage = models.PositiveSmallIntegerField(blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name