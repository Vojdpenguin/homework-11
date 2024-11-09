from django import template

from ..models import Author

register = template.Library()


def get_author(id_):
    try:
        author = Author.objects.get(id=id_)
        return author.fullname
    except Author.DoesNotExist:
        return "Unknown Author"


register.filter('author', get_author)