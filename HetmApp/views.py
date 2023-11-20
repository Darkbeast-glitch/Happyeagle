from django.shortcuts import render, redirect, HttpResponseRedirect
from HetmApp.models import MainPackageView, TourPackages, HomePackages, Bookings, PackageCategory, Gallery
from django.conf import settings
from django.contrib import messages #import messages
from django.contrib import messages #import messages

import os
from pyairtable import Api
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

# from django.http import JsonResponse

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


# newbooking view

# old BookignView
def BookingView(request):
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY

    tour_packs = TourPackages.objects.all()

    if request.method == 'POST':
        # Get form data from the POST request
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        age = request.POST.get('age')
        nationality = request.POST.get('nationality')
        reservation_date = request.POST.get('reservationdate')
        phone_number = request.POST.get('phonenumber')
        email = request.POST.get('email')
        tour_packages = request.POST.get('tourpackages')
        additional_request = request.POST.get('addtionalrequest')

        # Initialize the Airtable API using your API key
        api = Api(os.environ['AIRTABLE_API_KEY'])

        # Specify y our base ID and table ID
        base_id = 'appyuKokIsUjlynJ6'
        table_id = 'tbliu8b1bQWGMnRvB'

        # Access the table
        table = api.table(base_id, table_id)

        # Create a new record in the table with the form data
        new_record = table.create({
            'Last Name': last_name,
            'First Name': first_name,
            'Nationality': nationality,
            'Additional Requests': additional_request,
            'Age': age,
            'Phone number': phone_number,
            'Reservation Date': reservation_date,
            'Tour Packages': tour_packages,
            'Email address': email,
            # 'Tour Packages': tour_packages
        })
        
        
        # get the tour package name
        selected_package_name = request.POST.get('tourpackages')

        # Get the selected package object
        selected_package = TourPackages.objects.get(
            tour_place=selected_package_name)

        # Construct the payment URL with the package's payment ID
        payment_url = f"https://paystack.com/pay/{selected_package.payment_id}"

        # Redirect the user to the payment URL after a delay
        return render(request, 'success.html', {'payment_url': payment_url})
        # new_record.save()

        # # Redirect to a thank you page or any other desired page
        # return redirect('success')  # Replace 'thank_you' with the URL name of your thank you page

        
    context = {
        'tour_packs': tour_packs,

    }

    return render(request, 'booking.html', context)


# Contact us data


def ContactView(request):
    
    if request.method == 'POST':
        Name = request.POST.get('full_name')
        Email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Message = request.POST.get('message')
        
        
        
         # Initialize the Airtable API using your API key
        api = Api(os.environ['AIRTABLE_API_KEY'])

        # Specify y our base ID and table ID
        base_id = 'appyuKokIsUjlynJ6'
        table_id = 'tbl0LjyDuHeassFWy'

        # Access the table
        table = api.table(base_id, table_id)

        # Create a new record in the table with the form data
        new_record = table.create({
         'Name':Name,
         'Email': Email,
         'Subject': Subject,
         'Message':Message
         
        })
        messages.success(request, "Heyy!!!,😃 We have received your message, we shall revert soon" )

        
        
        
        


    context = {}

    return render(request, 'contact.html', context)



# package view


def PackageView(request):
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY

    # Get the selected category ID from the URL parameters
    category_id = request.GET.get('category')

    # Fetch all packages if no category is selected
    if category_id:
        # Filter packages based on the selected category
        packages = MainPackageView.objects.filter(category__id=category_id)
    else:
        # If no category is selected, display all packages
        packages = MainPackageView.objects.all()

    # Fetch all categories to populate the filter dropdown
    categories = PackageCategory.objects.all()

    context = {
        'packages': packages,
        'categories': categories,
    }

    return render(request, 'package.html', context)


# def PackageView(request):
#     if not request.session.has_key('currency'):
#         request.session['currency'] = settings.DEFAULT_CURRENCY

#     packages = MainPackageView.objects.all()
#     categories = PackageCategory.objects.all()  # Fetch all categories from the database

#     context = {
#         'packages': packages,
#         'categories': categories,  # Include categories in the context
#     }

#     return render(request, 'package.html', context)


def AboutView(request):
    context = {}

    return render(request, 'about.html', context)


# SELECT CURRENCY VIEW

def SelectCurrency(request):
    lasturl = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        request.session['currency'] = request.POST['currency']
        return HttpResponseRedirect(lasturl)

    return HttpResponseRedirect(lasturl)


def SuccessPage(request):
    # Fetch the first booking as an example
    booking_data = Bookings.objects.first()
    context = {
        'booking_data': booking_data
    }
    return render(request, 'success.html', context)






def GalleryPage(request):
    gallery_tile = Gallery.objects.all()
    # default to first page
    default_page = 1
    page = request.GET.get('page', default_page)
    
    # Paginate items
    items_per_page = 10
    paginator = Paginator(gallery_tile, items_per_page)
    
    
    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    context = {

        'gallery_tile': gallery_tile,
        "items_page":items_page,
    }
    

    return render(request, 'gallery.html', context)
