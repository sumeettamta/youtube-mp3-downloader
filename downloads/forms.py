from django import forms

class DownloadForm(forms.Form):
    dl = forms.CharField(label='Download Link', max_length=100)