from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AddExpenses,AddIncome
from django.forms import ModelForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
		
class AddExpensesForm(ModelForm):
    """docstring for ClassName"""
    class Meta:
        model = AddExpenses
        fields = ['amount','purpose','date','owner']
        widgets={
                    
                    "purpose": forms.TextInput(attrs={'placeholder':'purpose'}),
                    "amount":forms.NumberInput(attrs={'min':'0.00','step': 0.01}),
                    "date":forms.TextInput(attrs={'placeholder':'Date','class':'datepicker'}),
                 }
    def __init__(self, *arg, **kwargs):
        kwargs.setdefault('label_suffix', '') 
        super(AddExpensesForm, self).__init__(*arg, **kwargs)
        self.fields['owner'].widget = forms.HiddenInput()
        self.fields['amount'].required = True
        self.fields['purpose'].required = True
        self.fields['date'].required = True
        self.fields['amount'].label = 'Amount'
        self.fields['purpose'].label = 'Purpose'
        self.fields['date'].label = 'Date'

class AddIncomeForm(ModelForm):
    """docstring for ClassName"""
    class Meta:
        model = AddIncome
        fields = ['amount','source','date','owner']
        widgets={
                    
                    "source": forms.TextInput(attrs={'placeholder':'source'}),
                    "amount":forms.NumberInput(attrs={'min':'0.00','step': 0.01}),
                    "date":forms.TextInput(attrs={'placeholder':'Date','class':'datepicker'}),
                 }
    def __init__(self, *arg, **kwargs):
        kwargs.setdefault('label_suffix', '') 
        super(AddIncomeForm, self).__init__(*arg, **kwargs)
        self.fields['owner'].widget = forms.HiddenInput()
        self.fields['amount'].required = True
        self.fields['source'].required = True
        self.fields['date'].required = True
        self.fields['amount'].label = 'Amount'
        self.fields['source'].label = 'Source'
        self.fields['date'].label = 'Date'
        


