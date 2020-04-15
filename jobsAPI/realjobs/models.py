from django.db import models

# Create your models here.


class JobOffer(models.Model):
    company_name = models.CharField(max_length=60)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=60)
    job_description = models.CharField(null=True,max_length=120)
    salary = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
