"""
Created on 16/giu/2013

@author: Marco Pompili
"""

from django import template
from django.utils.translation import get_language

register = template.Library()

langs = {
    "it": "it_IT",
    "en": "en_US",
    "de": "de_DE"
}


def fb_like_btn(href, **kwargs):
    """
        Reproduce a W3C compliant facebook Like button.
        Check the social plugin page for more infos:
            https://developers.facebook.com/docs/reference/plugins/like/
        
        Usage::
        
            {% fb_like_btn_html "<page-url>" %}
        
        Example::
        
            {% fb_like_btn_html "https://www.facebook.com/FacebookDevelopers" %}
    
    """

    return {
        'lang': langs[get_language()],
        'href': href,
        'layout': kwargs.get('layout', 'standard'),
        'colorscheme': kwargs.get('colorscheme', 'light'),
        'action': kwargs.get('action', 'like'),
        'showfaces': kwargs.get('showfaces', 'true'),
        'share': kwargs.get('share', 'true'),
        'height': kwargs.get('height', '80'),
        'scrolling': kwargs.get('scrolling', 'no'),
        'frameborder': kwargs.get('frameborder', '0'),
        'allowTransparency': kwargs.get('allowTransparency', 'true')
    }


register.inclusion_tag('django_fbplugins/btn/iframe.html', name='fb_like_btn_iframe')(fb_like_btn)
register.inclusion_tag('django_fbplugins/btn/html5.html', name='fb_like_btn_html')(fb_like_btn)


def fb_like_box(href, **kwargs):
    """
        Reproduce a W3C compliant facebook Like box.
        Check the social plugin page for more infos:
            https://developers.facebook.com/docs/reference/plugins/like-box/
        
        Usage::
        
            {% fb_like_box_html "<page-url>" %}
            
        Example::
        
            {% fb_like_box_html "https://www.facebook.com/FacebookDevelopers" %}
            
    """

    return {
        'lang': langs[get_language()],
        'href': href,
        'height': kwargs.get('height', '290'),
        'colorscheme': kwargs.get('colorscheme', 'light'),
        'showfaces': kwargs.get('showfaces', 'true'),
        'header': kwargs.get('header', 'true'),
        'stream': kwargs.get('stream', 'false'),
        'showborder': kwargs.get('showborder', 'true'),
        'scrolling': kwargs.get('scrolling', 'no'),
        'frameborder': kwargs.get('frameborder', '0'),
        'allowTransparency': kwargs.get('allowTransparency', 'true')
    }


register.inclusion_tag('django_fbplugins/box/iframe.html', name='fb_like_box_iframe')(fb_like_box)
register.inclusion_tag('django_fbplugins/box/html5.html', name='fb_like_box_html')(fb_like_box)


@register.inclusion_tag('django_fbplugins/box/feed.html')
def fb_feed_box(href, **kwargs):
    return {
        'lang': langs[get_language()],
        'href': href,
        'action': kwargs.get('action', 'likes, recommends'),
        'colorscheme': kwargs.get('colorscheme', 'light'),
        'header': kwargs.get('header', 'true')
    }