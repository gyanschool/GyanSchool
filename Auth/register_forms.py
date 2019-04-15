from django import forms


class RegisterForm(forms.Form):
    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
    CHOICES = (
        ('teacher', 'TEACHER'),
        ('student', 'STUDENT'),

    )

    username = forms.CharField(label="username",
                               required=True,
                               max_length=20,
                               )

    email = forms.CharField(required=True,
                            label='Email',
                            max_length=32,
                            )

    phno = forms.CharField(required=True,
                           label='phno',
                           max_length=12,
                           )

    city = forms.CharField(label='city',
                           max_length=25,
                           )

    institution = forms.CharField(label='instituion',
                           max_length=100,
                           )

    password = forms.CharField(label="password",
                               required=True,
                               max_length=20,
                               widget=forms.PasswordInput(),
                               )
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    LOG_IN_AS = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CHOICES,
    )



