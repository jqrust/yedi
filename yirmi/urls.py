from django.urls import path
from . import views
app_name = 'yirmi'
urlpatterns = [    
    path('',views.home_view,name="home"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('register/',views.register_view,name="register"),
    path('report/',views.ReportView.as_view(),name="report"),
    path('report/<int:pk>/',views.DetailView.as_view(),name="detail"),
    path('report/create/',views.CreateView.as_view(),name="create"),
]