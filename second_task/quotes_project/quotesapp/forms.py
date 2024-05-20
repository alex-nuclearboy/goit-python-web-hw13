from django.forms import (
    ModelForm,
    CharField,
    DateField,
    TextInput,
    ModelChoiceField,
    ModelMultipleChoiceField,
    SelectMultiple
)
from .models import Tag, Author, Quote


class TagForm(ModelForm):
    """Form for creating and updating Tag instances.

    Attributes:
        name (CharField): Field for the tag name.
    """
    name = CharField(
        min_length=3, max_length=25, required=True, widget=TextInput()
    )

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    """Form for creating and updating Author instances.

    Attributes:
        fullname (CharField): Full name of the author.
        birth_date (DateField): Birth date of the author.
        birth_location (CharField): Birth location of the author.
        description (CharField): A description field for additional
                                 information about the author.
    """
    fullname = CharField(
        min_length=3, max_length=70, required=True, widget=TextInput()
    )
    birth_date = DateField()
    birth_location = CharField(
        min_length=5, max_length=150, required=True, widget=TextInput()
    )
    description = CharField()

    class Meta:
        model = Author
        fields = ['fullname', 'birth_date', 'birth_location', 'description']


class QuoteForm(ModelForm):
    """Form for creating and updating Quote instances.

    Attributes:
        tags (ModelMultipleChoiceField): Multiple choice field for selecting
                                         tags associated with the quote.
        quote (CharField): The quote text.
        author (ModelChoiceField): Dropdown for selecting the author
                                   of the quote.
    """
    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required=False, widget=SelectMultiple()
    )
    quote = CharField(
        min_length=3, max_length=255, required=True, widget=TextInput()
    )
    author = ModelChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Quote
        fields = ["quote", "author", 'tags']
