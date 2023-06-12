from django.db import models
from account.models import User
from apps.arena.models import Arena


class Bron(models.Model):
    arena = models.ForeignKey(Arena, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.BooleanField(null=True)
    pre_pay = models.FloatField(default=0)
    pay = models.FloatField(default=0)
    back_pay = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.arena} ---- {self.user}"


class PaymentHistory(models.Model):
    bron = models.ForeignKey(Bron, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    min_pay = models.FloatField(default=0)
    full_pay = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
