from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(OfferLettercontract)
class offerlettercontract(admin.ModelAdmin):
    list_display = ['candidateid','candidatename','offredcompany','employmenttype','offerdate'
                    ,'address','designation','location','projectname','reporting','joining',
                    'contractend','salary','phone','emialid']
    list_editable = ['employmenttype','address','designation','location','projectname','reporting','joining',
                    'contractend','salary','phone','emialid',]