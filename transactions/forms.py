from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList 
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model  = Transaction
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)

    def save(self, commit = True):
        self.instance.account = self.account 
        self.account.balance 
        return super().save(commit)
    
class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposite = 300
        amount = self.cleaned_data.get('amount')
        if amount < min_deposite:
            raise forms.ValidationError(f'you need at least {min_deposite} to deposite')
        return amount