from django import template

# Create a template library instance
register = template.Library()


def tags(quote_tags):
    """
    A custom template filter to display tags associated with a quote.

    Args:
        quote_tags: A queryset of Tag objects associated with a quote.

    Returns:
        A string containing comma-separated names of the tags.
    """
    return ', '.join([str(name) for name in quote_tags.all()])


register.filter('tags', tags)
