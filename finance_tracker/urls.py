
from django.urls import path
from finance_tracker import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(next_page="login"),name="logout"),
    path("",views.TransactionListView.as_view(),name="transaction-list"),
    path("detail/<int:pk>/",views.TransactionDetailView.as_view(),name="transaction-detail"),
    path("create/",views.TransactionCreateView.as_view(),name="transaction-create"),
    path("delete/<int:pk>/",views.TransactionDeleteView.as_view(),name="transaction-delete"),
    path("update/<int:pk>/",views.TransactionUpdateView.as_view(),name="transaction-update"),
    path("register/",views.RegistrationCreateView.as_view(),name="register"),

]
