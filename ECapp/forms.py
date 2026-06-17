from django import forms
from ECapp.models import AccountUser

class RegisterUser1Form(forms.Form):

    user_id = forms.CharField(label="会員ID",max_length=128)
    password= forms.CharField(label="パスワード",max_length=256)
    password2= forms.CharField(label="確認用パスワード",max_length=256)
    name = forms.CharField(label="お名前",max_length=128)
    address = forms.CharField(label="住所",max_length=256)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("パスワードと確認用パスワードが一致しません")
        
    def clean_user_id(self):
        value = self.cleaned_data["user_id"]
        if AccountUser.objects.filter(user_id = value).exists():
            raise forms.ValidationError("このユーザーIDは既に使用されています。")

        return value



class RegisterUserForm(forms.Form):

    user_id = forms.CharField(label="会員ID",max_length=128)
    password= forms.CharField(label="パスワード",max_length=256)
    password2= forms.CharField(label="確認用パスワード",max_length=256)
    name = forms.CharField(label="お名前",max_length=128)
    address = forms.CharField(label="住所",max_length=256)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("パスワードと確認用パスワードが一致しません")
        



    

class LoginForm(forms.Form):

    user_id = forms.CharField(label="会員ID",max_length=128)
    password= forms.CharField(label="パスワード",max_length=256)


