from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from djmoney.forms.fields import MoneyField
import public_procurement
from public_procurement.models import TypeProcurement, TheContractor, Comment, Procedure, Contract, CommentProcedure, \
    CommentProcedure


class AddTypeForm(forms.Form):
    type_procurement = forms.CharField(max_length=258)
    contract = forms.ModelMultipleChoiceField(queryset=Contract.objects.all(), widget=forms.CheckboxSelectMultiple)
class TheContractorAddForm(forms.ModelForm):
    class Meta:
        model = TheContractor
        fields = "__all__"


class ContractAddForm(forms.Form):
    title = forms.CharField(max_length=458)
    contractor = forms.ModelMultipleChoiceField(
        queryset=TheContractor.objects.all(), widget=forms.CheckboxSelectMultiple()
    )
    value_contract = MoneyField(decimal_places=2, default_currency='PLN', max_digits=11)
    start_date = forms.DateField()
    end_date = forms.DateField()


class AddProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = "__all__"


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class CommentProcedureAddForm(forms.ModelForm):
    class Meta:
        model = CommentProcedure
        fields = ['text']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        max_length=100, widget=forms.PasswordInput
    )


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise ValidationError('Hasła nie są takie same!')
