from allauth.account.forms import SignupForm
from django import forms
from django.http import HttpRequest


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    """

    full_name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your full name"}),
    )
    short_name = forms.CharField(
        label="Short name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your first name or nickname"}
        ),
    )

    def save(self, request: HttpRequest):
        user = super().save(request)
        user.full_name = self.cleaned_data["full_name"]
        user.short_name = self.cleaned_data["short_name"]
        user.save()
        return user
