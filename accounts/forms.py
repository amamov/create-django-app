from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordChangeForm as AuthPasswordChangeForm,
)
from .models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

    def clean_email(self):
        # model에서 email unique=False인 경우 다음과 같이 유효성 검사를 form단에서 해줄 수 있다.
        email = self.cleaned_data.get("email")
        if email:
            user = User.objects.filter(email=email)
            if user.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")

        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "avatar",
            "email",
            "website_url",
            "bio",
            "phone_number",
            "gender",
        )


class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password2(self):
        old_password = self.cleaned_data.get("old_password", None)
        new_password2 = super().clean_new_password2()
        if old_password == new_password2:
            raise forms.ValidationError("Same as the old password.")
        return new_password2
