from django.contrib import admin
from HetmApp.models import TourPackages,MainPackageView,HomePackages,PackageCategory,Gallery



# Register your models here.



admin.site.register(TourPackages)
admin.site.register(HomePackages)
admin.site.register(Gallery)


# Register the MainPackageView model
@admin.register(MainPackageView)
class MainPackageViewAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'package_place', 'package_days', 'category', 'package_price', 'theDate', 'date_added')
    # Add more fields as needed for the list view in the admin interface



# Register the PackageCategory model
@admin.register(PackageCategory)
class PackageCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
# admin.site.register(MainPackageView)