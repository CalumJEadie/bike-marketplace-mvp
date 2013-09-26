from django.db import models

from account.models import Account

class Bike(models.Model):

    account = models.ForeignKey(Account)

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
    type = models.CharField(max_length=50, blank=True, default="Road")
    brand = models.CharField(max_length=50, blank=True, default="Trek")
    model = models.CharField(max_length=50, blank=True, default="7100")
    # cm
    frame_size = models.PositiveSmallIntegerField(blank=True, default=58)
    # materials from bikesoup.co.uk
    # Any
    # Aluminium
    # Carbon
    # Steel
    # Titanium
    # Other
    frame_material = models.CharField(max_length=50, blank=True, default="Aluminium")
    # disc brakes
    # rim brakes
    # other
    brakes = models.CharField(max_length=50, blank=True, default="Rim Brakes")
    model_year = models.PositiveSmallIntegerField(blank=True, default=2009)
    mileage = models.PositiveSmallIntegerField(blank=True, default=4500)
    description = models.TextField(blank=True, default="""Road bike speed and upright comfort join together for aggressive fitness rides or long commutes. Available with lightweight TCT Carbon or hydroformed Alpha Black Aluminum frames, rigid performance forks and fast-rolling 700c wheels.
If you want a practical bike for daily use or develop your cycling fitness as an alternative to the gym the Trek 7100 2009 Women's Hybrid Bike is a great option. Upright position, reliable easy to use brakes and gears with a durable wheel set means you can ride comfortably and safely whatever your journey.
""")
    price = models.PositiveSmallIntegerField(blank=True, default=200)

    def __unicode__(self):
        return self.name