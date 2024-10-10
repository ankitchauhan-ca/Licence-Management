from django import forms
from .models import License

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['license_key', 'user_email', 'expiration_date']
