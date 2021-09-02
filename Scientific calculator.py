from tkinter import *
from math import *
from time import *

cal = Tk()
cal.title("Scientific Calculator")
cal.geometry("+200+0")
clock = Frame(cal);clock.pack(fill=X)
var = Frame(cal);var.pack()
init =Frame(cal);init.pack()
mainscreen = Frame(cal);mainscreen.pack()
navi=Frame(mainscreen);navi.pack(side=RIGHT)
subscreen = Frame(cal);subscreen.pack()

buttons = Frame(cal);buttons.pack()
x='0';y='0';z='0'
keys=[]
global cursor 
def clearframe(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
def tick():
    clocklabel.config(text=strftime("%I:%M:%S %p"))
    clocklabel.after(1000,tick)

clocklabel=Label(clock,text=strftime("%I:%M:%S"),font=('Courier','15'));clocklabel.pack(side=LEFT)
tick()

def createnavi():
    global btnup,btndown,btnleft,btnright
#    btnup=Button(navi,text="🠝",command=lambda:disp1.icursor(cursor));btnup.pack()  # just for entry widget
    btnup=Button(navi,text="🠝",command=lambda:disp1.mark_set(INSERT,'insert-1d line'));btnup.pack(ipady=5)
#    btnup=Button(navi,text="🠝",command=lambda:disp1.mark_set(INSERT,cursor+"-1c"));btnup.pack()
    btndown=Button(navi,text="🠟",command=lambda:disp1.mark_set(INSERT,'insert+1d line'));btndown.pack(side=BOTTOM,ipady=5)
    btnleft=Button(navi,text="🠜",command=lambda:disp1.mark_set(INSERT,'insert-1d char'));btnleft.pack(side=LEFT,padx=10,ipadx=5)
    btnright=Button(navi,text="🠞",command=lambda:disp1.mark_set(INSERT,'insert+1d char'));btnright.pack(side=RIGHT,padx=10,ipadx=5)
    disp1.bind('<Up>',up)
    disp1.bind('<Down>',down)
    disp1.bind('<Left>',left)
    disp1.bind('<Right>',right)
def createbuttons():
    global btn
    clearframe(navi)
    clearframe(buttons)
    btn=[]
    createnavi()
    for i in range(len(keys)):
        btn.append(Button(buttons,bd=6,text=keys[i],font=('Courier','18','bold'),command=lambda i=i:func(i),width =1, height=1))
        btn[i].grid(row=i//10,column=i%10,ipadx=25)               
    btn[39].destroy()
    btn[29].config(font=('courier','18','bold'),height=3)
    btn[29].grid(rowspan=2)
    disp1.bind('<Return>',Enter)
    disp1.bind('<Tab>',Tab1)
    disp1.bind('<Escape>',escape)
def up(event):btnup.invoke(); return 'break'
def down(event):btndown.invoke(); return 'break'
def left(event):disp1.see('insert-3d char');btnleft.invoke(); return 'break'
def right(event):disp1.see('insert+3d char');btnright.invoke(); return 'break'
def escape(event):btn[8].invoke();return 'break'
def Enter(event ):btn[len(keys)-1].invoke();return 'break'
def Tab1(event):btn[29].invoke();return 'break'
def Tab2(event):dispfrac();return 'break'
    
def simple():
    global keys
    keys =["𝑎²","𝑎³","𝑎ⁿ","√𝑎"," ","->x","->y","->z"," "," ","7","8","9","+"," ","4","5","6","-"," ","1","2","3","×"," ","0","(",")","/",
           " ",".","π","Ans"," ","="]
    createbuttons()
def scientific():
    global keys
    keys=["sin","cos","tan","sin⁻¹","cos⁻¹","tan⁻¹","logₑ","eⁿ"      ,"CE"   ,"DEL",
          "x"  ,"y"  ,"z"  ,"𝑎²"   ,"𝑎³"   ,"𝑎ⁿ"   ,"√𝑎"  ,"𝑎⁻¹"      ,"𝑎⁻²"  ,"𝑎⁻³",
          "7"  ,"8"  ,"9"  ,"0"    ,"-"    ,"/"    ,"³√𝑎"   ,"°"        ,"'─'"  ,"𝑎\n─\n𝑏"  ,
          "4"  ,"5"  ,"6"  ,"."    ,"+"    ,"×"    ,"("   ,")"        ,"disp" ," "  ,
          "1"  ,"2"  ,"3"  ,"π"    ,"Fact"    ,"Ans " ,"="   ]
    createbuttons()
def dispread(display):
    
    if display==disp1:dispr=displines(disp1)
    else: dispr = display.get()
    dispr=dispr.replace('^','**')
    dispr=(dispr).replace('π','pi')
    dispr=(dispr).replace("×",'*')
    dispr=(dispr).replace("³√","cubrt")
    dispr=(dispr).replace("√",'sqrt')
    dispr=(dispr).replace(b'\xfe\xff'.decode('UTF-16 BE'),'fact')
    dispr=(dispr).replace('!',"")
    dispr=(dispr).replace("°",'*pi/180')
    dispr=(dispr).replace("sin⁻¹",'asin')
    dispr=(dispr).replace("cos⁻¹",'acos')
    dispr=(dispr).replace("tan⁻¹",'atan')
    dispr=(dispr).replace("⁻¹",'**(-1)')
    dispr=(dispr).replace("⁻²",'**(-2)')
    dispr=(dispr).replace("⁻³",'**(-3)')
    dispr=(dispr).replace("²",'**2')
    dispr=(dispr).replace("³",'**3')
#    print(disp1r)
    return round(eval(dispr),10)
def fact(x):
    if x==0:return 1
    else: return x*fact(x-1)
def cubrt(x): return x**(1/3)

def displines(display):
    strexp=''
    line = display.get('1.0', END).splitlines();     
    print(display.get('1.0', END))
    while len(line[1].split('─',1))!=1:    
        strexp+=line[1].split('─',1)[0]
        line[1]=line[1].split('─',1)[1]
        line[1]=line[1].lstrip('─')
        line[0]=line[0].lstrip()
        line[2]=line[2].lstrip()
        strexp+='('+line[0].split('  ',1)[0]+')/('+line[2].split('  ',1)[0]+')'
        line[0]=line[0].split('  ',1)[1]
        line[2]=line[2].split('  ',1)[1]
    strexp+=line[1].rstrip()
    print (strexp)
    return strexp

def func(i):
    global x,y,z, Ans,cursor
    if keys[i]=="=":
         x=dispread(xvalue);y=dispread(yvalue);z=dispread(zvalue)
         s=dispread(disp1)
         disp2.delete(0,END)
         disp2.insert(END,s)        
    elif keys[i]=="CE":
        disp1.delete(1.0,END);
        disp1.insert(1.0,' '*40+'\n'+' '*40+'\n'+' '*40+'\n');
        disp1.mark_set(INSERT,2.0)
    elif keys[i]=="DEL":disp1.delete('insert-1d char')
    elif keys[i]=="𝑎²":disp1.insert(INSERT,'²');
    elif keys[i]=="𝑎³":disp1.insert(INSERT,'³')
    elif keys[i]=="𝑎⁻²":disp1.insert(INSERT,'⁻²')
    elif keys[i]=="𝑎⁻³":disp1.insert(INSERT,'⁻³')
    elif keys[i]=="√𝑎":disp1.insert(INSERT,'√()');disp1.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="³√𝑎":disp1.insert(INSERT,"³√()");disp1.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="𝑎⁻¹":disp1.insert(INSERT,'⁻¹')
    elif keys[i]=="Ans":Ans= dispread(disp2);disp1.insert(INSERT,'Ans')
    elif keys[i]=="sin":disp1.insert(INSERT,"sin()");disp1.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="cos":disp1.insert(INSERT,"cos()");disp1.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="tan":disp1.insert(INSERT,"tan()");disp1.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="sin⁻¹":disp1.insert(INSERT,"sin⁻¹()");disp1.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="cos⁻¹":disp1.insert(INSERT,"cos⁻¹()");disp1.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="tan⁻¹":disp1.insert(INSERT,"tan⁻¹()");disp1.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="logₑ":disp1.insert(INSERT,"log()");disp1.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="eⁿ":disp1.insert(INSERT,"e^")
    elif keys[i]=="Fact" : disp1.insert(INSERT,b'\xfe\xff'.decode('UTF-16 BE')+"()!");disp1.mark_set(INSERT,'insert-2d char')
    elif keys[i]=="𝑎ⁿ":disp1.insert(INSERT,"^")
    elif keys[i]=="x":disp1.insert(INSERT,"x")
    elif keys[i]=="y":disp1.insert(INSERT,"y")
    elif keys[i]=="z":disp1.insert(INSERT,"z")
    elif keys[i]=="disp":displines(disp1)
    elif keys[i]=="𝑎\n─\n𝑏": dispfrac()
    elif keys[i]=="'─'":
        if disp1.index(INSERT).split('.')[0]=='1':disp1.insert(INSERT+'+1d line-1d char','─')
        elif disp1.index(INSERT).split('.')[0]=='3':disp1.insert(INSERT+'-1d line-1d char','─')
        else:disp1.insert(INSERT,'─')
                        
    else: disp1.insert(INSERT,keys[i])

def send(v):
     if v=='x':x=dispread(disp1);xvalue.delete(0,END);xvalue.insert(END,x)
     elif v=='y':y=dispread(disp1);yvalue.delete(0,END);yvalue.insert(END,y)
     elif v=='z':z=dispread(disp1);zvalue.delete(0,END);zvalue.insert(END,z)
def dispfrac():
    global cursor,length   
    disp1.bind('<Tab>',Tab2)
    if disp1.index(INSERT).split('.')[0]=='2':
        cursor=disp1.index(INSERT);
        disp1.mark_set(INSERT,cursor+'-1d line+2d char')
    elif disp1.index(INSERT).split('.')[0] =='1':
        n=len(disp1.get(cursor+'-1d line+2d char','insert'))
        length =n
        disp1.insert(cursor+'+1d char',"─"*(length+2))
        disp1.mark_set(INSERT,cursor+'+1d line+2d char')
    elif disp1.index(INSERT).split('.')[0] =='3':
        m=len(disp1.get(cursor+'+1d line+2d char','insert'))
        if m>length: length=m
        numerator=disp1.get(cursor+'-1d line+2d char',cursor+'-1d line'+'+'+str(length+3)+'d char').strip()
        denominator=disp1.get(cursor+'+1d line+2d char',cursor+'+1d line'+'+'+str(length+3)+'d char').strip()
        disp1.delete(cursor+'-1d line+1d char',cursor+'-1d line'+'+'+str(length+3)+'d char')
        disp1.delete(cursor,cursor+'+'+str(length+3)+'d char')
        disp1.delete(cursor+'+1d line+1d char',cursor+'+1d line'+'+'+str(length+3)+'d char')
        numerator=numerator.center(length+2)
        denominator=denominator.center(length+2)
        disp1.insert(cursor+'-1d line+1d char',numerator)
        disp1.insert(cursor+'+1 char',"─"*(length+2))
        disp1.insert(cursor+'+1d line+1d char',denominator)
        disp1.mark_set(INSERT,cursor+'+'+str(length+4)+'d char')
        disp1.bind('<Tab>',Tab1)
            
        
    

Button(var,text="𝑥 =",font=('Courier','15','bold'),command=lambda:send('x')).grid(row=0,column=0);
xvalue=Entry(var,bd=6,justify=RIGHT,font=('Courier','15','bold'),width=10);xvalue.grid(row=0,column=1);xvalue.insert(END,'0.0')
Button(var,text="𝑦 =",font=('Courier','15','bold'),command=lambda:send('y')).grid(row=0,column=2);
yvalue=Entry(var,bd=6,justify=RIGHT,font=('Courier','15','bold'),width=10);yvalue.grid(row=0,column=3);yvalue.insert(END,'0.0')
Button(var,text="𝑧 =",font=('Courier','15','bold'),command=lambda:send('z')).grid(row=0,column=4);
zvalue=Entry(var,bd=6,justify=RIGHT,font=('Courier','15','bold'),width=10);zvalue.grid(row=0,column=5);zvalue.insert(END,'0.0')


disp1 = Text(mainscreen, bd=4,font=('Courier','18','bold'),height=3,width=40,wrap='none')
disp1.pack()

disp1.focus_set()
disp1.insert(1.0,' '*40+'\n'+' '*40+'\n'+' '*40+'\n');

disp1.mark_set(INSERT,2.0)
cursor=disp1.index(INSERT);

disp2=Entry(subscreen,bd=4,justify=RIGHT,font=('Courier','20','bold'));
disp2.grid(row=0,column=0,columnspan=2)
scientific()

Button(init,text="Simple Calculator",command=simple).pack(side=LEFT)
Button(init,text="Scientific Calculator",command=scientific).pack(side=LEFT)

cal.mainloop()
