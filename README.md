django-facebook-social-plugins
==============================
Django wrapper tags on facebook social plugins.

Requirements
------------
- [Django >= 1.5](https://www.djangoproject.com/)

Installation
------------
Install the extension running the setup.py, until i'll not publish on PyPi.

Configuration
-------------
Configure the settings.py like this:
```python
INSTALLED_APPS = (... 'django_fbplugins' ...)
```

Use it
------
As a like button:
```html
{% fb_like_btn_html href="https://www.facebook.com/FacebookDevelopers" %}
```

As a like box:
```html
{% fb_like_box_html href="https://www.facebook.com/FacebookDevelopers" %}
```

Options
-------
You can use various options like this:
```html
{% fb_like_box_html href="https://www.facebook.com/FacebookDevelopers"  colorscheme="dark" showborder="false" header="false" %}
```