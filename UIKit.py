from ti_system import *
from ti_draw import *
from time import *

canvas=[]
defaultpen = set_pen("thin","solid")

def init():
  set_window(0,317,0,210)
  set_pen("thin","solid")

def getStringWidth(text):
  len=0
  for i in text:
    len+=7
  return len

def getStringHeight(text):
  return 10

class Color:
  def __init__(self, R, G, B):
    self.R = R
    self.G = G
    self.B = B
  
  def set(self, R, G, B):
    self.R = R
    self.G = G
    self.B = B
    
  def gset(self):
    set_color(self.R,self.G,self.B)
  
  def get(self):
    return self.R,self.G,self.B

class UIElement:
  x=0
  y=0
  width=10
  height=10
  input=False
  def isCursor(self):
    pos=get_mouse()
    xc = pos[0]+3
    yc = 210-pos[1]
    if get_key() == "8":
      print(xc)
      print(self.x+self.width)
    if xc < (self.x+self.width) and xc > self.x and yc > self.y and yc < (self.y+self.height):
      return True
    else:
      if xc < (self.x+self.width) and xc > self.x and yc > self.y and yc < (self.y+self.height):
        return True
      else:
        if xc < (self.x+self.width) and xc > self.x and yc > self.y and yc < (self.y+self.height):
          return True
        else:
          return False
      
  def isClick(self):
    if (self.isCursor() == True and get_key() == "enter"):
      return True

class Label(UIElement):
  def __init__(self, x, y, text):
    self.text = text
    self.x=x
    self.y=y
    self.font = set_pen("thin","solid")
    self.height = getStringHeight(text)
    self.width = getStringWidth(text)
    self.color = Color(0,0,0)
  def setText(self, nt):
    self.text = nt
    self.height = getStringHeight(self.text)
    self.width = getStringWidth(self.text)
    
  def getText(self):
    return self.text
    
  def render(self):
    self.color.gset()
    draw_text(self.x,self.y,self.text)
    set_color(0,0,0)

class Button(UIElement):
  def __init__(self, x, y, width, height, text, onClick, arg):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
    self.onClick = onClick
    self.arg = arg
    self.callback = "You are trying to access the callback before it has been set; why?"
    self.bdcolor = Color(0,0,0)
    self.txcolor = Color(0,0,0)

  def setText(self, text):
    self.text = text

  def getText(self):
    return self.text

  def getSize(self):
    size = self.width, self.height
    return size

  def setSize(self, width, height):
    self.width = width
    self.height = height

  def render(self):
    if self.isClick() == True:
      if self.onClick != None:
        if self.arg != None:
          self.callback = self.onClick(self.arg)
        else:
          self.callback = self.onClick()
      #not needed
      #self.ccolor.gset()
      #fill_rect(self.x,self.y,self.width,self.height)
      self.bdcolor.gset()
    
    
    draw_rect(self.x,self.y,self.width,self.height)
    self.txcolor.gset()
    draw_text(self.x+3,self.y+self.height/10,self.text)
    set_color(0,0,0)

class Textbox(UIElement):
  CL = -1
  edit = False
  def __init__(self, x, y, width, height, text, isreadonly):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
    self.readonly = isreadonly
    self.DCL = True

  def __init__(self, x, y, width, height, text, isreadonly, DCL):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
    self.readonly = isreadonly
    self.DCL = DCL

  def setText(self, text):
    if self.DCL == True:
      while True:
        if getStringWidth(text) > self.width:
          text = text[:len(text)-1]
        else:
          self.text = text
          break
    elif self.CL != -1:
      while True:
        if len(text) > self.Cl:
          text = text[:len(text)-1]
        else:
          self.text = text
          break
    else:
      self.text = text

  def getText(self):
    return self.text

  def getSize(self):
    size = self.width, self.height
    return size

  def setSize(self, width, height):
    self.width = width
    self.height = height

  def render(self):
    if get_key() == "enter":
      self.edit = True
    if self.readonly == False and self.isCursor() and self.edit == True:
      set_color(210,210,210)
      fill_rect(self.x,self.y,self.width,self.height)
      key=str(get_key(1))
      if key == "del":
        self.setText(self.text[:len(self.text)-1])
      elif key == "esc":
        self.edit = False
      elif key != "esc":
        self.setText(self.text+key)
    else:
      set_color(160,160,160)
      fill_rect(self.x,self.y,self.width,self.height)
    set_color(0,0,0)
    draw_rect(self.x,self.y,self.width,self.height)
    draw_text(self.x+3,self.y+self.height/10,self.text)
