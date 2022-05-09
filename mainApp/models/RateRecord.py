from django.db import models


class RateRecord(models.Model):
    appoint_id = models.IntegerField()
    doctor_id = models.IntegerField()
    rate = models.IntegerField()