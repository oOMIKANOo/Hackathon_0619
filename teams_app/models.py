from django.db import models

class Lang(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tech(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teams(models.Model):
    name = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    langs = models.ManyToManyField(Lang,blank=True)
    techs = models.ManyToManyField(Tech,blank=True)

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__ 