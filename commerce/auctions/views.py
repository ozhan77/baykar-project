from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from datetime import datetime
from .models import User,Category,Listing,Logs,Rentlist
from .forms import ProductForm



def index(request):
    activeListing =Listing.objects.filter(isActive=True)
    allCategories = Category.objects.all()
    return render(request, "auctions/index.html",{
        "listings":activeListing,
        "categories":allCategories
    })

def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryFromForm)
        activeListing =Listing.objects.filter(isActive=True, category=category)
        allCategories = Category.objects.all()
        return render(request, "auctions/index.html",{
            "listings":activeListing,
            "categories":allCategories
        })

def listing(request,id):
    listingData = Listing.objects.get(pk=id)
    return render(request, "auctions/listing.html",{
        "listing":listingData
    })

def deleteListing(request,id):
    listingData = Listing.objects.get(pk=id)
    listingData.delete()
    return redirect('index')

def createListing(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request,"auctions/create.html",{
            "categories":allCategories
        })
    else:
        brand = request.POST["brand"]
        model = request.POST["model"]
        description = request.POST["description"]
        weight = request.POST["weight"]
        imageUrl = request.POST["imageUrl"]
        price = request.POST["price"]
        category = request.POST["category"]
        currentUser = request.user

        categoryData =Category.objects.get(categoryName=category)

        newListing = Listing(
            brand=brand,
            model=model,
            description=description,
            weight=float(weight),
            imageUrl=imageUrl,
            price=float(price),
            category=categoryData,
            owner=currentUser
        )
        newListing.save()
        newLog = Logs(
            transaction= str(currentUser) + " add new vehicle " +str(model)
        )
        newLog.save()

        return HttpResponseRedirect(reverse(index))

def updateListing(request,id):
    listingData = Listing.objects.get(pk=id)
    allCategories = Category.objects.all()
    form= ProductForm(instance=listingData)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=listingData)
        if form.is_valid():
            listingData = form.save(commit=False)
            listingData.owner = request.user
            listingData.save()
            return redirect('index')
    context = {
        "categories":allCategories,
        "form":form
    }
    return render(request, 'auctions/update.html', context)
    
def rentListing(request,id):
    listingData = Listing.objects.get(pk=id)
    if request.method == 'POST':
        rent_date = request.POST.get('rentDate')
        returnRentDate = request.POST.get('returnRentDate')
        listingData.rented = datetime.strptime(rent_date, '%m/%d/%Y').strftime('%Y-%m-%d')
        listingData.isActive=False
        listingData.owner = request.user
        listingData.save()
        newRented = Rentlist(
            customer=str(request.user),
            iha="iha id:"+str(id)+" model:"+listingData.model,
            rentStartDate=datetime.strptime(rent_date, '%m/%d/%Y').strftime('%Y-%m-%d'),
            rentFinishDate=datetime.strptime(returnRentDate, '%m/%d/%Y').strftime('%Y-%m-%d'),
            date=datetime.now()
        )
        newRented.save()
        return redirect('index')
        

    return render(request, 'auctions/rentcheckout.html',{
        "listing":listingData
    })

def showRentList(request):
    rentRequests=Rentlist.objects.all()
    return render(request, "auctions/rentrequest.html",{
        "rentRequests":rentRequests,
        
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
