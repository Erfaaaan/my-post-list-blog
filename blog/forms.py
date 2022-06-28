from django import forms
from .models import account,comment

class accountform(forms.Form):
    SEX_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    firstname=forms.CharField(max_length=25)
    lastname=forms.CharField(max_length=50)
    sex = forms.ChoiceField(choices=SEX_CHOICES,widget=forms.RadioSelect)
    address = forms.CharField(max_length=250)
    age=forms.IntegerField()
    phone=forms.CharField(max_length=11)

    def clean_phone(self):
        s=self.cleaned_data['phone']
        if s:
            if not s.isnumeric():
                raise forms.ValidationError("phone number should be number !")
            elif s[0]!='0' or s[1]!='9':
                raise  forms.ValidationError("phone number shold be start with 09 !")
            else:
                return s

    def clean_age(self):
        s=self.cleaned_data['age']
        if s:
            if s<0:
                raise forms.ValidationError("age shode be a positive number !")
            else:
                return s
class contactusform(forms.Form):
    name = forms.CharField(max_length=75,required=True)
    phone = forms.CharField(max_length=11)
    email=forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    message=forms.CharField(widget=forms.Textarea,required=True)


    def clean_phone(self):
        s=self.cleaned_data['phone']
        if s:
            if not s.isnumeric():
                raise forms.ValidationError("phone number should be number !")
            elif s[0]!='0' or s[1]!='9':
                raise  forms.ValidationError("phone number shold be start with 09 !")
            else:
                return s

    def clean_age(self):
        s=self.cleaned_data['age']
        if s:
            if s<0:
                raise forms.ValidationError("age shode be a positive number !")
            else:
                return s

class Shareform(forms.Form):
    name = forms.CharField(max_length=75,required=True)
    to=forms.EmailField(required=True)

class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields=('name','body')