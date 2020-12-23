from django.db import models



class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Transaction(models.Model):

    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE, blank=True)
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=200, blank=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
