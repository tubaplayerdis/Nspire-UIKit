from ti_system import *
from ti_draw import *
from time import *
from random import *

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
  return 8
  
def draw_arrow(x1,y1,x2,y2,vx,vy):
  draw_line(x1,y1,vx,vy)
  draw_line(x2,y2,vx,vy)
  
def isNumber(key):
  if key == "1":
    return True
  elif key == "3":
    return True
  elif key == "4":
    return True
  elif key == "5":
    return True
  elif key == "6":
    return True
  elif key == "7":
    return True
  elif key == "8":
    return True
  elif key == "9":
    return True

def getColor(color):
  if color == "red":
    return Color(178,31,53)
  elif color == "redorange":
    return Color(216,39,53)
  elif color == "orange":
    return Color(255,116,53)
  elif color == "orangeyellow":
    return Color(255,161,53)
  elif color == "yellow":
    return Color(255,240,53)
  elif color == "darkgreen":
    return Color(0,117,58)
  elif color == "green":
    return Color(0,158,71)
  elif color == "lightgreen":
    return Color(22,221,53)
  elif color == "darkblue":
    return Color(0,82,165)
  elif color == "blue":
    return Color(0,121,252)
  elif color == "lightblue":
    return Color(0,169,252)
  elif color == "cyan":
    return Color(0,255,255)
  elif color == "violet":
    return Color(104,30,126)
  elif color == "purple":
    return Color(125,60,181)
  elif color == "lightpurple":
    return Color(189,122,246)
  elif color == "underwearcrust":
    return Color(169,104,64)
  elif color == "brown":
    return Color(183,97,39)
  elif color == "lightbrown":
    return Color(210,138,90)
  elif color == "darkbrown":
    return Color(95,44,10)
  elif color == "black":
    return Color(0,0,0)
  elif color == "white":
    return Color(255,255,255)
  elif color == "gold":
    return Color(160,160,60)
  elif color == "gray":
    return Color(160,160,160)
  elif color == "lightgray":
    return Color(211,211,211)
  elif color == "darkgray":
    return Color(105,105,105)

class Color:
  def __init__(self, R, G, B):
    self.R = R
    self.G = G
    self.B = B
  
  def set(self, color):
    nc = getColor(color)
    self.R = nc.R
    self.G = nc.G
    self.B = nc.B
  def mset(self, R, G, B):
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
    if get_key() == "enter":
      if self.isCursor() == True:
        return True
    return False

class Label(UIElement):
  def __init__(self, x, y, text):
    self.text = text
    self.x=x
    self.y=y
    self.font = set_pen("thin","solid")
    self.height = 20
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
    self.bgcolor = Color(140,140,140)

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
      #self.ccolor.gset()
      #fill_rect(self.x,self.y,self.width,self.height)
    self.bgcolor.gset()
    fill_rect(self.x,self.y,self.width,self.height)
    self.bdcolor.gset()
    draw_rect(self.x,self.y,self.width,self.height)
    self.txcolor.gset()
    draw_text(self.x+3,self.y+self.height/10,self.text)
    set_color(0,0,0)

class Textbox(UIElement):
  CL = -1
  edit = False
  def __init__(self, x, y, width, height, text, isreadonly, DCL):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
    self.readonly = isreadonly
    self.DCL = DCL
    self.bdcolor = Color(0,0,0)
    self.txcolor = Color(0,0,0)
    self.ndcolor = Color(160,160,160)
    self.edcolor = Color(210,210,210)
    self.numMode = False

  def setNumMode(self, toggle):
    self.numMode = toggle

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
      self.edcolor.gset()
      fill_rect(self.x,self.y,self.width,self.height)
      key=str(get_key(1))
      if key == "del":
        self.setText(self.text[:len(self.text)-1])
      if get_platform() == "hh":
        if key == "esc":
          self.edit = False
        elif key != "del":
          if self.numMode:
            if isNumber(key):
              self.setText(self.text+key)
          else:
            self.setText(self.text+key)
      else:
        if key == "up":
          self.edit = False
        elif key != "del":
          if self.numMode:
            if isNumber(key):
              self.setText(self.text+key)
          else:
            self.setText(self.text+key)
    else:
      self.ndcolor.gset()
      fill_rect(self.x,self.y,self.width,self.height)
    self.bdcolor.gset()
    draw_rect(self.x,self.y,self.width,self.height)
    self.txcolor.gset()
    draw_text(self.x+3,self.y+self.height/10,self.text)
    set_color(0,0,0)
    

class Dropdown(UIElement):
  def __init__(self, x, y, width, height, text, collapsable):
    self.x=x
    self.y=y
    self.width = width
    self.height = height
    self.text = text
    self.collapsable = collapsable
    self.items = []
    self.collapsed = True
    self.buffer = 5
    self.txcolor = Color(0,0,0)
    self.bdcolor = Color(0,0,0)
    self.bgcolor = Color(160,160,160)
    self.btcolor = Color(0,0,0)
  def addElement(self,element):
    self.items.append(element)
  
  def removeElement(self,index):
    self.items.pop(index)
  
  def removeAll(self):
    self.items.clear()
    
  def render(self):
    if self.isClick():
      self.collapsed = not self.collapsed
    self.bgcolor.gset()
    fill_rect(self.x,self.y,self.width,self.height)
    self.bdcolor.gset()
    draw_rect(self.x,self.y,self.width,self.height)
    #fill_circle(self.x+10,self.y+(self.height/2),5)
    self.txcolor.gset()
    draw_text(self.x+20,self.y+(self.height/5),self.text)
    if self.collapsed == False:
      self.btcolor.gset()
      draw_arrow(self.x+5,self.y+(self.height/1.5),self.x+15,self.y+(self.height/1.5),self.x+10,self.y+(self.height/3))
      space = 0
      enumeration = 0
      if len(self.items) != 0:
        for item in self.items:
          item.x = self.x+5
          addto = 5
          for i in range(0,enumeration):
            addto += self.items[i].height
            addto += self.buffer
          space += (item.height+self.buffer)
          item.y = self.y-(self.height/2+addto+self.buffer)
          enumeration=enumeration+1
        self.bgcolor.gset()
        fill_rect(self.x+1,self.y-space,self.width-1,space+1)
        set_color(0,0,0)
        for item in self.items:
          item.render()
    else:
      self.btcolor.gset()
      draw_arrow(self.x+5,self.y+(self.height/3),self.x+15,self.y+(self.height/3),self.x+10,self.y+(self.height/1.5))
      set_color(0,0,0)
      
class TButton(UIElement):
  def __init__(self, x, y, width, height, text, onClick, arg):
    self.x=x
    self.y=y
    self.width = width
    self.height = height
    self.text = text
    self.readonly = False
    self.toggle = False
    self.bdcolor = Color(0,0,0)
    self.oncolor = Color(160,160,160)
    self.ofcolor = Color(0,0,0)
    self.txcolor = Color(0,0,0)
    self.bgcolor = Color(140,140,140)
    self.onClick = onClick
    self.arg = arg
    self.callback = "You are trying to access the callback before it has been set; why?"

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
    if self.isClick():
      if self.onClick != None:
        if self.arg != None:
          self.callback = self.onClick(self.arg)
        else:
          self.callback = self.onClick()
      self.toggle = not self.toggle
    
    self.bgcolor.gset()
    fill_rect(self.x,self.y,self.width,self.height)

    if self.toggle == True:
      self.oncolor.gset()
    else:
      self.ofcolor.gset()

    fill_circle(self.x+(self.height/2), self.y+(self.height/2), self.height/3)
    self.bdcolor.gset()
    draw_rect(self.x,self.y,self.width,self.height)
    self.txcolor.gset()
    draw_text(self.x+self.height,self.y+(self.height/2)-7,self.text)
    set_color(0,0,0)  

class Panel(UIElement):
  def __init__(self,x,y,width,height,isRender):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = Color(55,55,55)
    self.bdcolor = Color(0,0,0)
    self.items = []
    self.hasBorder = False
    self.isRender = isRender
  
  def addElement(self,element):
    element.x = self.x+element.x
    element.y = self.y+element.y
    self.items.append(element)
  
  def removeElement(self,index):
    self.items.pop(index)
  
  def removeAll(self):
    self.items.clear()
    
  def toggleRender(self):
    self.isRender = not self.isRender
  
  def setRender(self, state):
    self.isRender = state
    
  def render(self):
    if self.isRender == True:
      self.color.gset()
      fill_rect(self.x,self.y,self.width,self.height)
      if self.hasBorder == True:
        self.bdcolor.gset()
        draw_rect(self.x,self.y,self.width,self.height)
      for item in self.items:
        item.render()

class Slider(UIElement):
  def __init__(self,x,y,width,height):
    self.x = x
    self.y = y
    self.width = width
    sellf.height = height

class Colorpicker(UIElement):
  def __init__(self,x,y,color,func,arg):
    self.x = x
    self.y = y
    self.width = 120
    self.height = 105
    self.crcolor = color
    self.items = []
    self.bgcolor = Color(105,105,105)
    self.bdcolor = Color(255,255,255)
    self.isopen = False
    self.func = func
    self.arg = arg
    #the items
    self.ranbt = Button(5,5,50,20,"random",self.rancol,None)
    self.setbt = Button(65,5,50,20,"select",self.selcol,None)
    self.rbox = Textbox(65,80,50,20,str(color.R),False,False)
    self.gbox = Textbox(65,55,50,20,str(color.G),False,False)
    self.bbox = Textbox(65,30,50,20,str(color.B),False,False)
    self.rlab = Label(58,85,"r")
    self.glab = Label(58,60,"g")
    self.blab = Label(58,35,"b")
    self.items.append(self.ranbt)
    self.items.append(self.setbt)
    self.items.append(self.rbox)
    self.items.append(self.gbox)
    self.items.append(self.bbox)
    self.items.append(self.rlab)
    self.items.append(self.glab)
    self.items.append(self.blab)
    self.items[2].setNumMode(True)
    self.items[3].setNumMode(True)
    self.items[4].setNumMode(True)
    for item in self.items:
      item.x = self.x + item.x
      item.y = self.y + item.y
  def rancol(self):
    self.rbox.setText(str(randint(0,255)))
    self.gbox.setText(str(randint(0,255)))
    self.bbox.setText(str(randint(0,255)))
  
  def selcol(self):
    if self.func != None:
      if self.arg != None:
        self.func(self.arg)
      else:
        self.func()
    self.isopen = False
  def upcol(self):
    r=0
    g=0
    b=0
    if self.rbox.text != "":
      r = int(self.rbox.getText())
    if self.gbox.text != "":
      g = int(self.gbox.getText())
    if self.bbox.text != "":
      b = int(self.bbox.getText())
    self.crcolor.mset(r,g,b)
  
  def getColor(self):
    return self.crcolor
  
  def render(self):
    if self.isopen == True:
      self.bgcolor.gset()
      fill_rect(self.x,self.y,self.width,self.height)
      self.upcol()
      self.crcolor.gset()
      fill_rect(self.x+5,self.y+30,45,70)
      for item in self.items:
        item.render()
