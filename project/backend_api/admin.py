from django.contrib import admin
from .models import (Customers,InsurancePolicy)
# Register your models here.
admin.site.register(Customers)
admin.site.register(InsurancePolicy)
