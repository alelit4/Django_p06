from lettuce import *
from lxml import html
from nose.tools import assert_equals
from django.test.client import Client

@before.all
def set_browser():
    world.browser = Client()


@step(r'Given Se accede a la url de home "(.*)"')
def accede_url_home(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

    
@step(r'Then Se muestra la cabecera "(.*)"') 
def mostrar_cabecera(step, text):
    header = world.dom.cssselect('h1')[0]
    assert header.text == text
                        
