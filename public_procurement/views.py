from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
import public_procurement
from public_procurement.forms import TheContractorAddForm, ContractAddForm, AddProcedureForm, \
    CommentAddForm, LoginForm, UserCreateForm
from public_procurement.models import TheContractor, Contract, TypeProcurement, Comment, Procedure


class AddTheContractorView(View):
    def get(self, request):
        form = TheContractorAddForm()
        return render(request, 'form.html', {'form': form})

    def post(slef, request):
        form = TheContractorAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number_NIP = form.cleaned_data['number_NIP']
            nameStreet = form.cleaned_data['nameStreet']
            city = form.cleaned_data['city']
            TheContractor.objects.create(name=name, number_NIP=number_NIP, nameStreet=nameStreet, city=city)
            return redirect('list_contractor')
        return render(request, 'form.html', {'form': form})


class ListContractorView(View):

    def get(self, request):
        contractor = TheContractor.objects.all()
        return render(request, 'ContractorList.html', {'contractor': contractor})


class AddContractView(View):
    def get(self, request):
        form = ContractAddForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = ContractAddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            contractor = form.cleaned_data['contractor']
            value_contract = form.cleaned_data['value_contract']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            con = Contract.objects.create(title=title, contractor=contractor, value_contract=value_contract,
                                          start_date=start_date, end_date=end_date)
            con.contractor.set(contractor)
            return redirect('list_contract')
        return render(request, 'form.html', {'form': form})


class ListContractView(View):
    def get(self, request):
        contract = Contract.objects.all()
        return render(request, 'ContractList.html', {'contract': contract})


class AddTypeProView(View):
    def get(self, request):
        cont = Contract.objects.all()
        return render(request, 'addType.html', {'cont': cont})

    def post(self, request):
        type_procurement = request.POST.get('type_procurement')
        TypeProcurement.objects.create(type_procurement=type_procurement)
        return redirect('list_typ')



class ListTypView(View):
    def get(self, request):
        typ_procurement = TypeProcurement.objects.all()
        return render(request, 'TypList.html', {'typ_procurement': typ_procurement})


class AddProcedureView(View):
    def get(self, request):
        form = AddProcedureForm()
        return render(request, 'form.html', {'form': form})
    def post(self, request):
        form = AddProcedureForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name_procedure']
            data_initiation = form.cleaned_data['data_initiation']
            value = form.cleaned_data['value']
            end_date_procedure = form.cleaned_data['end_date_procedure']
            Procedure.objects.create(name_procedure=name, data_initiation=data_initiation, value=value, end_date_procedure=end_date_procedure)
            return redirect('list_procedure')
        return render(request, 'form.html', {'form': form})
class ListProcedureView(View):
    def get(self, request):
        procedure = Procedure.objects.all()
        return render(request, 'ProcedureList.html', {'procedure': procedure})

class ContractDetailView(View):

    def get(self, request, pk):
        contract = Contract.objects.get(pk=pk)
        form = CommentAddForm()
        return render(request, 'contract_detail.html', {'contract': contract, 'form': form})


class AddCommentView(View):

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
        return render(request, 'form.html', {'form': form})

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
        return render(request, 'form.html', {'form': form, 'message': message})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class RegisterView(View):

    def get(self, request):
        form = UserCreateForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.set_password(form.cleaned_data['password'])
            u.save()
            return redirect("index")
        return render(request, 'form.html', {'form': form})
