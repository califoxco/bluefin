import uuid
from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Owner(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(default=0)
    status = models.CharField(max_length=100, default="Active")

    # below is the option to link to user account, but for now lets not use a login system yet
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}, name: {self.first_name} {self.last_name}"


class Property(models.Model):
    # slug is used for generating url
    slug = models.SlugField(default='0')
    # -----------------basic info----------------------
    listed_date = models.DateTimeField(auto_now_add=True)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)
    square_feet = models.CharField(max_length=100)
    number_bedroom = models.IntegerField(default=0)
    number_baths = models.FloatField(default=0)
    description = models.CharField(max_length=500, default="Beautiful country home")
    transaction_state = models.CharField(max_length=100)
    price = models.FloatField()
    item_picture = models.ImageField(default='default.jfif', upload_to='homeImg')
    # -----------------database foreign key----------------------
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.address_1 + '-' + self.address_2 + '-' + self.zip)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
