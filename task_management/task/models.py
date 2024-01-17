
##### all the imports here
from django.db import models
from category.models import Category

##### Create your models here.

# add task model
class AddTask(models.Model):
    title = models.CharField(max_length = 300)
    description = models.TextField()
    category = models.ManyToManyField(Category)

    # see the title
    def __str__(self):
        return self.title