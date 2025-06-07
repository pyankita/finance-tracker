
from django.urls import path
from finance_tracker import views

urlpatterns = [
   
    path("",views.TransactionListView.as_view(),name="transaction-list"),
    path("detail/<int:pk>/",views.TransactionDetailView.as_view(),name="transaction-detail"),
    path("create/",views.TransactionCreateView.as_view(),name="transaction-create"),
    path("delete/<int:pk>/",views.TransactionDeleteView.as_view(),name="transaction-delete"),
    path("update/<int:pk>/",views.TransactionUpdateView.as_view(),name="transaction-update"),

]
