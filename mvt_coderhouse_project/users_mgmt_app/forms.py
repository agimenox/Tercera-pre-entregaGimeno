from django import forms

class ClientForm(forms.Form):
    client_name = forms.CharField(max_length=100,required=True)
    client_email = forms.CharField(max_length=100,required=True)
    client_phone = forms.CharField(max_length=100)
    client_address = forms.CharField(max_length=100)