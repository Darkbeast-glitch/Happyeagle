from django.shortcuts import render,redirect,HttpResponseRedirect
from HetmApp.models import MainPackageView,TourPackages, HomePackages
from django.conf import settings
import os
from pyairtable import Api
from django.http import JsonResponse

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
            'Last Name': last_name ,
            'First Name': first_name,
            'Nationality': nationality,
            'Additional Requests': additional_request,
            'Age': 20,
            'Phone number': phone_number,
            'Reservation Date': reservation_date,
            'Tour Packages': tour_packages,
            'Email address': email,
            # 'Tour Packages': tour_packages
        })
        
        # new_record.save()
        
        

        # Redirect to a thank you page or any other desired page
        return redirect('contact')  # Replace 'thank_you' with the URL name of your thank you page
    
    
    context = {
        'tour_packs':tour_packs,
        
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








# 'Tour Packages': ['recn4CVOQBfBbzZFw'], 'Email address': 'kwasiampong32@gmail.com'}}, {'id': 'recpSAbGgosln5e6r', 'createdTime': '2023-09-20T11:14:37.000Z', 'fields': {'Last Name': 'Hegarty', 'First Name': 'Henry', 'Nationality': 'USA', 'Additional Requests': 'hELLO', 'Age': 89, 'Phone number': '07793227038', 'Reservation Date': '2023-09-20', 'Email address': 'bbjulius900@gmail.com'}}, {'id': 'recq5DtqciT1TcYDo', 'createdTime': '2023-09-15T14:46:38.000Z', 'fields': {'Last Name': 'Boakye', 'First Name': 'Julius', 'Nationality': 'American', 'Additional Requests': 'njn', 'Age': 25, 'Phone number': '0500159892', 'Reservation Date': '2023-09-21', 'Tour Packages': ['recvSAFRGre17IyPo'], 'Email address': 'bbjulius900@gmail.com'}}, {'id': 'recrmxMuZDtd6Oy9b', 'createdTime': '2023-09-15T14:47:41.000Z', 'fields': {'Last Name': 'Boakye', 'First Name': 'Julius', 'Nationality': 'Ghanaian', 'Additional Requests': 'jhjkh', 'Age': 25, 'Phone number': '0500159892', 'Reservation Date': '2023-09-14', 'Tour Packages': ['rec8oYIA5Gk3AKh3K'], 'Email address': 'bbjulius900@gmail.com'}}, {'id': 'recro5epjAFX2dqt8', 'createdTime': '2023-09-20T16:19:53.000Z', 'fields': {'First Name': 'Julius', 'Age': 89, 'Nationality': 'Canada', 'Reservation Date': '2023-09-20', 'Email address': 'bbjulius900@gmail.com', 'Phone number': '07793227038', 'Additional Requests': 'Chalie this is a new one ', 'Last Name': 'NANA'}}, {'id': 'recwbrDKp9qbp5lfr', 'createdTime': '2023-09-20T16:22:17.000Z', 'fields': {'First Name': 'Julius', 'Age': 20, 'Nationality': 'Ghanaian', 'Reservation Date': '2023-09-29', 'Email address': 'bbjulius900@gmail.com', 'Additional Requests': 'hello', 'Last Name': 'Boakye'}}, {'id': 'recy4nQQPkOU4MMNB', 'createdTime': '2023-09-13T16:32:01.000Z', 'fields': {'Last Name': 'Agbogblojo', 'First Name': 'Kofi ', 'Nationality': 'Ghanaian', 'Additional Requests': 'None', 'Age': 46, 'Phone number': '(054) 476-7509', 'Reservation Date': '2023-09-28', 'Tour Packages': ['rec9Nc3zFkTVY9yAT'], 'Email address': 'kofiagbo1@gmail.com'}}]