from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from app_users.forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from curriculum.models import Standard
from .models import UserProfileInfo, Contact
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.models import User  # Import the User model
from .forms import UserForm  # Import your UserForm





# Create your views here.
def index(request):
    return render(request,'base.html')

    
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("please use correct id and password")
        
    else:
        return render(request, 'app_users/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_superuser = True if user_form.cleaned_data['user_type'] == 'teachers' else False
            user.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('index')
    else:
        user_form = UserForm()

    return render(request, 'app_users/registration.html', {'user_form': user_form})

class HomeView(TemplateView):
    template_name = 'app_users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        standards = Standard.objects.all()
        teachers = UserProfileInfo.objects.filter(user_type='teachers')
        context['standards'] = standards
        context['teachers'] = teachers
        return context

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'app_users/contact.html'
