from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import public_procurement
from public_procurement.models import TheContractor, TypeProcurement, Comment, Procedure


class TheContractorAddForm(forms.ModelForm):
    class Meta:
        model = TheContractor
        fields = "__all__"


class ContractAddForm(forms.Form):
    title = forms.CharField(max_length=458)
    contractor = forms.ModelChoiceField(
        queryset=TheContractor.objects.all(), widget=forms.RadioSelect
    )
    type = forms.ModelChoiceField(
        queryset=TypeProcurement.objects, widget=forms.RadioSelect
    )
    value_contract = forms.IntegerField()
    start_date = forms.DateField()
    end_date = forms.DateField()


class addTypeProcurementForm(forms.ModelForm):
    class Meta:
        model = TypeProcurement
        fields = "__all__"

class AddProcedureForm(forms.ModelForm):

    class Meta:
        model = Procedure
        fields = "__all__"


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
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
