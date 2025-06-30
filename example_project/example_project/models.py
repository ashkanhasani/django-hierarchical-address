from django.db import models
from django_places.models import ContinentField, CountryField, StateProvinceField, CityField, CountyField

class TestAddressFieldsModel(models.Model):
    name = models.CharField(max_length=100)
    continent = ContinentField(null=True, blank=True, help_text="Continent as JSON")
    country = CountryField(null=True, blank=True, help_text="Country as JSON")
    state_province = StateProvinceField(null=True, blank=True, help_text="State/Province as JSON")
    city = CityField(null=True, blank=True, help_text="City as JSON")
    county = CountyField(null=True, blank=True, help_text="County as JSON")
    address_line = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name 