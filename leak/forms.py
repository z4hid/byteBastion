from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LeakForm(forms.Form):
    username_or_email = forms.CharField(
        max_length=255,
        required=True,
        label="Username or Email",
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-md py-2 px-3 text-gray-900 shadow-sm focus:ring-2 focus:ring-indigo-600',
            'placeholder': 'Enter your email or username'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Scan for Breaches', css_class='w-full py-3 px-4 bg-indigo-600 rounded-md text-white font-medium hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500'))
