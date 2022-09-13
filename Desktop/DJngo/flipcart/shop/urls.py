from django.urls import path
from . import views
#pass ---alok@123--us/nm--alok

urlpatterns = [
    path("", views.index, name="shophome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="Contact"),
    path("tracker/", views.tracker, name="Tracker"),
    path("search/", views.search, name="Search"),
    path("product/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("order/", views.order, name="Or-der"),
    path("handlerequest/",views.handlerequest, name="HandleRequest")
]


