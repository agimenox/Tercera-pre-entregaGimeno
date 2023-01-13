from django.shortcuts import render, redirect
from users_mgmt_app.models import Member, Client, Group
from django.urls import reverse
from users_mgmt_app.forms import ClientForm, GroupForm
from django.db.models import Q


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

def search_clients(request):
    if request.method == "POST":
        data = request.POST
        searchs_result = Client.objects.filter(client_name__contains=data['name_to_search'])
        context = {
            'clients': searchs_result
        }
        return render(
            request=request,
            template_name='list_client.html',
            context=context,
        )


def new_group(request):
    if request.method == "POST":
        new_form = GroupForm(request.POST)
        if new_form.is_valid():
            data = new_form.cleaned_data
            new_group = Group(
                group_name=data['group_name'],
                group_description=data['group_description'],
                )
            new_group.save()
            sucess_url = reverse('list_groups')
            return redirect(sucess_url)
    else:  # GET
        new_form = GroupForm()
    return render(
        request=request,
        template_name='group_form.html',
        context={'new_form': new_form},
    )