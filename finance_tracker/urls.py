
from django.urls import path

from finance_tracker.views import RegisterView

urlpatterns = [
   
    path("register/",RegisterView.as_view(),name='register'),
]
