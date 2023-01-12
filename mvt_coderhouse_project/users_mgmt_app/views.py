from django.shortcuts import render, redirect
from users_mgmt_app.models import Member, Client, Group
from django.urls import reverse
from users_mgmt_app.forms import ClientForm


# Create your views here.

def list_users(request):
    cntxt = {
        'users': Member.objects.all()
    }
    return render(
        request=request,
        template_name='list_users.html',
        context=cntxt,
    )   

def home_page(request):

    return render(request=request, template_name='home.html',) 

def under_construction(request):

    return render(request=request, template_name='under_construction.html',)

def list_clients(request):
    cntxt = {
        'clients': Client.objects.all()
    }
    return render(
        request=request,
        template_name='list_client.html',
        context=cntxt,
    )

def list_groups(request):
    cntxt = {
        'groups': Group.objects.all()
    }
    return render(
        request=request,
        template_name='list_groups.html',
        context=cntxt,
    )

def new_client(request):
    if request.method == "POST":
        new_form = ClientForm(request.POST)
        if new_form.is_valid():
            data = new_form.cleaned_data
            new_client = Client(client_name=data['client_name'], client_email=data['client_email'],client_phone=data['client_phone'],client_address=data['client_address'])
            new_client.save()
            sucess_url = reverse('list_clients')
            return redirect(sucess_url)
    else:  # GET
        new_form = ClientForm()
    return render(
        request=request,
        template_name='client_form.html',
        context={'new_form': new_form},
    )