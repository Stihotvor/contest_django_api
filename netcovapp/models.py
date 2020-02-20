from django.db import models


class Operator(models.Model):
    name = models.CharField(max_length=24)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=128)


class Coverage(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    net_2g = models.BooleanField(default=False)
    net_3g = models.BooleanField(default=False)
    net_4g = models.BooleanField(default=False)

