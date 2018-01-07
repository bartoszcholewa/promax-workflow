from django import forms

class JoinForm(forms.Form):
	url = forms.URLField(label='URL', widget=forms.TextInput(attrs={'placeholder': 'https://picturewall.pl/...'}))

	