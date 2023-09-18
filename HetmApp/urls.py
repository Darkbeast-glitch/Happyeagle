from django.urls import path,include
from HetmApp.views import HomepageView, BookingView,PackageView,AboutView,ContactView,SelectCurrency
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomepageView, name="home" ),
    path('booking/', BookingView, name="booking" ),
    path('packages/', PackageView, name="packages" ),
    path('aboutus/', AboutView, name="about" ),
    path('contact/', ContactView, name="contact" ),
    path('selectcurrency/', SelectCurrency, name='selectcurrency'),
    

]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


