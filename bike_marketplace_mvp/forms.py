from django import forms

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
)

class SearchForm(forms.Form):

    gender = forms.ChoiceField(GENDER_CHOICES, initial='m')
    height_feet = forms.IntegerField(min_value=2, max_value=10, initial=5)
    height_inches = forms.IntegerField(min_value=0, max_value=11, initial=11)
    max_price = forms.IntegerField(min_value=0, initial="500")