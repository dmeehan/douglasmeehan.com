from django.template import Library, Node
from actionmanual.maestro.models import Category, CategoryItem

register = Library()

class CategoriesForObjectNode(Node):
    def __init__(self, obj, context_var):
        self.obj = Variable(obj)
        self.context_var = context_var

    def render(self, context):
        context[self.context_var] = \
            Category.objects.get_for_object(self.obj.resolve(context))
        return ''
        
def do_categories_for_object(parser, token):
    """
    Retrieves a list of ``Category`` objects associated with an object and
    stores them in a context variable.

    Usage::

       {% categories_for_object [object] as [varname] %}

    Example::

        {% categories_for_object foo_object as category_list %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError(_('%s tag requires exactly three arguments') % bits[0])
    if bits[2] != 'as':
        raise TemplateSyntaxError(_("second argument to %s tag must be 'as'") % bits[0])
    return TagsForObjectNode(bits[1], bits[3])


def get_category_items(parser, token):
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError, "get_latest tag takes exactly three arguments"
    if bits[2] != 'as':
        raise TemplateSyntaxError, "third argument to get_category_item tag must be 'as'"
    return CategoryItemsNode(bits[1], bits[3])
    

register.tag('get_category_items', get_category_items)
register.tag('categories_for_object', do_categories_for_object)