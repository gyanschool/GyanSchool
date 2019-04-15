from django import forms


class LoginForm(forms.Form):
    username=forms.CharField(label="username",
                             required = True,
                             max_length=20,
                            )

    password=forms.CharField(label="password",
                             required = True,
                             max_length=20,
                             widget = forms.PasswordInput(),
                             )
#login_form
