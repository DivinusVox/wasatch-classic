from django.core.exceptions import ValidationError
from django.db import models


REGISTRATION_LIMIT = 2


class Show(models.Model):
    number = models.IntegerField()

    def __unicode__(self):
        return u"Watatch Classic {}".format(self.number)


class Registration(models.Model):
    show = models.ForeignKey(Show)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=15)

    def __unicode__(self):
        return u"{} {} <{}>".format(self.first_name,
                                                 self.last_name,
                                                 self.email)


class Car(models.Model):
    registrant = models.ForeignKey(Registration)
    make = models.CharField(max_length=100)
    year = models.CharField(max_length=20)

    def __unicode__(self):
        return u"{} {}".format(self.year, self.make)

    def save(self, *args, **kwargs):
        if self.registrant.car_set.count() >= REGISTRATION_LIMIT:
            raise ValidationError("Unable to register more than {} cars.".format(REGISTRATION_LIMIT))
        super(Car, self).save(*args, **kwargs)
