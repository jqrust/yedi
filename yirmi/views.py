from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user

from .forms import UserForm, ReportForm
from .models import User, Report, Department
from django.views import generic
# Create your views here.

class ReportView(generic.ListView):
    template_name = 'yirmi/report.html'
    context_object_name = 'report_list'
    def get_queryset(self):      
        curr_user = get_user(self.request)        
        dep = Department.objects.filter(user=curr_user)
        if(curr_user.is_anonymous):
            return
        elif(dep): 
            return Report.objects.filter(department__in=dep)
        else:
            return Report.objects.filter(createdby=curr_user)
        

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
    fields = ['header', 'text',   'department',]
    def post(self, request, *args, **kwargs):
        form =  ReportForm(request.POST)
        if form.is_valid():
            header=form.cleaned_data.get('header')
            text = form.cleaned_data.get('text')
            department = form.cleaned_data.get('department')
            obj = Report(header=header,text=text,createdby=get_user(self.request),department =department)
            obj.save()
            return redirect("../")
        #d = Department.objects.all()
        #context = {'department_obj':d}
        return render(request, self.template_name, {})

def home_view(request):
    return render(request,"yirmi/home.html",{})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("../report/")
        else:
            context = {
                "not_user": True
            }
            return render(request,"yirmi/login.html", context)
    return render(request,"yirmi/login.html")

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
