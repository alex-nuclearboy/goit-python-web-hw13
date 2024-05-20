from django.db import models


class Tag(models.Model):
    """Represents a tag for categorizing quotes.

    Attributes:
        name (CharField): The name of the tag, must be unique.
        created_at (DateTimeField): The date and time the tag was created,
                                    automatically set to the current time
                                    when the tag is created.
    """
    name = models.CharField(max_length=50, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    """Represents an author of the quote.

    Attributes:
        fullname (CharField): The full name of the author, must be unique.
        birth_date (DateField): The birth date of the author.
        birth_location (CharField): The birth location of the author.
        description (TextField): An optional description of the author.
        created_at (DateTimeField): The date and time the author was created,
                                    automatically set to the current time
                                    when the author is created.
    """
    fullname = models.CharField(max_length=70, null=False, unique=True)
    birth_date = models.DateField(null=False)
    birth_location = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    """Represents a quote.

    Attributes:
        quote (TextField): The text of the quote.
        author (ForeignKey): A reference to the Author of the quote,
                             establishing a many-to-one relationship.
        tags (ManyToManyField): A set of Tags associated with the quote,
                                establishing a many-to-many relationship.
        created_at (DateTimeField): The date and time the quote was created,
                                    automatically set to the current time
                                    when the quote is created.
    """
    quote = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quote} by {self.author}"
