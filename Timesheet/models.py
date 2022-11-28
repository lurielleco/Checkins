from django.db import models

# Create your models here.
class Checkin(models.Model):
    user = models.CharField(max_length=45, default='admin')
    date_checkin = models.DateField()
    hours = models.FloatField()
    project = models.CharField(max_length=45, default='admin')

    def __str__(self):
        return self.user + str(self.date_checkin)