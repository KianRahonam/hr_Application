from django.db import models

# Create your models here.
class OfferLettercontract(models.Model):
    objects = None
    candidateid = models.IntegerField(primary_key=True,auto_created=True)
    offredcompany = models.CharField(max_length=50, null=True)
    employmenttype = models.CharField(max_length=50,null=True)
    offerdate = models.DateField(auto_now=True, null=True)
    candidatename = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=300, null=True)
    designation = models.CharField(max_length=50, null=True)
    reporting = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    projectname = models.CharField(max_length=100, null=True)
    joining = models.CharField(max_length=10, null=True)
    contractend = models.CharField(max_length=10, null=True)
    salary = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=10, null=True)
    emialid = models.CharField(max_length=50, null=True)
