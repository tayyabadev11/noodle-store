from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Noodle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='noodles/')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name
