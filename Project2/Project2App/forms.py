from django import forms
from .models import AuthorModel,RelatedModel, WikiPostsModel
from datetime import date

class AuthorForm(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = ["username", "password1", "password2"]


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords DO NOT MATCH!!!!!!!!!!!!!")

class WikiPostsForm(forms.ModelForm):
    class Meta:
        model = WikiPostsModel
        exclude = ["foreignKeyToAuthor"]


    def clean_createdDateTime(self):
        cleanCreatedDateTimeData = self.cleaned_data["createdDateTime"]

        if cleanCreatedDateTimeData == None:
            raise forms.ValidationError("No date was entered")

        if cleanCreatedDateTimeData > date.today():
            raise forms.ValidationError("Future date should not be entered")

        return cleanCreatedDateTimeData

    def clean_lastUpdatedDateTime(self):
        cleanLastUpdatedDateTimeData = self.cleaned_data["lastUpdatedDateTime"]

        if cleanLastUpdatedDateTimeData == None:
            raise forms.ValidationError("No date was entered")

        if cleanLastUpdatedDateTimeData > date.today():
            raise forms.ValidationError("Future date should not be entered")


class RelatedForm(forms.ModelForm):
    class Meta:
        model = RelatedModel
        exclude = ["foreignKeyToWikiPosts"]


    def clean_createdDateTime(self):
        cleanCreatedDateTimeData = self.cleaned_data["createdDateTime"]

        if cleanCreatedDateTimeData == None:
            raise forms.ValidationError("No date was entered")

        if cleanCreatedDateTimeData > date.today():
            raise forms.ValidationError("Future date should not be entered")

        return cleanCreatedDateTimeData

    def clean_lastUpdatedDateTime(self):
        cleanLastUpdatedDateTimeData = self.cleaned_data["lastUpdatedDateTime"]

        if cleanLastUpdatedDateTimeData == None:
            raise forms.ValidationError("No date was entered")

        if cleanLastUpdatedDateTimeData > date.today():
            raise forms.ValidationError("Future date should not be entered")

        return cleanLastUpdatedDateTimeData



