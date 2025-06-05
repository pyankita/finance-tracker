from django.db import models

class Transaction(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10)
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
