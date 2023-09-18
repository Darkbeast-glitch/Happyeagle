from django.db import models
from currencies.models import Currency

# Create your models here.




class TourPackages(models.Model):
    tour_packages = models.CharField(max_length=200, blank=True, null=True)    
    tour_place = models.CharField(max_length=200, blank=True, null=True)   
    
    def __str__(self):
        return self.tour_packages
    
    class Meta:
        verbose_name = 'tour_package'
        verbose_name_plural = 'tour_packages'
    
    

class HomePackages(models.Model):
    image = models.ImageField(upload_to="images/")
    package_name = models.CharField(max_length=100, null=True, blank=True)
    package_place = models.CharField(max_length=100, null=True, blank=True)
    package_days = models.IntegerField(null=True, blank=True)
    package_price = models.IntegerField()
    # packages_includs = models.ForeignKey(TourPackages, on_delete=models.CASCADE, blank=True, null=True)
    packages_include_1= models.CharField(max_length=100, null=True, blank=True)
    packages_include_2= models.CharField(max_length=100, null=True, blank=True)
    packages_include_3= models.CharField(max_length=100, null=True, blank=True)
    packages_include_4= models.CharField(max_length=100, null=True, blank=True)
    packages_include_5= models.CharField(max_length=100, null=True, blank=True)
    
    theDate = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True) 
    
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, null=True, blank=True)
    package_short_description = models.TextField()
    
    class Meta:
        ordering = ['-date_added']
        verbose_name = 'HomePackage'
        verbose_name_plural = 'HomePackages'
    
    
    def __str__(self):
        return self.package_name
    
  
        
        



    
    
    
    

class MainPackageView(models.Model):
    image = models.ImageField(upload_to="images/")
    package_name = models.CharField(max_length=100, null=True, blank=True)
    package_place = models.CharField(max_length=100, null=True, blank=True)
    package_days = models.IntegerField(null=True, blank=True)
    package_price = models.IntegerField()
    # packages_includs = models.ForeignKey(TourPackages, on_delete=models.CASCADE, blank=True, null=True)
    packages_include_1= models.CharField(max_length=100, null=True, blank=True)
    packages_include_2= models.CharField(max_length=100, null=True, blank=True)
    packages_include_3= models.CharField(max_length=100, null=True, blank=True)
    packages_include_4= models.CharField(max_length=100, null=True, blank=True)
    packages_include_5= models.CharField(max_length=100, null=True, blank=True)
    
    theDate = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True) 
    
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, null=True, blank=True)
    package_short_description = models.TextField()
    
    class Meta:
        ordering = ['-date_added']
        verbose_name = 'MainPackage'
        verbose_name_plural = 'MainPackages'
        
   
    
    def __str__(self):
        return self.package_name
    
    
        