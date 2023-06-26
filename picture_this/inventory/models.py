from django.db import models

# Create your models here.
class Shirt(models.Model):
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.color} {self.size} Shirt"

class Transaction(models.Model):
    SHIRT_ACTIONS = (
        ('IN', 'Inventory'),
        ('SA', 'Sale'),
    )

    shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    action = models.CharField(max_length=2, choices=SHIRT_ACTIONS)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_action_display()} - {self.shirt} - {self.quantity}"