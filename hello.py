import kivy
kivy.require('1.7.0')
import bottle
import threading

from bottle import template
from kivy.app import App
from kivy.base import *
from kivy.uix.label import *
from kivy.uix.stacklayout import *

@bottle.route("/hello")
def hello():
  return 'Hello world!'

@bottle.route("/ui")
def ui():
  ui = get_widget_json(EventLoop.window)
  print ui
  return ui

def get_widget_json(widget):
  widget_id = ''
  if hasattr(widget, 'id'):
    widget_id = widget.id 

  value  = ''
  if hasattr(widget, 'text'):
    value = widget.text

  widget_json = {'type':widget.__class__.__name__, 'id':widget_id , 'value':value}

  for child in widget.children:
    children_json = []
    children_json.append(get_widget_json(child))
    widget_json['children'] = children_json

  return widget_json


class HelloApp(App):

  def build(self):
    thread = threading.Thread(target=bottle.run, kwargs={'host':'localhost', 'port':5000})
    thread.setDaemon(True)
    thread.start()

    label = Label(text='Hello, world!', id='mylabel')
    stack_layout = StackLayout(id='rootstacklayout')
    stack_layout.add_widget(label)
    return stack_layout

if __name__=="__main__":
  HelloApp().run()


