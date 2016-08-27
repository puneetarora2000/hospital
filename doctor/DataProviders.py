
from faker import Factory
from doctor.models import InsuranceCompany,Patient,RegisterDevicesForPatient
from faker.providers import BaseProvider

class OceanProvider(BaseProvider):

    __provider__ = "ocean"
    __lang__     = "en_US"

    oceans = [
        u'Atlantic', u'Pacific', u'Indian', u'Arctic', u'Southern',
    ]

    @classmethod
    def ocean(cls):
        return cls.random_element(cls.oceans)

class BloodPressureSensorProvider(BaseProvider):
    __provider__ = "bloodpressure"
    __lang__     = "en_US"

    bloodpressures = [
        u'110-120', u'40-120', u'420-120', u'410-1220', u'40-1220',
    ]

    @classmethod
    def bloodpressure(cls):
        return cls.random_element(cls.bloodpressures)


class TemperatureSensorDataProvider(BaseProvider):
    __provider__ = "temperature"
    __lang__     = "en_US"

    temperatures  = [
        u'97.1', u'40-120', u'420-120', u'410-1220', u'40-1220',
    ]

    @classmethod
    def temperature(cls):
        return cls.random_element(cls.temperatures)

class SleepPatternDataProvider(BaseProvider):
    __provider__ = "sleep"
    __lang__     = "en_US"

    sleeps  = [
        u'97.1', u'40-120', u'420-120', u'410-1220', u'40-1220',
    ]

    @classmethod
    def sleep(cls):
        return cls.random_element(cls.sleeps)

class BloodSugarSensorDataProvider(BaseProvider):
    __provider__ = "sugar"
    __lang__     = "en_US"

    sugars  = [
        u'97.1', u'40-120', u'420-120', u'410-1220', u'40-1220',
    ]

    @classmethod
    def sugar(cls):
        return cls.random_element(cls.sugars)

class WorkOutSensorDataProvider(BaseProvider):
    __provider__ = "workout"
    __lang__     = "en_US"

    workouts  = [
        u'97.1', u'40-120', u'420-120', u'410-1220', u'40-1220',
    ]

    @classmethod
    def workout(cls):
        return cls.random_element(cls.workouts)

class PulseSensorDataProvider(BaseProvider):
    __provider__ = "pluse"
    __lang__     = "en_US"

    pluses  = [
        u'97.1', u'40-120', u'420-120', u'410-1220', u'40-1220',
    ]

    @classmethod
    def pluse(cls):
        return cls.random_element(cls.pluses)


class InsuranceCompanyDataProvider(BaseProvider):
    __provider__ = "pluse"
    __lang__     = "en_US"

    pluses  = [
        u'97.1', u'40-120', u'420-120', u'410-1220', u'40-1220',
    ]

    @classmethod
    def pluse(cls):
        return cls.random_element(cls.pluses)