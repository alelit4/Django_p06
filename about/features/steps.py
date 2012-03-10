from lettuce import *
from lxml import html
from nose.tools import assert_equals
from django.test.client import Client

@before.all
def set_browser():
    world.browser = Client()


@step(r'Given Se accede a la url de about "(.*)"')
def accede_url_about(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

    
@step(r'Then Se muestra la cabecera "(.*)"') 
def mostrar_cabecera(step, text):
    header = world.dom.cssselect('h1')[0]
    assert header.text == text
                        
      
      

#from lettuce import *
#from lxml import html
#from django.test.client import Client
#from nose.tools import assert_equals

#@before.all
#def set_browser():
    #world.browser = Client()

#@step(r'I access the url "(.*)"')
#def access_url(step, url):
    #response = world.browser.get(url)
    #world.dom = html.fromstring(response.content)

#@step(r'I see the header "(.*)"')
#def see_header(step, text):
    #header = world.dom.cssselect('h1')[0]
    #assert header.text == text
