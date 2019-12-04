from django import forms

class loginform1(forms.Form):
    student_name=forms.CharField(required=True,max_length=20)
    username=forms.CharField(required=True,max_length=20)
    password=forms.CharField(required=True,max_length=15,widget=forms.PasswordInput)
    branch=forms.CharField(required=True,max_length=10)
    email=forms.EmailField(max_length=50)


class login(forms.Form):
    username= forms.CharField(required=True,max_length=20)
    password=forms.CharField(max_length=15,widget=forms.PasswordInput)
    
