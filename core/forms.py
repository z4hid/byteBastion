from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Full Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email Address'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Your Message',
            'rows': 4
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'space-y-6'
        self.helper.layout = Layout(
            Field('name', css_class='form-input mt-1 block w-full rounded-md shadow-sm'),
            Field('email', css_class='form-input mt-1 block w-full rounded-md shadow-sm'),
            Field('message', css_class='form-textarea mt-1 block w-full rounded-md shadow-sm'),
            Submit('submit', 'Send Message', css_class='bg-indigo-600 hover:bg-indigo-700 text-white py-2 px-4 rounded-md w-full')
        )
