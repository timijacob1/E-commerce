from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import SignUpform
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpform
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def index_page(request):
    return render(request,'index.html')

# def login(request):
#     return render(request,'login.html')