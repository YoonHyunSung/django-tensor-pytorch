from django.db import models



class Crwaling_Live(models.Model):
    sortation = models.AutoField()
    death = models.AutoField()
    serious = models.AutoField()
    new_hospitalization = models.AutoField()
    confirmed = models.AutoField()


    def __str__(self):
        return f'{self.confirmed}'
    class Meta:
        db_table = 'covid'



