
from faker import Factory
from doctor.models import InsuranceCompany,Patient,RegisterDevicesForPatient


class InsuranceCompany():
fake = Factory.create()
for _ in range(0,10):
  print fake.name()
