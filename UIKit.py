from ti_system import *
from ti_draw import *
from time import *
import random as Random

canvas=[]
defaultpen = set_pen("thin","solid")


def init():
  set_window(0,317,0,210)
  set_pen("thin","solid")

def getStringWidth(text: str)->int:
  len=0
  for i in text:
    len+=8
  return len

def getStringHeight(text: str)->int:
  return 8
  
def draw_arrow(x1,y1,x2,y2,vx,vy):
  draw_line(x1,y1,vx,vy)
  draw_line(x2,y2,vx,vy)
  
def isNumber(key: str)->bool:
  if key == "0":
    return True
  elif key == "1":
    return True
  elif key == "2":
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
  
def WrapText(text: str, max_width: int):
  lines = []
  current_line = ''
  current_width = 0

  for char in text:
      if char == ' ':
          if current_width < max_width:
              if current_line:
                  current_line += ' '
              current_width += 1
          else:
              lines.append(current_line)
              current_line = ''
              current_width = 0
      else:
          current_line += char
          current_width += 1
          if current_width >= max_width:
              lines.append(current_line)
              current_line = ''
              current_width = 0

  if current_line:
      lines.append(current_line)

  return lines

def WrapText_D(text: str, width: int):
  lines = []
  og=text
  line = text
  i = 0
  b=0
  while True:
    for char in text:
      line = line+char
      i=i+1
      if getStringWidth(line) >= width-1:
        #print(line)
        lines.append(line)
        line = ""
        text = text[i:]
        if i == len(text):
          #print("Making new line")
          break
        else:
          i=0
      #print("B is: "+str(b))
      b=b+1 
        
    if b>=len(og)-1: 
      lines.pop(0)
      lines[0]=og[0]+lines[0]
      return lines

class Listener():
  def __init__(self, funcref: function):
    self.funcref = funcref
  def call(self, args):
    self.funcref(args)

class Event():
  def __init__(self):
    self.listeners = []
  
  def addListener(self, listener: Listener):
    self.listeners.append(listener)
  
  def removeListener(self, index: int):
    self.listeners.pop(index)
    
  def removeAll(self):
    self.listeners = []
    
  def InvokeListeners(self, ref):
    for listen in self.listeners:
      listen.call(ref)

class Color:
  def __init__(self, R: int, G: int, B: int):
    self.R = R
    self.G = G
    self.B = B
  
  def set(self, color: str):
    nc = getColor(color)
    self.R = nc.R
    self.G = nc.G
    self.B = nc.B
  def mset(self, R: int, G: int, B: int):
    self.R = R
    self.G = G
    self.B = B
    
  def gset(self):
    set_color(self.R,self.G,self.B)
  
  def get(self)->tuple:
    return self.R,self.G,self.B
  
def getColor(color: str)->Color:
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

class UIElement:
  x=0
  y=0
  width=100
  height=20
  input=False
  cursorEvent = Event()
  clickEvent = Event()
  def isCursor(self)->bool:
    pos=get_mouse()
    xc = pos[0]+3
    yc = 210-pos[1]
    if xc < (self.x+self.width) and xc > self.x and yc > self.y and yc < (self.y+self.height):
      return True
    else:
      if xc < (self.x+self.width) and xc > self.x and yc > self.y and yc < (self.y+self.height):
        self.cursorEvent.InvokeListeners(self)
        return True
      else:
        if xc < (self.x+self.width) and xc > self.x and yc > self.y and yc < (self.y+self.height):
          self.cursorEvent.InvokeListeners(self)
          return True
        else:
          return False
      
  def isClick(self)->bool:
    if get_key() == "enter":
      if self.isCursor() == True:
        self.clickEvent.InvokeListeners(self)
        return True
    return False

class Label(UIElement):
  def __init__(self, x: int, y: int, text:str):
    self.text = text
    self.x=x
    self.y=y
    self.font = set_pen("thin","solid")
    self.height = 20
    self.width = getStringWidth(text)
    self.color = Color(0,0,0)
  def setText(self, nt: str):
    self.text = nt
    self.width = getStringWidth(self.text)
    
  def getText(self):
    return self.text
    
  def render(self):
    self.color.gset()
    draw_text(self.x,self.y,self.text)
    set_color(0,0,0)

class Button(UIElement):
  def __init__(self, x: int, y: int, width: int, height: int, text: str, onClick: function, arg: any):
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
    self.onClickEvent = Event()

  def setText(self, text: str):
    self.text = text

  def getText(self)->str:
    return self.text

  def getSize(self)->tuple:
    size = self.width, self.height
    return size

  def setSize(self, width: int, height: int):
    self.width = width
    self.height = height

  def render(self):
    if self.isClick() == True:
      if self.onClick != None:
        if self.arg != None:
          self.callback = self.onClick(self.arg)
        else:
          self.callback = self.onClick()
        self.onClickEvent.InvokeListeners(self)
      #self.ccolor.gset()
      #fill_rect(self.x,self.y,self.width,self.height)
    self.bgcolor.gset()
    fill_rect(self.x,self.y,self.width,self.height)
    self.bdcolor.gset()
    draw_rect(self.x,self.y,self.width,self.height)
    self.txcolor.gset()
    draw_text(self.x+3,self.y+(self.height/10),self.text)
    set_color(0,0,0)

class Textbox(UIElement):
  def __init__(self, x: int, y: int, width: int, height: int, text: str, isreadonly: bool, DCL: bool):
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
    self.CL = -1
    self.edit = False

  def setNumMode(self, toggle: bool):
    self.numMode = toggle

  def setText(self, text: str):
    if self.DCL == True:
      while True:
        if getStringWidth(text) > self.width:
          text = text[:len(text)-1]
        else:
          self.text = text
          break
    elif self.CL != -1:
      while True:
        if len(text) > self.CL:
          text = text[:len(text)-1]
        else:
          self.text = text
          break
    else:
      self.text = text

  def getText(self)->str:
    return self.text

  def getSize(self)->tuple:
    size = self.width, self.height
    return size

  def setSize(self, width: int, height: int):
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
  def __init__(self, x: int, y: int, width: int, height: int, text:str, iscollapsable: bool):
    self.x=x
    self.y=y
    self.width = width
    self.height = height
    self.text = text
    self.collapsable = iscollapsable
    self.items = []
    self.collapsed = True
    self.buffer = 5
    self.txcolor = Color(0,0,0)
    self.bdcolor = Color(0,0,0)
    self.bgcolor = Color(160,160,160)
    self.btcolor = Color(0,0,0)
  def addElement(self,element: UIElement):
    self.items.append(element)
  
  def removeElement(self,index: int):
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
  def __init__(self, x: int, y: int, width: int, height: int, text: str, onClick: function, arg: any):
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
    self.onClickEvent = Event()

  def setText(self, text: str):
    self.text = text

  def getText(self)->str:
    return self.text

  def getSize(self)->tuple:
    size = self.width, self.height
    return size

  def setSize(self, width: int, height: int):
    self.width = width
    self.height = height

  def render(self):
    if self.isClick():
      if self.onClick != None:
        if self.arg != None:
          self.callback = self.onClick(self.arg)
        else:
          self.callback = self.onClick()
        self.onClickEvent.InvokeListeners(self)
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
  def __init__(self,x: int,y: int,width: int,height: int,isRender: bool):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = Color(55,55,55)
    self.bdcolor = Color(0,0,0)
    self.items = []
    self.hasBorder = False
    self.isRender = isRender
  
  def addElement(self,element: UIElement):
    element.x = self.x+element.x
    element.y = self.y+element.y
    self.items.append(element)
  
  def removeElement(self,index: int):
    self.items.pop(index)
  
  def removeAll(self):
    self.items.clear()
    
  def toggleRender(self):
    self.isRender = not self.isRender
  
  def setRender(self, state: bool):
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
  def __init__(self,x: int,y: int,width: int,height: int,min: float,max: float,value: float,isInt: bool):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.rangemax = max
    self.rangemin = min
    self.value = value
    self.ischange = False
    self.isint = isInt
    self.bgcolor = Color(160,160,160)
    self.bdcolor = Color(0,0,0)
    self.slcolor = Color(105,105,105)
    self.selcolor = Color(0,0,0)
    self.lncolor = Color(0,0,0)
    self.maxtxcolor = Color(0,0,0)
    self.mintxcolor = Color(0,0,0)
    self.valbxcolor = Color(150,150,150)
    self.valtxcolor = Color(0,0,0)
    self.prvalue = self.x+(self.width/2)
    self.onChangeValue = Event()
    self.onSelectValue = Event()
  
  def evalValue(self):
    medval = (self.prvalue-self.x-5)/(self.width-10)
    frange = abs(self.rangemax)+abs(self.rangemin)
    if self.isint:
      self.value = round((medval*frange)-abs(self.rangemin),0)
    else:
      self.value = round((medval*frange)-abs(self.rangemin),2)
    
  
  def render(self):
    if self.isClick():
      if not self.ischange:
        self.onSelectValue.InvokeListeners(self)
      self.ischange = not self.ischange
    
    if self.ischange:
      tempval = get_mouse()
      self.prvalue = tempval[0]
      if self.prvalue < self.x+5:
        self.prvalue = self.x+5
      if self.prvalue > self.x+self.width-5:
        self.prvalue = self.x+self.width-5
    self.bgcolor.gset()
    fill_rect(self.x,self.y,self.width,self.height)
    self.bdcolor.gset()
    draw_rect(self.x,self.y,self.width,self.height)
    self.lncolor.gset()
    draw_line(self.x+5,self.y+(self.height/1.5),(self.x+self.width)-5,self.y+(self.height/1.5))
    if self.ischange:
      self.selcolor.gset()
    else:
      self.slcolor.gset()
    fill_circle(self.prvalue,self.y+(self.height/1.5),5)
    if self.ischange:
      self.valbxcolor.gset()
      fill_rect(self.prvalue-10,self.y+self.height+3,35,15)
      self.evalValue()
      self.valtxcolor.gset()
      draw_text(self.prvalue-8, self.y+self.height+4, str(self.value))
      self.onChangeValue.InvokeListeners(self)
    self.mintxcolor.gset()
    draw_text(self.x+2,self.y+(self.height/3)-8,str(self.rangemin))
    self.maxtxcolor.gset()
    draw_text(self.x+self.width-getStringWidth(str(self.rangemax)),self.y+(self.height/3)-8,str(self.rangemax))

class Colorpicker(UIElement):
  def __init__(self,x: int,y: int,color: Color):
    self.x = x
    self.y = y
    self.width = 120
    self.height = 105
    self.crcolor = color
    self.items = []
    self.bgcolor = Color(105,105,105)
    self.bdcolor = Color(255,255,255)
    self.isopen = False
    self.onselect = Event()
    self.onrandom = Event()
    self.onopen = Event()
    #the items
    self.ranbt = Button(5,5,50,20,"random",self.rancol,None)
    self.setbt = Button(65,5,50,20,"select",self.selcol,None)
    self.rbox = Textbox(65,80,50,20,str(color.R),False,False)
    self.rbox.CL = 3
    self.gbox = Textbox(65,55,50,20,str(color.G),False,False)
    self.gbox.CL = 3
    self.bbox = Textbox(65,30,50,20,str(color.B),False,False)
    self.bbox.CL = 3
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
    Random.seed(get_time_ms())
    self.rbox.setText(str(Random.randint(0,255)))
    self.gbox.setText(str(Random.randint(0,255)))
    self.bbox.setText(str(Random.randint(0,255)))
    self.onrandom.InvokeListeners(self)
  
  def open(self):
    self.isopen = True
    self.onopen.InvokeListeners(self)

  def selcol(self):
    self.isopen = False
    self.onselect.InvokeListeners(self)

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
    if r>255:
      r=255
    if g>255:
      g=255
    if b>255:
      b=255
    self.crcolor.mset(r,g,b)
  
  def getColor(self)->Color:
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

class Document:
  lines = []
  def __init__(self, width: int, height: int, text: str):
    self.width = width
    self.height = height
    self.algotype = 0
    self.algo0time = -1
    self.algo1time = -1
    first = get_time_ms()
    self.lines = WrapText(text, self.width/8)
    self.algo0time = (get_time_ms()-first)/1000   
  def calclines(self, text: str):
    if self.algotype == 1:
      first = get_time_ms()
      self.lines = WrapText_D(text, self.width/8)
    else:
      first = get_time_ms()
      self.lines = WrapText(text, self.width/8)
      self.algo1time = (get_time_ms()-first)/1000
      


class Textarea(UIElement):
  def __init__(self, x: int, y: int, width: int, height: int):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.readonly = False
    self.exitkey = "up"
    self.edit = False
    self.text = " "
    self.bdcolor = Color(0,0,0)
    self.txcolor = Color(0,0,0)
    self.bgcolor = Color(230,230,230)
    self.onTextChange = Event()
    self.onEdit = Event()
    self.onExit = Event()
    self.document = Document(width, height, self.text)
    self.firstLoop = True
  def calcarea(self, args):
    self.document.calclines(args)

  def setText(self, newtext: str):
    self.text = newtext

  def addText(self, addtext: str):
    self.text += addtext

  def render(self):
    #Input
    if(self.isClick()):
      self.edit = not self.edit
      if not self.edit:
        self.calcarea(self.text)

    if self.edit:
      self.bgcolor.mset(215,215,215)
      key = get_key(1)
      newtext = ""
      if key == self.exitkey:
        self.edit = False
      elif key == "del":
        newtext = self.text[:len(self.text)-1]
      elif key == "enter":
        newtext = self.text+"new"
      else:
        newtext = self.text + key
      self.document.calclines(newtext)
      self.text = newtext
      self.onTextChange.InvokeListeners(self)
    else:
      self.bgcolor.mset(230,230,230)
    #Render
    self.bgcolor.gset()
    fill_rect(self.x, self.y, self.width, self.height)
    self.bdcolor.gset()
    draw_rect(self.x, self.y, self.width, self.height)
    self.txcolor.gset()
    add = 5
    for lin in self.document.lines:
      draw_text(self.x+2,(self.y+self.height-10)-add, lin)
      add = add+10



