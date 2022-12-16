from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
import public_procurement
from public_procurement.forms import TheContractorAddForm, ContractAddForm, AddProcedureForm, addTypeProcurementForm, \
    CommentAddForm, LoginForm, UserCreateForm
from public_procurement.models import TheContractor, Contract, TypeProcurement, Comment, Procedure


class AddTheContractorView(View):
    def get(self, request):
        form = TheContractorAddForm()
        return render(request, 'form.html', {'form': form})

    def post(slef, request):
        form = TheContractorAddForm(request.POST)
        name = request.POST.get('name')
        number_NIP = request.POST.get('number_NIP')
        nameStreet = request.POST.get('nameStreet')
        city = request.POST.get('city')
        TheContractor.objects.create(name=name, number_NIP=number_NIP, nameStreet=nameStreet, city=city)
        return redirect('list_contractor')

class ListContractorView(View):

    def get(self, request):
        contractor = TheContractor.objects.all()
        return render(request, 'ContractorList.html', {'contractor': contractor})

class AddContractView(View):
    def get(self, request):
        form = TheContractorAddForm()
        return render(request, 'form.html', {'form': form} )


    def post(self, request):
        form = TheContractorAddForm(request.POST)
        title = request.POST.get('title')
        contractor = request.POST.get('contarctor')
        type = request.POST.get('type')
        value_contract = request.POST.get('value_contract')
        start_date = request.POST.get('name')('start_date')
        end_date = request.POST.get('end_date')
        Contract.objects.create(title=title, contractor=contractor, type=type, value_contract=value_contract, start_date=start_date, end_date=end_date)
        return redirect('list_contract')

class ListContractView(View):
    def get(self, request):
        contract = Contract.objects.all()
        return render(request, 'ContractList.html', {'contract': contract})

class AddTypeProView(View):

    def get(self, request):
        form = addTypeProcurementForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = addTypeProcurementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'form.html', {'form': form},)

class AddProcedureView(View):

    def get(self, request):
        form = AddProcedureForm()
        return render(request, 'form.html', {'form': form})
    def post(self, request):
        form = AddProcedureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'form.html', {'form': form},)

class ContractDetailView(View):

    def get(self, request, pk):
        contract = Contract.objects.get(pk=pk)
        form = CommentAddForm()
        return render(request, 'contract_detail.html', {'contract': contract, 'form': form})


class AddCommentView(PermissionRequiredMixin, View):
    permission_required = ['public_procurement.add_comment']

    def post(self, request, contract_pk):
        form = CommentAddForm(request.POST)
        contract = Contract.objects.get(pk=contract_pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.contract = contract
            comment.author = request.user
            comment.save()
            return redirect('detail_contract', contract_pk)

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        message = ""
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            message = "nie poprawne hasło lub/i nazwa użytkownika"
        return render(request, 'form.html', {'form': form, 'message':message})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class RegisterView(View):

    def get(self, request):
        form = UserCreateForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.set_password(form.cleaned_data['password'])
            u.save()
            return redirect("index")
        return render(request, 'form.html', {'form':form})