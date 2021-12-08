from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Snack (models.Model) :
    purchaser = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    name = models.CharField(max_length = 64)
    description = models.TextField()

    def __str__(self) :
        return self.name

# Way 2
    def get_absolute_url(self) :
        return reverse('snack_detail', args=[self.id])