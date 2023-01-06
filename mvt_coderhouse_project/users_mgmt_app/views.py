from django.shortcuts import render
from users_mgmt_app.models import Member

# Create your views here.

def show_all_users(request):

    return render(request=request, template_name='modelo.html')

def list_users(request):
    cntxt = {
        'users': Member.objects.all()
    }
    return render(
        request=request,
        template_name='list_users.html',
        context=cntxt,
    )    