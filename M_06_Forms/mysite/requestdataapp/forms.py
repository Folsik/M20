from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import UploadProduct, BuyProduct


# class UserBioForm(forms.Form):
#     name = forms.CharField(max_length=15)
#     age = forms.IntegerField(label="Your age", max_value=100, min_value=1)
#     bio = forms.CharField(label="Biography", widget=forms.Textarea)


class UserBioForm(forms.ModelForm):
    class Meta:
        model = UploadProduct
        fields = "name", "age", "bio"


def validate_file_name(file: InMemoryUploadedFile) -> None:
    if file.name and "virus" in file.name:
        raise ValidationError("File name should not contain  'virus'")


class UploadFileForm(forms.Form):
    file = forms.FileField()


class UserBuyProduct(forms.ModelForm):
    class Meta:
        model = BuyProduct
        fields = "name", "quantity", "address", "comment"
