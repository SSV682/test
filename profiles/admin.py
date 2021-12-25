from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('date','subject','content')
