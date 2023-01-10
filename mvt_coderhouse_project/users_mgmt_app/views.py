from django.shortcuts import render
from users_mgmt_app.models import Member

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