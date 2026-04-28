from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    threshold=models.IntegerField(default=5)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name