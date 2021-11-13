# from django import forms
# import secrets
# import string
# from .models import MusicSchool
#
#
# class AdminRegisterForm(forms.BaseModelForm):
#     email = forms.EmailField()
#     password = forms.CharField(max_length=50,
#                                initial=''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(20)))
#     name = forms.CharField(max_length=100)
#     musical_school_id = forms.ChoiceField(choices=MusicSchool.objects.all())
#
#
# class RegisterForm(forms.BaseModelForm):
#     email = forms.EmailField()
#     password = forms.CharField(max_length=50,
#                                initial=''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(20)))
#     name = forms.CharField(max_length=100)
#     musical_school_id = forms.IntegerField(show_hidden_initial=True)
