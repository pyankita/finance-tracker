from django.urls import reverse_lazy
from .models import Transaction
from finance_tracker.forms import RegisterForm
from django.contrib.auth import login
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin


class TransactionListView(LoginRequiredMixin,ListView):
    model=Transaction
    template_name="transaction_list.html"
    context_object_name='transactions'
    ordering=['-date']
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        transaction_type = self.request.GET.get('type')  # e.g. income or expense
        start_date = self.request.GET.get('start_date')  # e.g. 2025-06-01
        end_date = self.request.GET.get('end_date')      # e.g. 2025-06-07

        if transaction_type in ['income', 'expense']:
            queryset = queryset.filter(type=transaction_type)
        
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        
        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        income = Transaction.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = Transaction.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
        balance = income - expense

        context['total_income'] = income
        context['total_expense'] = expense
        context['balance'] = balance
        return context

class TransactionDetailView(LoginRequiredMixin,DetailView):
    model=Transaction
    template_name="transaction_detail.html"
    context_object_name="transaction"

class TransactionCreateView(LoginRequiredMixin,CreateView):
    model=Transaction
    template_name="transaction_create.html"
    fields="__all__"
    success_url=reverse_lazy('transaction-list')

class TransactionDeleteView(LoginRequiredMixin,DeleteView):
    model=Transaction
    template_name="transaction_delete.html"
    success_url=reverse_lazy("transaction-list")


class TransactionUpdateView(LoginRequiredMixin,UpdateView):
    model=Transaction
    template_name="transaction_update.html"
    fields="__all__"
    success_url=reverse_lazy("transaction-list")