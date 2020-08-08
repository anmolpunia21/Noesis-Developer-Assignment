from django.urls import path
from .views import contact_view

urlpatterns = [
    path('contacts/', contact_view),
]
