from django import template

register = template.Library()

@register.filter
def change_status(text):
    if text == 'a':
        text = 'ongoing'
    if text == 'b':
        text = 'completed'
    if text == 'c':
        text = 'stalled'
    return text

@register.filter
def color(text):
    if text == 'a':
        text = 2
    if text == 'b':
        text = 1
    if text == 'c':
        text = 3
    return text