from django import forms
from django.core import validators
from .models import Product


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(min_value=1, max_value=500000, decimal_places=2)
#     description = forms.CharField(
#         label="product description",
#         widget=forms.Textarea(attrs={"rows": 5, "cols": 30}),
#         validators=[validators.RegexValidator(
#             regex=r"color",
#             message="Filed must contain word 'color'",
#         )]
#     )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount"
