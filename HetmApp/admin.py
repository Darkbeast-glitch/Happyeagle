from django.contrib import admin
from HetmApp.models import TourPackages,MainPackageView,HomePackages,PackageCategory,Gallery



# Register your models here.




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


class TourPackagesAdmin(admin.ModelAdmin):
    list_display = ('tour_package', 'tour_place', 'tour_price', 'payment_id')
    
    def save_model(self, request, obj, form, change):
        # Automatically set tour_price based on MainPackageView when creating/editing TourPackages
        if obj.tour_package and not obj.tour_price:
            obj.tour_price = obj.tour_package.tour_price
        super().save_model(request, obj, form, change)

admin.site.register(TourPackages, TourPackagesAdmin)