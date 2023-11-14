from django.test import TestCase
from .models import TourPackages, HomePackages
from django.utils import timezone
# Create your tests here.



class TourTestCase(TestCase):
    def testBooking(self):
        packages = TourPackages( tour_place="Kumasi", tour_price="300", payment_id="DK3VEASW")
        self.assertEqual(packages.tour_place, "Kumasi")
        self.assertEqual(packages.tour_price, "300")
        self.assertEqual(packages.payment_id, "DK3VEASW")
        
        
        
class HomePackageTestCase(TestCase):
    def testHomePagePackage(slef, package_name="Shi Hills", package_place="Volta Region", package_days="30", package_price="450", packages_include_1="Free food", theDate=timezone.now(), date_added=timezone.now()):
        return HomePackages.objects.create(package_name=package_name, package_place=package_place , package_days=package_days, package_price=package_price, packages_include_1=packages_include_1, theDate=theDate, date_added=date_added)
    
    def test_homoage_creation(self):
        w = self.testHomePagePackage()
        self.assertTrue(isinstance(w, HomePackages))
        self.assertEqual(w.__str__(), w.package_name)
        