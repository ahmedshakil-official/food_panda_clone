from django import forms

from accounts.models import User, UserProfile
from common.validators import allow_only_image_validator


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "phone_number",
            "email",
            "password",
        ]

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")


class UserProfileForm(forms.ModelForm):
    profile_pic = forms.FileField(
        widget=forms.FileInput(attrs={"class": "btn btn-info"}),
        validators=[allow_only_image_validator],
    )

    cover_photo = forms.FileField(
        widget=forms.FileInput(attrs={"class": "btn btn-info"}),
        validators=[allow_only_image_validator],
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Start typing...", "required": "required"}
        )
    )

    longitude = forms.CharField(widget=forms.TextInput(attrs={"readonly": "readonly"}))
    latitude = forms.CharField(widget=forms.TextInput(attrs={"readonly": "readonly"}))

    class Meta:
        model = UserProfile
        fields = [
            "profile_pic",
            "cover_photo",
            "address",
            "city",
            "state",
            "country",
            "pin_code",
            "longitude",
            "latitude",
        ]
