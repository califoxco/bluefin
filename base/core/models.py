from django.shortcuts import reverse
from django.db import models
from django.utils.text import slugify


# ------------------------------------ Owner Model ------------------------------------
# Description: Stores Owner objects
# Parameter: model
# -------------------------------------------------------------------------------------
class Owner(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(default=0)  # alternatively use string
    status = models.CharField(max_length=100, default="Active")

    # below is the option to link to user account, but for now lets not use a login system yet
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)

    # eg. jiaming yang
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ------------------------------------ Property Model ------------------------------------
# Description: Stores property objects
# Parameter: model
# ----------------------------------------------------------------------------------------
# these are set choices. Note that key and value are the same because keys serve no purpose
class Property(models.Model):
    PROPERTY_TYPE = (
        ("Single Family Home", "Single Family Home"),
        ("Condominium", "Condominium"),
        ("Apartment", "Apartment"),
        ("Town Home", "Town Home"),
        ("Duplex", "Duplex"),
        ("Loft", "Loft"),
    )

    TRANSACTION_TYPE = (
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Available", "Available"),
        ("Closed", "Closed"),
        ("Sold", "Sold"),
    )

    # slug is used for generating url
    slug = models.SlugField(default='', editable=False)
    # -----------------basic info----------------------
    listed_date = models.DateTimeField(auto_now_add=True)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE)
    square_feet = models.CharField(max_length=100)
    number_bedroom = models.IntegerField(default=0)
    number_baths = models.FloatField(default=0)
    description = models.CharField(max_length=500, default="Beautiful country home")
    transaction_state = models.CharField(max_length=100, choices=TRANSACTION_TYPE)
    price = models.FloatField()
    item_picture = models.ImageField(default='default.jfif', upload_to='homeImg')
    # -----------------database foreign key----------------------
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    # creating an unique slug for each property
    def save(self, *args, **kwargs):
        self.slug = slugify(self.address_1 + '-' + self.address_2 + '-' + self.zip)
        super().save(*args, **kwargs)

    # creating an url for detail view using slug
    def get_absolute_url(self):
        return reverse("core:home-detail", kwargs={
            'slug': self.slug
        })

    # eg.  1-1719 Eucalyptus Dr.
    def __str__(self):
        return str(self.id) + '-' + self.address_1
