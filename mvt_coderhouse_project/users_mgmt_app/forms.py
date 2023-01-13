from django import forms

class ClientForm(forms.Form):
    client_name = forms.CharField(max_length=100,required=True)
    client_email = forms.CharField(max_length=100,required=True)
    client_phone = forms.CharField(max_length=100)
    client_address = forms.CharField(max_length=100)

class GroupForm(forms.Form):
    group_name = forms.CharField(max_length=50)
    group_description = forms.CharField(max_length=200)

class MemberForm(forms.Form):
    first_name= forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    birth_date = forms.DateField(null=True)
    gender = forms.CharField(max_length=1)
    email = forms.EmailField(max_length=20,null=True)
    preferr_number = forms.IntegerField(null=True)
    preferr_color = forms.CharField(max_length=10,required=True)