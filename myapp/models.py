from django.db import models

# Create your models here.
class Feature(models.Model):
    ## models.Model converts this basic class into model.
    ## Whenever we create a model, we do not have to id againg, as each attribute/object will have an id created
    #id: int
    #name: str
    #details: str
    #is_rich: bool

    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)
