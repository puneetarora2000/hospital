from models import InsuranceCompany,Patient,PatientHealthData,RegisterDevicesForPatient
from autofixture import generators, register, AutoFixture
from django.contrib.auth.models import User ,Group

class PatientAutoFixture(AutoFixture):
    @classmethod
    def makePat(self):
     field_values = {
        'Patient_ID': generators.IntegerGenerator(min_value=1,max_value=111111),
        'FullName': generators.FirstNameGenerator(),
        'FullAddress': generators.LoremSentenceGenerator(),
        'Patient_History': generators.LoremSentenceGenerator(),
        'RegisterPatientRemoteMonitoring': generators.BooleanGenerator(),
        'Credential': generators.ImageGenerator(),
        #'DoctorID': generators.IntegerGenerator(min_value=5,max_value=5),
        #'InsuranceCompanyID':generators.IntegerGenerator(min_value=2,max_value=99) ,
     }
     fixture = AutoFixture(Patient, generate_fk=True)
     entries=fixture.create(5)



class RegisterDevicesForPatientCompanyAutoFixture(AutoFixture):
    field_values = {
        'Patient_ID': generators.IntegerGenerator(min_value=1,max_value=8000),
        'SugarMonitoringDevice': generators.StaticGenerator('X'),
        'WorkOutMachineDevice': generators.StaticGenerator('X'),
        'PulseMonitor': generators.StaticGenerator('X'),
        'TemperatureMonitor': generators.StaticGenerator('X'),
        'SleepPatternsMonitor': generators.StaticGenerator('X'),
        'GulcoseMonitoringDeviceID': generators.StaticGenerator('X'),
        'WorkOutMachineDeviceID': generators.StaticGenerator('X'),
        'PulseMonitorID': generators.StaticGenerator('X'),
        'TemperatureMonitorID': generators.StaticGenerator('X'),
        'SleepPatternsDeviceID': generators.StaticGenerator('X'),


    }

class PatientHealthDataCompanyAutoFixture(AutoFixture):
    field_values = {
        'Patient_ID': generators.StaticGenerator('X'),
        'InsuranceCompanyID': generators.StaticGenerator('X'),
        'DataOfReading': generators.StaticGenerator('X'),
        'SugarMonitoringDeviceReading': generators.StaticGenerator('X'),
        'WorkOutMachineDeviceReading': generators.StaticGenerator('X'),
        'PulseMonitorReading': generators.StaticGenerator('X'),
        'TemperatureMonitorReading': generators.StaticGenerator('X'),
        'SleepPatternsMonitorReading': generators.StaticGenerator('X'),

    }
class InsuranceCompanyAutoFixture(AutoFixture):
    field_values = {
        'InsuranceCompanyName': generators.StaticGenerator('X'),
    }


register(Patient, PatientAutoFixture)
register(PatientHealthData, PatientHealthDataCompanyAutoFixture)
register(RegisterDevicesForPatient, RegisterDevicesForPatientCompanyAutoFixture)
register(InsuranceCompany, InsuranceCompanyAutoFixture)