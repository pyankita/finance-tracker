from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True)
    type = models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10,blank=True,null=True)
    category = models.CharField(max_length=50,blank=True,null=True)
    date = models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
