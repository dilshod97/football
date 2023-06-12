from django.db import models
import uuid, os
from account.models import User


def get_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('arena', filename)


class Arena(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    mode_start = models.TimeField()
    mode_end = models.TimeField()
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    status = models.BooleanField(default=True)
    price_hour = models.FloatField()
    min_pre_hour = models.FloatField(null=True, default=0)
    fine_refuse_price = models.FloatField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    arena = models.ForeignKey(Arena, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image, default='arena/default.png')
