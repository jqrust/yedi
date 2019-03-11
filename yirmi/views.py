from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user

from .forms import UserForm, ReportForm  
from .models import User, Report
from django.views import generic 
# Create your views here.
class ReportView(generic.ListView):
    template_name = 'yirmi/report.html'
    context_object_name = 'report_list'
    def get_queryset(self):
        obj = Report.objects.filter(createdby=get_user(self.request))
        return obj
class DetailView(generic.DetailView):
    model = Report
    template_name = 'yirmi/detail.html'
    def get_queryset(self):
        return self.queryset

    def get(self,request,*args,**kwargs):
        pk = self.kwargs.get('pk')
        q = get_object_or_404(self.model, pk=pk )
        context = {'report': q }
        return render(request, self.template_name, context)
class CreateView(generic.CreateView):
    model = Report
    template_name = 'yirmi/create.html'
    fields = ['header',
            'text',   'department',]
    def post(self, request, *args, **kwargs):
        form =  ReportForm(request.POST)
        if form.is_valid():            
            header=form.cleaned_data.get('header')
            text = form.cleaned_data.get('text')
            department = form.cleaned_data.get('department')
            obj = Report(header=header,text=text,createdby=get_user(self.request),department =department)
            obj.save()
            return redirect("../")
        return render(request, self.template_name, {})
def home_view(request):
    return render(request,"yirmi/home.html",{})
def login_view(request):
    ph_username = "Kullanıcı Adı"
    ph_pw = "Şifre" 
    ph_login = "Giriş Yap"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect("../report/")  

    return render(request,"yirmi/login.html",{'ph_username':ph_username,'ph_pw':ph_pw,'ph_login':ph_login})
def logout_view(request):
    logout(request)
    return redirect("../")

def register_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    context = {
        'form' : form
    }
    return render(request,"yirmi/register.html",context)
