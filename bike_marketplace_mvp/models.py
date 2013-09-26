from string import Template

from django.db import models
from django.db.models.signals import post_save

from account.models import Account

class Seller(models.Model):
    """
    Following design pattern from http://gistflow.com/posts/725-how-to-extend-the-behaviour-of-the-user-class-in-django-1-5.
    """

    account = models.OneToOneField(Account, unique=True)

    has_facebook = models.BooleanField(default=True)
    facebook_friends = models.PositiveSmallIntegerField(blank=True, default=347)
    has_linkedin = models.BooleanField(default=True)
    linkedin_connections = models.PositiveSmallIntegerField(blank=True, default=184)
    has_road = models.BooleanField(default=True)
    has_single_track = models.BooleanField(default=True)

    @classmethod
    def _create(cls, sender, instance, created, **kwargs):
        if created:
            profile, created = cls.objects.get_or_create(account=instance)

    def __unicode__(self):
        return unicode(self.account)

post_save.connect(Seller._create, sender=Account)

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
    verified_not_stolen = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    BIKEPEDIA_TEMPLATE_URL = Template("http://www.bikepedia.com/quickbike/BikeSpecs.aspx?Year=$year&Brand=$brand&Model=$model&Type=bike")

    @property
    def bikepedia_url(self):

        return self.BIKEPEDIA_TEMPLATE_URL.substitute({
            "brand": self.brand,
            "model": self.model,
            "year": self.model_year
        })