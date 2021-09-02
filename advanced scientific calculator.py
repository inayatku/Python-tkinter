from tkinter import *
from math import *
from time import *
from sympy import *
from sympy.solvers.solveset import solvify
cal = Tk()
cal.title("Advanced Scientific Calculator")
cal.geometry("+200+0")
clock = Frame(cal);clock.pack(fill=X)
var = LabelFrame(cal,text="Click these buttons to assign your result to these variables");var.pack()
init =Frame(cal);init.pack()
mainscreen = Frame(cal);mainscreen.pack()
navi=Frame(mainscreen);navi.pack(side=RIGHT)
subscreen = Frame(cal);subscreen.pack()
buttons = Frame(cal);buttons.pack()

keys=[]
invifact=b'\xe2\x80\x8e'.decode('UTF-8')
invicross=b'\xfe\xff'.decode('UTF-16 BE')

global cursor 

def clearframe(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
def tick():
    clocklabel.config(text=strftime("%I:%M:%S %p"))
    disp1.see('insert-1d line')
    clocklabel.after(1000,tick)

clocklabel=Label(clock,text=strftime("%I:%M:%S"),font=('Courier','15'));clocklabel.pack(side=LEFT)


def createnavi():
    btnup=Button(navi,text="🠝",command=lambda event=None:up(event));btnup.pack(ipady=5)
    btndown=Button(navi,text="🠟",command=lambda event=None:down(event));btndown.pack(side=BOTTOM,ipady=5)
    btnleft=Button(navi,text="🠜",command=lambda event=None:left(event) );btnleft.pack(side=LEFT,padx=10,ipadx=5)
    btnright=Button(navi,text="🠞",command=lambda event=None:right(event) );btnright.pack(side=RIGHT,padx=10,ipadx=5)
    disp1.bind('<Up>',up)
    disp1.bind('<Down>',down)
    disp1.bind('<Left>',left)
    disp1.bind('<Right>',right)
def up(event):
    if int(disp1.index(INSERT).split('.')[1])>=2:disp1.see('insert-1d line');
    if int(disp1.index(INSERT).split('.')[0])>1: disp1.mark_set(INSERT,'insert-1d line');
    return 'break'
def down(event):
    disp1.see('insert-1d line');
    if int(disp1.index(INSERT).split('.')[0])<3:disp1.mark_set(INSERT,'insert+1d line');
    return 'break'
def left(event):
    if int(disp1.index(INSERT).split('.')[1])>=3:disp1.see('insert-3d char');
    if int(disp1.index(INSERT).split('.')[1])>0: disp1.mark_set(INSERT,'insert-1d char');
    return 'break'
def right(event):
    disp1.see('insert+3d char');
    disp1.mark_set(INSERT,'insert+1d char');
    return 'break'

def simple():
    global keys
    keys =["𝑎²"   ,"𝑎³"   ,"𝑎ⁿ"   ,"√𝑎"  ,"𝑎⁻¹"      ,"𝑎⁻²"  ,"𝑎⁻³","³√𝑎" ,"CE"   ,"DEL",
            "7"  ,"8"  ,"9"  ,"0"    ,"-"    ,"/"    ,"ⁿCₘ"," "        ,"'─'"  ," "  ,
            "4"  ,"5"  ,"6"  ,"."    ,"+"    ,"×"    ," "   ,"d→f"     ,"f→d" ,"𝑎\n─\n𝑏"   ,
          "1"  ,"2"  ,"3"  ," "    ,"()"   ," " ," "," ","Compute"," " ]
    createbuttons()

def scientific():
    global keys
    keys=["sin","cos","tan","csc","sec","cot","logₑ","eⁿ"      ,"CE"   ,"DEL",
          "x"  ,"y"  ,"z"  ,"𝑎²"   ,"𝑎³"   ,"𝑎ⁿ"   ,"√𝑎"  ,"𝑎⁻¹"      ,"𝑎⁻²"  ,"𝑎⁻³",
          "7"  ,"8"  ,"9"  ,"0"    ,"-"    ,"/"    ,"³√𝑎" ,"°"        ,"'─'"  ,"𝑎\n─\n𝑏"  ,
          "4"  ,"5"  ,"6"  ,"."    ,"+"    ,"×"    ,"()!"   ,"d→f"     ,"f→d" ," "  ,
          "1"  ,"2"  ,"3"  ,"π"    ,"()"   ,"Solve\nfor x" ,"=",",","∫dx","𝜕/𝜕x",
          "×10ⁿ","Rand#","ⁿCₘ","Gamma","Simplify 1"," ","Simplify 2"," " ,"Simplify 3" ," ",
          "Factorize" ," ","Expand"    ," ","Solve System\nof Equations"," " ,"Result→Edit"," ","Compute"," ",
          "Trignometric\nSimplify"," ","Combinatorial\nSimplify"," ","Invisible\nMultiplication","","Linear\nOutput→Edit" ,"","",""]
    createbuttons()
    
def createbuttons():
    clearframe(navi)
    clearframe(buttons)
    btn=[]
    createnavi()
    for i in range(len(keys)):
        btn.append(Button(buttons,bd=6,text=keys[i],font=('Courier','14','bold'),command=lambda i=i:func(i),width =1, height=1))
        btn[i].grid(row=i//10,column=i%10,ipadx=25,ipady=0)               
    btn[29].grid(rowspan=2,ipady=26)
    btn[39].destroy()
    for i in range(45,54):
        btn[i].config(font=('courier','13','bold'),width=6);btn[i].grid(ipadx=1,ipady=1)
    for i in range(54,79,2):
        btn[i].config(font=('courier','13','bold'),width=9);
        btn[i].grid(columnspan=2)
        btn[i+1].destroy()
    btn[78].destroy()
    btn[79].destroy()
    btn[68].grid(rowspan=2,columnspan=2,ipady=26)
    
    disp1.bind('<Return>',enter)
    disp1.bind('<Tab>',tab)
    disp1.bind('<Escape>',escape)
    disp1.bind('<BackSpace>',backspace)

def escape(event):
    disp1.delete(1.0,END);
    disp1.insert(1.0,' '*200+'\n'+' '*200+'\n'+' '*200+'\n');
    disp3.delete(1.0,END);
    disp3.insert(1.0,' '*200+'\n'+' '*200+'\n'+' '*200+'\n');
    disp3.mark_set(INSERT,2.0);
    disp1.mark_set(INSERT,2.0);
    return 'break'
def enter(event):
    disp2.delete(0,END);x,y,z=symbols("x y z");
    disp=sympify(dispread(disp1));
    dispwrite(disp2,str(disp.subs(x,sympify(dispread(xvalue))).subs(y,sympify(dispread(yvalue))).subs(z,sympify(dispread(zvalue)))))
    dispresult(disp3,dispread(disp2))
    return 'break'
def tab(event):
    dispfrac();
    return 'break'
def backspace(event):
    display=cal.focus_get()
    if int(display.index(INSERT).split('.')[1])>0:display.delete('insert-1d char')
    return 'break'


def func(i):
    display=cal.focus_get()
    if keys[i]=="Compute": enter(None)
    elif keys[i]=="CE": escape(None)
    elif keys[i]=="DEL":backspace(None)
    elif keys[i]=="𝑎²":display.insert(INSERT,'²');
    elif keys[i]=="𝑎³":display.insert(INSERT,'³')
    elif keys[i]=="𝑎⁻²":display.insert(INSERT,'⁻²')
    elif keys[i]=="𝑎⁻³":display.insert(INSERT,'⁻³')
    elif keys[i]=="√𝑎":display.insert(INSERT,'√()');display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="³√𝑎":display.insert(INSERT,"³√()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="𝑎⁻¹":display.insert(INSERT,'⁻¹')
    elif keys[i]=="sin":display.insert(INSERT,"sin()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="cos":display.insert(INSERT,"cos()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="tan":display.insert(INSERT,"tan()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="csc":display.insert(INSERT,"csc()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="sec":display.insert(INSERT,"sec()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="cot":display.insert(INSERT,"cot()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="Gamma":display.insert(INSERT,"gamma()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="logₑ":display.insert(INSERT,"log()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="eⁿ":display.insert(INSERT,"e^()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="()":display.insert(INSERT,"()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="()!" :display.insert(INSERT,invifact+"()!");display.mark_set(INSERT,'insert-2d char')
    elif keys[i]=="𝑎ⁿ":display.insert(INSERT,"^()");display.mark_set(INSERT,'insert-1d char')
    elif keys[i]=="×10ⁿ":display.insert(INSERT,"×10^()");display.mark_set(INSERT,'insert-1d char')  
#    elif keys[i]=="Rand#": None
    elif keys[i]=="Invisible\nMultiplication":display.insert(INSERT,invicross);
    elif keys[i]=="x":display.insert(INSERT,"x")
    elif keys[i]=="y":display.insert(INSERT,"y")
    elif keys[i]=="z":display.insert(INSERT,"z")
#    elif keys[i]=="save":displines(disp1)
    elif keys[i]=="𝑎\n─\n𝑏": tab(None)
    elif keys[i]=="'─'":
        if disp1.index(INSERT).split('.')[0]=='1' and disp1.index(INSERT).split('.')[1]=='0':disp1.insert(INSERT+'+1d line','─')
        elif disp1.index(INSERT).split('.')[0]=='3' and disp1.index(INSERT).split('.')[1]=='0':disp1.insert(INSERT+'-1d line','─')
        elif disp1.index(INSERT).split('.')[0]=='1' and int(disp1.index(INSERT).split('.')[1])>0:disp1.insert(INSERT+'+1d line-1d char','─')
        elif disp1.index(INSERT).split('.')[0]=='3'and int(disp1.index(INSERT).split('.')[1])>0:disp1.insert(INSERT+'-1d line-1d char','─')
        else:disp1.insert(INSERT,'─')
    elif keys[i]=="d→f":
        s1= sympify(dispread(disp2));disp2.delete(0,END);
        disp2.insert(END,Rational(s1).limit_denominator(1000000))
        dispresult(disp3,dispread(disp2))
    elif keys[i]=="f→d":
        s2= sympify(dispread(disp2));disp2.delete(0,END);
        disp2.insert(END,round(s2.evalf(),10))
    elif keys[i]=="ⁿCₘ":
        display.insert(INSERT,"comb(,)");display.mark_set(INSERT,'insert-2d char')
    elif keys[i]=="Expand":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        dispwrite(disp2,str(expand(dispread(disp1))))
        dispresult(disp3,dispread(disp2))
    elif keys[i]=="Factorize":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        dispwrite(disp2,str(factor(dispread(disp1))))
        dispresult(disp3,dispread(disp2))
    elif keys[i]=="Trignometric\nSimplify":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        dispwrite(disp2,str(trigsimp(dispread(disp1))))
        dispresult(disp3,dispread(disp2))
    elif keys[i]=="∫dx":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        dispwrite(disp2,str(integrate(dispread(disp1),x)))
        dispresult(disp3,dispread(disp2))
    elif keys[i]=="𝜕/𝜕x":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        dispwrite(disp2,str(diff(dispread(disp1),x)))
        dispresult(disp3,dispread(disp2))
    elif keys[i]=="Result→Edit":
        s=disp3.get('1.0',END);escape(None);
        disp1.insert(1.0,s);disp1.mark_set(INSERT,2.0);  
    elif keys[i]=="Simplify 1":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        dispwrite(disp2,str(sympify(dispread(disp1))))
        dispresult(disp3,dispread(disp2))
    elif keys[i]=="Simplify 2":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        dispwrite(disp2,str(cancel(dispread(disp1))))
        dispresult(disp3,dispread(disp2))
    elif keys[i]=="Simplify 3":
        disp2.delete(0,END);x,y,z=symbols("x y z");      
        print(simplify(dispread(disp1)))
        dispwrite(disp2,str(simplify(dispread(disp1))))
        dispresult(disp3,str(dispread(disp2)))
        print(str(dispread(disp2)))
    elif keys[i]=="Solve\nfor x":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        eq= dispread(disp1).split('=',1)
        if len(eq)==1:
            eq=sympify(eq)
            equ=eq[0]
            dispwrite(disp2,str(solvify(equ,x,Complexes)))
        elif len(eq)==2:
            eq=sympify(eq)
            equ=Eq(eq[0],eq[1])
            dispwrite(disp2,str(solvify(equ,x,Complexes)))
        else : dispwrite(disp2,"Error!! Incorrect Equation Format")
        dispresult(disp3,dispread(disp2),1)
    elif keys[i]=="Combinatorial\nSimplify":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        dispwrite(disp2,str(combsimp(sympify(dispread(disp1)))))
        dispresult(disp3,dispread(disp2))
    elif keys[i]=="Linear\nOutput→Edit":
        s=disp2.get();escape(None);
        s=s.strip('[').strip(']')
        disp1.insert(2.0,s);disp1.mark_set(INSERT,2.0);           
    elif keys[i]=="Solve System\nof Equations":
        disp2.delete(0,END);x,y,z=symbols("x y z");
        eq=dispread(disp1).split(',')
        var=[]
        if eq[0].find('=')==-1:
            eq=sympify(eq)
            for i in range(len(eq)):
                var.append(eq[i].free_symbols)
        else:
            for i in range(len(eq)):
                eq[i]=(eq[i].split('=')[0],eq[i].split('=')[1])
                eq[i]=sympify(eq[i])
                eq[i]=Eq(eq[i][0],eq[i][1])
                var.append(eq[i].free_symbols)
        dispwrite(disp2,str(solve(eq,set().union(*var))).replace(':',' = '))
        dispresult(disp3,dispread(disp2).replace(':',' = '),1)
             
    else: disp1.insert(INSERT,keys[i])


def cubrt(x): return x**(1/3)


# read the output screen and assign that output to variable v
def send(v):
    if v=='x':x=disp2.get();xvalue.delete(0,END);xvalue.insert(END,x)
    elif v=='y':y=disp2.get();yvalue.delete(0,END);yvalue.insert(END,y)
    elif v=='z':z=disp2.get();zvalue.delete(0,END);zvalue.insert(END,z)


# reads the display string and convert it into python notations 
def dispread(display):
    if display==disp1:dispr=displines(disp1)    # if display is input display then first convert it into string 
    else: dispr = display.get()
    dispr=dispr.replace('^','**')
    dispr=(dispr).replace('comb','binomial')
    dispr=(dispr).replace('π','pi')
    dispr=(dispr).replace("×",'*')
    dispr=(dispr).replace("³√","cubrt")
    dispr=(dispr).replace("√",'sqrt')
    dispr=(dispr).replace(invicross,'*')
    dispr=(dispr).replace(invifact,'factorial')
    dispr=(dispr).replace('!','')
    dispr=(dispr).replace("°",'*pi/180')
    dispr=(dispr).replace("sin⁻¹",'asin')
    dispr=(dispr).replace("cos⁻¹",'acos')
    dispr=(dispr).replace("tan⁻¹",'atan')
    dispr=(dispr).replace("csc⁻¹",'acsc')
    dispr=(dispr).replace("sec⁻¹",'asec')
    dispr=(dispr).replace("cot⁻¹",'acot')
    dispr=(dispr).replace("⁻¹",'**(-1)')
    dispr=(dispr).replace("⁻²",'**(-2)')
    dispr=(dispr).replace("⁻³",'**(-3)')
    dispr=(dispr).replace("²",'**2')
    dispr=(dispr).replace("³",'**3')
    print(dispr)
    return dispr

def displines(display):     # read lines of input display and convert it to a string 
    strexp=''
    line = display.get('1.0', END).splitlines();     
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
    return strexp
# this function executes when we press tab. and it starts writing fraction when current location is line 1. it go
# to line 0 then if we press it again it go to line 2 and then it go to line 1.
def dispfrac():
    global cursor,length   
    if disp1.index(INSERT).split('.')[0]=='2':
        cursor=disp1.index(INSERT);
        disp1.mark_set(INSERT,cursor+'-1d line+2d char')
    elif disp1.index(INSERT).split('.')[0] =='1':
        s1=disp1.get(cursor+'-1d line+2d char','insert')
        n=len(s1)
        length =n
        print("length num=",n)
        disp1.delete(cursor,cursor+'+'+str(length+3)+'d char')
        disp1.insert(cursor+'+1d char',"─"*(length+2))
        disp1.mark_set(INSERT,cursor+'+1d line+2d char')
    elif disp1.index(INSERT).split('.')[0] =='3':
        
        s2=disp1.get(cursor+'+1d line+2d char','insert')
        d=len(s2)
        if d>length: length=d
        print("length den",d)
        numerator=disp1.get(cursor+'-1d line+2d char',cursor+'-1d line'+'+'+str(length+2)+'d char').strip()
        denominator=disp1.get(cursor+'+1d line+2d char',cursor+'+1d line'+'+'+str(length+2)+'d char').strip()
        printfrac(disp1,cursor,numerator,denominator)
# writes a fraction on display at location loc
def printfrac(display,loc,num,den):
#    print(num,den)
    nlen=len(num)
    invinlen=num.count(invicross)+num.count(invifact)
    rnlen=nlen-invinlen
    dlen=len(den)
    invidlen=den.count(invicross)+den.count(invifact)
    rdlen= dlen-invidlen
#    print("actual length=",nlen,dlen)
#    print("redued length=",rnlen,rdlen)
    rlen=rnlen
    tlen=nlen
    if rdlen>rlen: rlen=rdlen
    if dlen>nlen : tlen=dlen
    display.delete(loc+'-1d line',loc+'-1d line'+'+'+str(tlen+3)+'d char')
    display.delete(loc,loc+'+'+str(tlen+3)+'d char')
    display.delete(loc+'+1d line',loc+'+1d line'+'+'+str(tlen+3)+'d char')
    if nlen>dlen: num=num.center(tlen+2);den=den.center(rlen+2)
    elif dlen>nlen: num=num.center(rlen+2);den=den.center(tlen+2)
    else:num=num.center(tlen+2);den=den.center(tlen+2)
#     print(" "+num)
#     print(" "+"─"*(rlen+2))
#     print(" "+den)
    display.insert(loc+'-1d line+1d char',num)
    display.insert(loc+'+1d char',"─"*(rlen+2))
    display.insert(loc+'+1d line+1d char',den)
    display.mark_set(INSERT,loc+'+'+str(rlen+4)+'d char')

def dispresult(display,equstr,solve=0):
    disp3.delete(1.0,END);
    disp3.insert(1.0,' '*200+'\n'+' '*200+'\n'+' '*200+'\n');
    disp3.mark_set(INSERT,2.0);
    equstr = convert(equstr)
    print(equstr)
    if solve==1:
        equstr=equstr[1:-1]
        equstr=equstr.replace('I','i')
    splitstr=list(equstr)
    for i in range(2):splitstr.append(" ")
    i=0
    while i <len(splitstr)-2:
        count =0
        while splitstr[i]!='(':
            if splitstr[i]=='-' or splitstr[i]=='+' or splitstr[i]=='/' or splitstr[i]==',' or splitstr[i]=='=':
                splitstr.insert(i,'@')
                splitstr.insert(i+2,'@')
                i+=2
            else:i+=1
            if i>=len(splitstr)-2: break
        count=1
        print("count=",count)
        while count !=0:
            i+=1
            if splitstr[i]=='(':count+=1
            if splitstr[i]==')':count-=1
            if i>=len(splitstr)-2: break
        i+=1
        if i>=len(splitstr)-2: break
    equstr="";equstr=equstr.join(splitstr);
    print(equstr)
    equstr = equstr.split("@")
    print(equstr)
    for i in range(len(equstr)):
        if equstr[i]=='/': equstr.pop(i);equstr.insert(i-1,'/');
    j=0
    display.mark_set(INSERT,'2.0')
    if solve==1:display.insert(INSERT,'{')
    for i in range(len(equstr)):
        if equstr[i]=='/':
            j=i;
            equstr[j+1]=equstr[j+1].strip()
            equstr[j+2]=equstr[j+2].strip()
            printfrac(display,INSERT,equstr[j+1],equstr[j+2]);j+=3
        if i==j:
            display.insert(INSERT,equstr[i]);
            j=i;
            j+=1;
    if solve==1: display.insert(INSERT,'}')
    display.mark_set(INSERT,'2.0')

# write the output string to display 
def dispwrite(display,dispw):
    dispw=convert(dispw)
    dispw = display.insert(END,dispw)

#convert python output to user friendly output
def convert(dispw):
    dispw=dispw.replace('**2',"²")
    dispw=(dispw).replace('**3',"³")
    dispw=(dispw).replace('**(-1)',"⁻¹")
    dispw=(dispw).replace('**(-2)',"⁻²")
    dispw=(dispw).replace('**(-3)',"⁻³")
    dispw=dispw.replace('**','^')
    dispw=(dispw).replace('pi','π')
    dispw=(dispw).replace('*pi/180',"°")
    dispw=(dispw).replace('*',"×")
    dispw=(dispw).replace('sqrt',"√")
    dispw=(dispw).replace('asin',"sin⁻¹")
    dispw=(dispw).replace('acos',"cos⁻¹")
    dispw=(dispw).replace('atan',"tan⁻¹")
    dispw = dispw.replace(" ","")
    dispw=dispw.replace("×",invicross)
    return (dispw)

Button(var,text="𝑥 =",font=('Courier','15','bold'),command=lambda:send('x')).grid(row=0,column=0);
xvalue=Entry(var,bd=6,justify=RIGHT,font=('Courier','15','bold'),width=10);xvalue.grid(row=0,column=1);xvalue.insert(END,'x')
Button(var,text="𝑦 =",font=('Courier','15','bold'),command=lambda:send('y')).grid(row=0,column=2);
yvalue=Entry(var,bd=6,justify=RIGHT,font=('Courier','15','bold'),width=10);yvalue.grid(row=0,column=3);yvalue.insert(END,'y')
Button(var,text="𝑧 =",font=('Courier','15','bold'),command=lambda:send('z')).grid(row=0,column=4);
zvalue=Entry(var,bd=6,justify=RIGHT,font=('Courier','15','bold'),width=10);zvalue.grid(row=0,column=5);zvalue.insert(END,'z')


disp1 = Text(mainscreen, bd=4,font=('Courier New','18','bold'),height=3,width=40,wrap='none')
disp1.pack()
sbh1 = Scrollbar(mainscreen,orient=HORIZONTAL,command=disp1.xview)
disp1.config(xscrollcommand=sbh1.set)
sbh1.pack(fill=X)
cursor=disp1.index(INSERT)

disp2=Entry(subscreen,bd=6,justify=RIGHT,font=('Courier','18','bold'),width=60);
disp2.grid(row=0,column=0,columnspan=2)

disp3 = Text(mainscreen, bd=4,font=('Courier New','14','bold'),height=3,width=70,wrap='none')
disp3.pack()
sbh2 = Scrollbar(mainscreen,orient=HORIZONTAL,command=disp3.xview)
disp3.config(xscrollcommand=sbh2.set)
sbh2.pack(fill=X)

disp1.focus_set();escape(None)
scientific()

Button(init,text="Simple Calculator",command=simple).pack(side=LEFT)
Button(init,text="Scientific Calculator",command=scientific).pack(side=LEFT)
tick()
cal.mainloop()
