from patient import Patient
from pk_models import marsh_drug, drug_from_clearances


def test_marsh_v1_70kg():
    drug = marsh_drug(Patient(40, 70, 170, "M"))
    assert round(drug.V1, 2) == 15.96


def test_marsh_only_v1_scales_with_weight():
    d70 = marsh_drug(Patient(40, 70, 170, "M"))
    d90 = marsh_drug(Patient(40, 90, 170, "M"))
    assert d70.V1 != d90.V1          # volume SHOULD change
    assert d70.k10 == d90.k10        # rate constants should NOT
    assert d70.k12 == d90.k12


def test_drug_from_clearances_divides_correctly():
    # made-up numbers chosen so every answer is different
    d = drug_from_clearances("test", V1=2, V2=4, V3=8, Cl1=1, Cl2=2, Cl3=4, ke0=0.5)
    assert d.k10 == 0.5   # Cl1 / V1
    assert d.k12 == 1.0   # Cl2 / V1
    assert d.k13 == 2.0   # Cl3 / V1
    assert d.k21 == 0.5   # Cl2 / V2
    assert d.k31 == 0.5   # Cl3 / V3