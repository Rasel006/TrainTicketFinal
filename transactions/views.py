from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from . models import Transaction
from .forms import DepositForm

# Create your views here.
class TransactionCreateMix(LoginRequiredMixin, CreateView):
    template_name = 'transaction/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs =  super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account 
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context.update({
            'title': self.title 
        })
        return context
    
class DepositeView(TransactionCreateMix):
    form_class = DepositForm
    title ="Get Started To Buy Ticket"

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account= self.request.user.account
        account.balance +=amount 
        account.save(
            update_fields = ['balance']
        )
        return super().form_valid(form)
    