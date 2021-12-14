from django.db import models
class pred(models.Model):
    date = models.CharField(max_length=100, primary_key=True)
    province = models.TextField()
    city = models.TextField()
    group = models.BooleanField()
    infection_case = models.TextField()
    confirmed = models.TextField()

    class Meta:
        db_table = "cases"
    def __str__(self):
        return f'[{self.pk}]{self.case_id}'
class Policy(models.Model):
    policy_id = models.CharField(max_length=100, primary_key=True)
    country = models.TextField()
    type = models.TextField()
    gov_policy = models.TextField()
    detail = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = "policy"

    def __str__(self):
        return f'[{self.pk}]{self.policy_id}'