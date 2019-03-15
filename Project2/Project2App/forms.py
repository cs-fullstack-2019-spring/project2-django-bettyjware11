from django import forms
from .models import UserModel, RelatedModel, WikiPostsModel
from datetime import date

class WikiPostsForm(forms.ModelForm):
    class Meta:
        model = WikiPostsModel
        exclude = ["foreignKeyToUser"]



class RelatedForm(forms.ModelForm):
    class Meta:
        model = RelatedModel
        exclude = ["foreignKeyToUser"]



class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["username", "password1", "password2", "email"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords DO NOT MATCH!!!!!!!!!!!!!")
