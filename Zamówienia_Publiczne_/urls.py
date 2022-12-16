"""ProcurementII URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, ='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from public_procurement import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name='base.html'), name='index'),
    path('contract/<int:pk>/', views.ContractDetailView.as_view(), name='detail_contract'),
    path('addContract/', views.AddContractView.as_view(), name='create_contract'),
    path('listContract/', views.ListContractView.as_view(), name='list_contract'),
    path('addContractor/', views.AddTheContractorView.as_view(), name='create_contractor'),
    path('listContractor/', views.ListContractorView.as_view(), name='list_contractor'),
    path('contract/<int:pk>/', views.ContractDetailView.as_view(), name='detail_contract'),
    path('add_comment/<int:contract_pk>/', views.AddCommentView.as_view(), name='add_comment'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('addType/', views.AddTypeProView.as_view(), name='add_type'),
    path('listTyp/', views.ListTypView.as_view(), name='list_typ'),
    path('addProcedure/', views.AddProcedureView.as_view(), name='create_procedure'),
    path('listProcedure/', views.ListProcedureView.as_view(), name='list_procedure' )
]
