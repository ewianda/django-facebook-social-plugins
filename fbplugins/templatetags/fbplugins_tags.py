'''
Created on 16/giu/2013

@author: Marco Pompili
'''

import hashlib
from django import template
from django.utils.translation import get_language

register = template.Library()


class UrlBasedPlugin(template.Node):
    """
        Base class for the social plugins nodes.
        Has some basic attributes and generates with MD5
        the id where to append the facebook widget.
    """
    def __init__(self, attributes):
        self.href = attributes.get('data-href')
        self.id = hashlib.md5(self.href).hexdigest()
        self.langs = { 
                        "it" : "it_IT",
                        "en" : "en_US",
                        "de" : "de_DE" 
                      }
    
    def set_js_attr(self, name, value):
        """
           Sets an attribute using javascript.
           
           Keyword arguments:
            name -- the name of the attribute
            value -- the attribute's value
            
        """
        return 'fb.setAttribute("{}","{}");'.format(name, value)


class BoxPlugin(UrlBasedPlugin):
    """
        The class for the Like box and the Like button.
        Has the basic html and javascript for rendering
        the social plugins. 
    """
    def __init__(self, attributes):
        super(BoxPlugin, self).__init__(attributes)
        
        self.html = [
                       '<div id="fb-root"></div>',
                       '<script>(function(d, s, id) {',
                       'var js, fjs = d.getElementsByTagName(s)[0];',
                       'if (d.getElementById(id)) return;',
                       'js = d.createElement(s); js.id = id;',
                       'js.src = "//connect.facebook.net/'+ self.langs[get_language()] +'/all.js#xfbml=1";',
                       'fjs.parentNode.insertBefore(js, fjs);}',
                       '(document, "script", "facebook-jssdk"));</script>',
                       '<div id="' + self.id + '"></div>',
                       '<script type="text/javascript">',
                       'var fb = document.createElement("div");'
                       ]
        
        self.html.extend([ self.set_js_attr(k,v) for k, v in attributes.iteritems() if v is not False ])
        self.html.extend([ 'document.getElementById("' + self.id + '").appendChild(fb);</script>' ])
        
    def render(self, context):
        return ''.join([ l for l in self.html ])

def parse_args(args):
    """
        Parse a list of strings from the django token contents
    
        Keyword arguments:
            args -- list of arguments
    """
    return { key : value for key, value in (arg.split('=') for arg in args[1:]) }

@register.tag
def facebook_like_button(parser, token):
    """
        Reproduce a W3C compliant facebook Like button.
        Check the social plugin page for more infos:
            https://developers.facebook.com/docs/reference/plugins/like/
        
        Usage::
        
            {% facebook_like_button data-href=<page-url> %}
        
        Example::
        
            {% facebook_like_button data-href=https://www.facebook.com/FacebookDevelopers %}
    
    """
    args = token.contents.split();
    
    if len(args) < 2:
        raise template.TemplateSyntaxError('%s tag requires the href attribute at least' % args[0])
    else:
        params = parse_args(args)
        
        attributes = { 'data-href' : params.get('href') }

        attributes['class'] = 'fb-like'
        attributes['data-send'] = params.get('send_btn', 'true')
        attributes['data-layout'] = params.get('layout', False)
        attributes['data-width'] = params.get('width', '450')
        attributes['data-show-faces'] = params.get('show_faces', 'true')
        attributes['data-colorscheme'] = params.get('color_scheme', False)
        attributes['font'] = params.get('font', False)
        
        return BoxPlugin(attributes)

@register.tag
def facebook_like_box(parser, token):
    """
        Reproduce a W3C compliant facebook Like box.
        Check the social plugin page for more infos:
            https://developers.facebook.com/docs/reference/plugins/like-box/
        
        Usage::
        
            {% facebook_like_box data-href=<page-url> %}
            
        Example::
        
            {% facebook_like_box data-href=https://www.facebook.com/FacebookDevelopers %}
            
    """
    args = token.contents.split();
    
    if len(args) < 2:
        raise template.TemplateSyntaxError('%s tag requires the href attribute at least' % args[0])
    else:
        params = parse_args(args)
        
        attributes = { 'data-href' : params.get('href') }
        
        attributes['class'] = 'fb-like-box'
        attributes['data-width'] = params.get('width', False)
        attributes['data-height'] = params.get('height', False)
        attributes['data-colorscheme'] = params.get('color_scheme', False)
        attributes['data-show-faces'] = params.get('show_faces', 'true')
        attributes['data-stream'] = params.get('data_stream', 'false')
        attributes['data-show-border'] = params.get('show_border', 'false')
        attributes['data-header'] = params.get('show_header', 'false')
        
        return BoxPlugin(attributes)