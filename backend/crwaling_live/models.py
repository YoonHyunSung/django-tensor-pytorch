from django.db import models



class Crwaling_Live(models.Model):
    death = models.CharField()
    serious = models.CharField()
    new_hospitalization = models.CharField()
    confirmed = models.CharField()





    def __str__(self):
        return f'{self.confirmed}'
    class Meta:
        db_table = 'covid'



