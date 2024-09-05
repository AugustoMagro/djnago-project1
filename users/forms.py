from django import forms

class LoginForms(forms.Form):
    user = forms.CharField(
        label="User",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInput"
            }
        )
    )
    password = forms.CharField(
        label="Password",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "floatingInput"
            }
        )
    )

class RegisterForms(forms.Form):
    name = forms.CharField(
        label="Name",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInput"
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "id": "floatingInput"
            }
        )
    )

    password_1 = forms.CharField(
        label="Password",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "floatingInput"
            }
        )
    )

    password_2 = forms.CharField(
        label="Password Confirmation",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "floatingInput"
            }
        )
    )