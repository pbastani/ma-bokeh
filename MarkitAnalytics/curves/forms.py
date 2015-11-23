from django import forms


class CurveConstructionForm(forms.Form):
    constructors_path = forms.CharField(
        label="Constructors",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Constructors File Path'}))

    processors_path = forms.CharField(
        label="Processors",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Processors File Path'}))

    market_data_path = forms.CharField(
        label="Market Data",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Market Data File Path'}))
