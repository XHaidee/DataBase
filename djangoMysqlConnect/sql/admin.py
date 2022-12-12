from django.contrib import admin
from sql.models import Haideep

# Register your models here.
@admin.register(Haideep)
class sql(admin.ModelAdmin):
  list_display = ('id', 'name')
