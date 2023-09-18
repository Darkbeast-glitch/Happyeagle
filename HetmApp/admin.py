from django.contrib import admin
from HetmApp.models import TourPackages,MainPackageView,HomePackages



# Register your models here.



admin.site.register(TourPackages)
admin.site.register(HomePackages)
admin.site.register(MainPackageView)