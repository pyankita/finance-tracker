from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Transaction
from django.contrib.auth import login
from finance_tracker.forms import RegisterForm
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User 


class TransactionListView(LoginRequiredMixin,ListView):
    model=Transaction
    template_name="transaction_list.html"
    context_object_name='transactions'
    ordering=['-date']
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        queryset = queryset.filter(user=self.request.user)
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
        user_transactions = Transaction.objects.filter(user=self.request.user)
        income = user_transactions.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = user_transactions.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
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
    fields=["title","amount","date","type","category"]
    success_url=reverse_lazy('transaction-list')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class TransactionDeleteView(LoginRequiredMixin,DeleteView):
    model=Transaction
    template_name="transaction_delete.html"
    success_url=reverse_lazy("transaction-list")


class TransactionUpdateView(LoginRequiredMixin,UpdateView):
    model=Transaction
    template_name="transaction_update.html"
    fields=["title","amount","date","type","category"]
    success_url=reverse_lazy("transaction-list")

class RegistrationCreateView(CreateView):
    model=User
    form_class=RegisterForm
    template_name="registration/register.html"
    success_url=reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(self.request, user)
        return redirect(self.success_url)