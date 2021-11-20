from django.db import models



class Crwaling_Live(models.Model):
    death = models.TextField()
    serious = models.TextField()
    new_hospitalization = models.TextField()
    confirmed = models.TextField()


    def __str__(self):
        return f'{self.confirmed}'
    class Meta:
        db_table = 'covid'



