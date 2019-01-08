from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    title = forms.CharField(
        label='Product Name', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Your Input...'}
            )
        )

    email = forms.EmailField()

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your description...',
                'class': 'new-class-name two',
                'id': 'text-area-id',
                'rows': 10,
                'cols': 60
            }
        )
    )

    price = forms.DecimalField(initial=89.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'description',
        ]

    # specific-developer-defined cleaning: 
    # def clean_<whatever var name/form field you declared>
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'DK' in title:
            raise forms.ValidationError("Invalid Title. Title should contain DK ")
        if not 'Keren' in title:
            raise forms.ValidationError("Invalid Title. Title should contain keren ")
        return title

    def clean_email(self, *args, **args):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError("Invalid email address.")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(
        label='Product Name', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Your Input...'}
            )
        )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your description...',
                'class': 'new-class-name two',
                'id': 'text-area-id',
                'rows': 10,
                'cols': 60
            }
        )
    )
    price = forms.DecimalField(initial=89.99)