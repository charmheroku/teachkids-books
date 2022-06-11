from django import forms
from django.contrib.flatpages.forms import FlatpageForm
from .models import CustomFlatePage, Application


class CustomFlatePageForm(FlatpageForm):
    class Meta:
        model = CustomFlatePage
        fields = "__all__"


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
        labels = {
            "agreement": "AGREE WITH THE PRIVACY POLICY",
        }

    def clean_agreement(self):
        agreement = self.cleaned_data.get("agreement")
        if not agreement:
            raise forms.ValidationError("This field is required")
        return agreement
