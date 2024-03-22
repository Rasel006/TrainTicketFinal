from django.db import models
from account.models import UserAccount
# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places = 2)