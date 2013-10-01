from django import forms

# GENDER_CHOICES = (
#     ('m', 'Male'),
#     ('f', 'Female'),
# )
FRAME_SIZE_CHOICES = (
    ('any', 'Any'),
    ('under_30', 'Under 30'),
    ('30_34', '30 to 34'),
    ('35_40', '35 to 40'),
    ('40_44', '40 to 44'),
    ('45_50', '45 to 50'),
    ('50_54', '50 to 54'),
    ('55_60', '55 to 60'),
    ('over_60', 'Over 60'),
)

class SearchForm(forms.Form):

    # gender = forms.ChoiceField(GENDER_CHOICES, initial='m')
    # height_feet = forms.IntegerField(min_value=2, max_value=10, initial=5)
    # height_inches = forms.IntegerField(min_value=0, max_value=11, initial=11)
    max_price = forms.IntegerField(min_value=0, initial="500", \
        widget=forms.TextInput(attrs={"style": "width: 2em"}))
    frame_size = forms.ChoiceField(FRAME_SIZE_CHOICES, initial='any', \
        widget=forms.Select(attrs={"class": "input-medium"}))

    def clean_frame_size(self):
        """
        :return: (min size, max size)
        """
        frame_sizes = {
            'any': (0, 100),
            'under_30': (0, 30),
            '30_34': (30, 35),
            '35_40': (35, 40),
            '40_44': (40, 45),
            '45_50': (45, 50),
            '50_54': (50, 55),
            '55_60': (55, 60),
            'over_60': (60, 100)
        }
        return frame_sizes[self.cleaned_data['frame_size']]