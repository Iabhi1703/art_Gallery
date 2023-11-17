from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField()
    art_genre = forms.CharField(max_length=100)
    booking_date = forms.DateField()
