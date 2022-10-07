from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-1'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-1'}))
    service = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-1'}))
