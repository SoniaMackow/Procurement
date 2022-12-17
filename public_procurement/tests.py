import pytest
from django.test import Client
from django.urls import reverse

from public_procurement.forms import CommentAddForm, TheContractorAddForm, ContractAddForm, LoginForm, UserCreateForm, AddProcedureForm
from public_procurement.models import Contract, Comment, TheContractor, TypeProcurement, Procedure


def test_index_view():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_contractor(contractor):
    client = Client()
    url = reverse('list_contractor')
    response = client.get(url)
    contractor_context = response.context['contractor']
    assert contractor_context.count() == len(contractor)
    for p in contractor:
        assert p in contractor_context

@pytest.mark.django_db
def test_create_contractor_post():
    data = {
        'name': 'test',
        'number_NIP': '1236545',
        'nameStreet' : 'testowy',
        'city': 'Testowo'
    }
    client = Client()
    url = reverse('create_contractor')
    response = client.post(url, data)
    assert response.status_code == 302
    assert TheContractor.objects.get(name='test', number_NIP='1236545', nameStreet='testowy', city='Testowo')


@pytest.mark.django_db
def test_list_contract(contract):
    client = Client()
    url = reverse('list_contract')
    response = client.get(url)
    contract_context = response.context['contract']
    assert contract_context.count() == len(contract)
    for m in contract:
        assert m in contract_context

