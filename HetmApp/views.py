from django.shortcuts import render,redirect,HttpResponseRedirect
from HetmApp.models import MainPackageView,TourPackages, HomePackages
from django.conf import settings

# Create your views here.


def HomepageView(request):
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY
          
    
    packages = HomePackages.objects.all().order_by('-date_added')
    # tour_packs = MainPackageView.objects.all()
    
    context = {
        
        'packages': packages,
        # 'tour_packs':tour_packs
    }
    
    return render(request, 'index.html', context)



def BookingView(request):
    tour_packs = TourPackages.objects.all()
    
    context = {
        'tour_packs':tour_packs
        
    }

    
    
    return render(request, 'booking.html', context)




def PackageView(request):
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY
    package = MainPackageView.objects.all()
    
    context = {
        
        'package': package
    }
    
    return render(request, 'package.html', context)


def AboutView(request):
    context = {}
    
    return render(request, 'about.html', context)




def ContactView(request):
    
    context = {}
    
    return render(request, 'contact.html', context)




# SELECT CURRENCY VIEW

def SelectCurrency(request):
    lasturl = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        request.session['currency'] = request.POST['currency']
        return HttpResponseRedirect(lasturl)

    return HttpResponseRedirect(lasturl)