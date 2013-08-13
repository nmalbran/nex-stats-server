from django import forms


class LogForm(forms.Form):
    log = forms.FileField()