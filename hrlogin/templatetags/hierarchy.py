from django import template

register = template.Library()

def assitant(obj):
    string = ''
    childs = obj.children.all()
    if childs.count() == 0:
        string = '<li>{}</li>'.format(obj)
    else:
        string += hierarchy(obj)

    return string


@register.filter
def hierarchy(unit):
    childs = unit.children.all()
    if childs.count() == 0:
        string = '<li>{}</li>'.format(unit)
    else:
        string = '<li>{}<ul>'.format(unit)
        for child in childs:
            string += assitant(child)
        string += '</ul></li>'
    return string