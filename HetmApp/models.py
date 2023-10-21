from django.db import models
from currencies.models import Currency

# Create your models here.






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
    package_short_description = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-date_added']
        verbose_name = 'HomePackage'
        verbose_name_plural = 'HomePackages'
    
    
    def __str__(self):
        return self.package_name
    
  
        
        



    

# CategoryModel
class PackageCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    

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
    category = models.ForeignKey(PackageCategory, on_delete=models.CASCADE, null=True, blank=True)
    
    
    theDate = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True) 
    
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, null=True, blank=True)
    package_short_description = models.TextField(blank=True, null=True)
    
    
    class Meta:
        ordering = ['-date_added']
        verbose_name = 'MainPackage'
        verbose_name_plural = 'MainPackages'
        
   
    
    def __str__(self):
        return self.package_name
    
   

        
class Bookings(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=2, blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    reserveation_date =  models.DateField( auto_now_add=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    tour_package = models.CharField(max_length=200, blank=True, null=True)
    additional_request  = models.TextField()


    
    class Meta:
        verbose_name = 'Bookings'
        verbose_name_plural = 'Booking'
        
   
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
    
    
    
class Gallery(models.Model):
        image = models.ImageField(upload_to="images/gallaries")
        
        class Meta:
            verbose_name = 'Gallery'
            verbose_name_plural = 'Galleries'
            
   
    
        def __str__(self):
            return f"{self.image}"



class TourPackages(models.Model):
    # tour_packages = models.CharField(max_length=200, blank=True, null=True)    
    tour_package = models.ForeignKey(
        MainPackageView, on_delete=models.CASCADE, null=True, blank=True)
    tour_place = models.CharField(max_length=200, blank=True, null=True)   
    tour_price = models.CharField(max_length=200,blank=True, null=True) 
    payment_id = models.CharField(max_length=100, unique=True)

   
    
    def __str__(self):
               return self.tour_package.package_name  # Assuming 'name' is a field in MainPackageView model

    
    class Meta:
        verbose_name = 'tour_package'
        verbose_name_plural = 'tour_packages'
    
    