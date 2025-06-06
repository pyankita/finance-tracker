from django.urls import reverse_lazy
from .models import Transaction
from finance_tracker.forms import RegisterForm
from django.contrib.auth import login
from django.views.generic import ListView,DetailView,CreateView


class TransactionListView(ListView):
    model=Transaction
    template_name="transaction_list.html"
    context_object_name='transactions'
    ordering=['-date']

class TransactionDetailView(DetailView):
    model=Transaction
    template_name="transaction_detail.html"
    context_object_name="transaction"

class TransactionCreateView(CreateView):
    model=Transaction
    template_name="transaction_create.html"
    fields="__all__"
    success_url=reverse_lazy('transaction-list')