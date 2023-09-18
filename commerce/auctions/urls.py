from django.urls import path,include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="create"),
    path("displayCategory", views.displayCategory, name="displayCategory"),
    path("listing/<int:id>",views.listing,name="listing"),
    path("updateListing/<int:id>/",views.updateListing,name="updateListing"),
    path("deleteListing/<int:id>/",views.deleteListing,name="deleteListing"),
    path("rentListing/<int:id>/",views.rentListing,name="rentListing"),
    path("showRentList", views.showRentList, name="showRentList"),
    path('api/', include('auctions.api.urls'))
]
