from django import forms
from django.contrib.auth.models import User
from .models import UserServiceBooking
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        new = cleaned_data.get("new_password")
        confirm = cleaned_data.get("confirm_password")
        if new != confirm:
            raise forms.ValidationError("New passwords do not match.")



class UserServiceBookingForm(forms.ModelForm):
    class Meta:
        model = UserServiceBooking
        fields = ['service_type', 'preferred_date', 'preferred_time', 'address', 'city' , 'additional_notes']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time'}),
        }