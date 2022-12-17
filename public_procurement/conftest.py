from django.contrib.auth.models import User, Permission
from jedi.plugins import pytest

from public_procurement.models import TheContractor, Contract

@pytest.fixture
def contractor():
    lst = []
    for n in range(10):
        p = TheContractor.objects.create(name=n, number_NIP=n, nameStreet=n, city=n)
        lst.append(p)
    return lst

@pytest.fixture
def contract(contractor):
    contractor_ = contractor[0]
    return Contract.objects.create(title="Robota", contractor=contractor_, value_contract=15121.02, start_date=2022-12-12, end_date=2022-12-31)

@pytest.fixture
def user():
    u = User.objects.create(username='tadeusz')
    return u

@pytest.fixture
def user_with_permission():
    u = User.objects.create(username='tadeusz')
    permission = Permission.objects.get(codename='add_comment')
    u.user_permissions.add(permission)
    return u
