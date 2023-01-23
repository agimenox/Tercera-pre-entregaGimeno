from django.shortcuts import render, redirect
from users_mgmt_app.models import Client, Group, User
from django.urls import reverse
from users_mgmt_app.forms import ClientForm, GroupForm, UserForm


# Create your views here.

def list_users(request):
    cntxt = {
        'users': User.objects.all()
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

def search_groups(request):
    if request.method == "POST":
        data = request.POST
        searchs_result = Group.objects.filter(group_name__contains=data['name_to_search'])
        context = {
            'groups': searchs_result
        }
        return render(
            request=request,
            template_name='list_groups.html',
            context=context,
        )


def new_user(request):
    if request.method == "POST":
        new_form = UserForm(request.POST)
        if new_form.is_valid():
            data = new_form.cleaned_data
            new_user = User(first_name=data['first_name'],last_name=data['last_name'],birth_date=data['birth_date'],gender=data['gender'],email=data['email'],preferr_number=data['preferr_number'],preferr_color=data['preferr_color'])
            new_user.save()
            sucess_url = reverse('list_users')
            return redirect(sucess_url)
    else:  # GET
        new_form = UserForm()
    return render(
        request=request,
        template_name='user_form.html',
        context={'new_form': new_form},
    )

def search_users(request):
    if request.method == "POST":
        data = request.POST
        searchs_result = User.objects.filter(first_name__contains=data['name_to_search'])
        context = {
            'users': searchs_result
        }
        return render(
            request=request,
            template_name='list_users.html',
            context=context,
        )
    
def show_user_data(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(
        request=request,
        template_name='show_user_data.html',
        context=context,
    )




def edit_user_data(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.birth_date = data['birth_date']
            user.gender = data['gender']
            user.email = data['email']
            user.preferr_number = data['preferr_number']
            user.preferr_color = data['preferr_color']
            user.save()
            sucess_url = reverse('list_users')
            return redirect(sucess_url)
    else:  # GET
        inicial = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'birth_date': user.birth_date,
            'gender': user.gender,
            'email': user.email,
            'preferr_number': user.preferr_number,
            'preferr_color': user.preferr_color,
        }
        form = UserForm(initial=inicial)
    return render(
        request=request,
        template_name='edit_user.html',
        context={'form': form},
    )

def delete_user(request, id):
    user_to_delete = User.objects.get(id=id)
    if request.method == "POST":
        user_to_delete.delete()
        sucess_url = reverse('list_users')
        return redirect(sucess_url)
