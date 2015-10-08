from django import forms

class EmailForm(forms.Form):
	enteredEmail = forms.CharField(label = 'enteredEmail', max_length=100)