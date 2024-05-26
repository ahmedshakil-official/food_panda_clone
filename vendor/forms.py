from django import forms

from common.validators import allow_only_image_validator
from vendor.models import Vendor


class VendorForm(forms.ModelForm):
    vendor_licence = forms.FileField(
        widget=forms.FileInput(attrs={"class": "btn btn-info"}),
        validators=[allow_only_image_validator],
    )

    class Meta:
        model = Vendor
        fields = ["vendor_name", "vendor_licence"]
