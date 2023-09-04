from django import forms
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordResetForm
from .models import Entry, Exercises, Category, NumberTracker, TrackerEntry
from django.contrib.auth import get_user_model
from django.contrib.auth.views import UserModel



DAYS = (
    ('SUN', 'SUN'),
    ('MON', 'MON'),
    ('TUE', 'TUE'),
    ('WED', 'WED'),
    ('THU', 'THU'),
    ('FRI', 'FRI'),
    ('SAT', 'SAT'),
)

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercises
        fields = ('days','name', 'units', )
        days = forms.MultipleChoiceField(
            required=True,
            widget=forms.CheckboxSelectMultiple,
            choices=DAYS,
        )
        widgets = {
            "name": forms.TextInput(attrs={'class': 'pt-20 pb-20 form__row form__input required', 'placeholder':'EXERCISE NAME' }),
            "units": forms.Select(attrs={'class': 'pt-20 pb-20 form__select ', 'placeholder':'UNITS'}),
            "days": forms.CheckboxSelectMultiple(attrs={'class':'checkbox-field--full checkbox-option'})
        }
        labels = {
            'name': 'Exercise Name',
            'units': 'Lbs/Kg',
            'days': 'days',
        }


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('exercise', 'weight', 'reps', 'notes')
        widgets = {
            "exercise": forms.Select(attrs={'class': 'pt-20 pb-20 form__select '}),
            "weight": forms.NumberInput(attrs={'class': ' form__input form__input--12 required', 'placeholder':'WEIGHT'}),
            "reps": forms.NumberInput(attrs={'class': 'd-flex align-items-center justify-space form__input form__input--12 required', 'placeholder':'REPS'}),
            "notes": forms.TextInput(attrs={'class': 'form__input justify-space', 'placeholder':'notes'}),
        }

    def __init__(self, eid=None, *args, **kwargs):
        self.eid = eid
        super(EntryForm, self).__init__(*args, **kwargs)
        self.initial['exercise'] = self.eid




class SetPasswordForm(SetPasswordForm):
    class meta:
         model = get_user_model()
         fields = ['new_password1', 'new_ password2']


class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent_category']
        widgets = {
            "name": forms.TextInput(attrs={'placeholder':'name', 'class':'custom-text-input',}),
            "parent_category": forms.Select(attrs={'class':'custom-select-input'}),
        }

class NumberTrackerForm(forms.ModelForm):
    class Meta:
        model = NumberTracker
        fields = ['name', 'category', 'units']
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'name', 'class': 'custom-text-input', }),
            "category": forms.Select(attrs={'class': 'custom-select-input'}),
            "units": forms.Select(attrs={'class': 'custom-select-input', 'placeholder':'UNITS'}),
        }

class TrackerEntryForm(forms.ModelForm):
    class Meta:
        model = TrackerEntry
        fields = ['weight','rep','number_tracker']
        widgets = {
            "weight": forms.NumberInput(attrs={'placeholder': 'WEIGHT','class':'custom-weight-input',}),
            "rep": forms.NumberInput(attrs={'placeholder': 'REPS', 'class':'custom-rep-input'}),
            "number_tracker": forms.HiddenInput(),
        }