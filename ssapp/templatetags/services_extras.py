from django import template
register = template.Library()
@register.inclusion_tag('app/side_bar.html')
def display_sidebar():
	return {'message':'Dashboard'}