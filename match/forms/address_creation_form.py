from django import forms

from core.forms import AddressCreateForm


class CustomCreateAddressForm(AddressCreateForm):
    def clean_city(self):
        city = self.cleaned_data['city']

        if city is None:
            raise forms.ValidationError(
                "Veuillez donner un nom de ville.")
        return city

    def clean_street(self):
        street = self.cleaned_data['street']

        if street is None:
            raise forms.ValidationError(
                "Veuillez donner un nom de rue.")
        return street

    def clean_number(self):
        number = self.cleaned_data['number']

        if number is None:
            raise forms.ValidationError(
                "Veuillez donner un numéro")
        return number
