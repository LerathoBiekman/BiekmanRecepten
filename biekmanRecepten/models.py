from django.db import models

# Create your models here.


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    dish = models.CharField(max_length=20)
    season = models.CharField(max_length=20)
    prep_time = models.IntegerField()
    people = models.IntegerField()
    description = models.TextField(default=None)

    class Meta:
        db_table = 'Recipe'

    def __str__(self):
        return "%s / %s / %s / %s / %s" % (self.title, self.dish, self.season, self.prep_time, self.people)
