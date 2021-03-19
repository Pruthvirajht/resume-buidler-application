from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Experience,Education,Skill



class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})}

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {'password':forms.PasswordInput(attrs={'auto-complete':'current-password','class':'form-control'})}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','phno','city','state','about','linkdin','github']
        labels = {'name':'Name','email':'Email','phno':'Phone Number','city':'City','state':'State','about':'About','linkdin':'Linkdin','github':'Github'}

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['sslc','puc','degree','percentage','city','state']
        labels = {'sslc':'SSLC','puc':'PUC','degree':'Degree','percentage':'Percentage','city':'City','state':'State'}


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']
        labels = {'skill':'Skill'}

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['jobrole','companyname','projects','city','state']
        labels = {'jobrole':'Job Role','companyname':'Company Name','projects':'Projects','city':'City','state':'State'}