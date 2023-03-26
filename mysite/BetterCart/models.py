import csv
from django.db import models

# Create your models here.
from django.db import models


class GroceryItem(models.Model):
    item_name = models.CharField(max_length=255)
    calories = models.IntegerField(null=True, blank=True)
    saturated_fat = models.FloatField(null=True, blank=True)
    unsaturated_fat = models.FloatField(null=True, blank=True)
    trans_fat = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.item_name


class nutritionFacts(models.Model):
    item_name = models.CharField(max_length=255)
    serving_size = models.CharField(max_length=20)
    calories = models.IntegerField(max_length=20)
    total_fat = models.CharField(max_length=20)
    carbs = models.CharField(max_length=20)
    protein = models.CharField(max_length=20)

    def __str__(self):
        return self.item_name


def load_data_from_csv():
    with open('nutrition.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nutrition = nutritionFacts(
                item_name=row['name'],
                serving_size=row['serving_size'],
                calories=row['calories'],
                total_fat=row['total_fat'],
                carbs=row['carbohydrate'],
                protein=row['protein']
            )
            nutrition.save()
