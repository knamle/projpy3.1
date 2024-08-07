from django.db import models
from django.contrib.auth.models import User



# Once you’ve defined your model, you need to create the corresponding database table. 
# python manage.py makemigrations 
# python manage.py migrate


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title


class Product(models.Model):
    VEGETABLES = 'Vegetable'
    MEAT = 'Meat'
    DAIRY = 'Dairy'
    OTHER = 'Otherr'

    CATEGORY_CHOICES = [
        (VEGETABLES, 'Vegetable'),
        (MEAT, 'Meat'),
        (DAIRY, 'Dairy'),
        (OTHER, 'Otherr'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=OTHER,
    )
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
