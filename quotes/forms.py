from django.forms import ModelForm, CharField, TextInput, DateInput, ModelMultipleChoiceField, CheckboxSelectMultiple, \
    ModelChoiceField
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        widgets = {
            'fullname': TextInput(attrs={'placeholder': 'Author Full Name'}),
            'born_date': DateInput(attrs={'type': 'date'}),
            'born_location': TextInput(attrs={'placeholder': 'Author Birth Location'}),
            'description': TextInput(attrs={'placeholder': 'Author Description'}),
        }

class QuoteForm(ModelForm):

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple(),
        required=False
    )

    author = ModelChoiceField(
        queryset=Author.objects.all(),
        required=True,
        empty_label="Виберіть автора"
    )