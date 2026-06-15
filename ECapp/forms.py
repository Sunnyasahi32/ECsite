from django import forms

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

    def clean_mail(self):
        value = self.cleaned_data["user_id"]
        return value
    
    def clean_password(self):
        value = self.cleaned_data["password"]
        return value

