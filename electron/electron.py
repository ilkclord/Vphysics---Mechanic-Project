from vpython import * 


"""
y
^
|
z - > x  3D tips

"""
t = 0 
dt = 10**-19 # time interval
muti = 1

r = 53 * 10**-12 # balance radius of standing wave
mr = 1.05 * r # maxima radius of mass wave
A = 1.6 * 10 **7
om1 = A / r # omega of orbit 10**19
om2 = 10 **25 # spinning omega of frame
om3 =  3 * om1# electron mass wave omega
B  = 10**8 #Amptitude of turing angular velocity 
R = vector(10 ,10,10) # the vector points to the core of atom
ugly = 0 # calculate usage

# function doing intergral of the term cant be intergraled
def getu() : 
    return B * sin(om2 * t) * atan2(-1 , cos(om1 * t))

def ugly_term() :
    global ugly
    ugly = ugly + getu() * dt
    return ugly

# get the value of each coordinate

def getro(t) :
    p1 = r + (mr - r) * sin(om3 * t)
    p2 = ugly_term()
    return  p1  + p2

def getthe(t) :
    d1 = om1 * t
    
    return d1

def getphy(t) :
    d1 = om1 * t
    p1 = atan2(-1 , cos(d1))
    p2 = ( r + (mr - r) * sin(om3 * t) )* B * cos(om2 * t) / om2
    return p1 + p2
    
def getx(ro , the ,phy) :

    return muti * ro * sin(phy) * cos(the)

def gety(ro , the , phy) :
    
    return muti * ro * sin(phy) * sin(the)
def getz(ro , the , phy) :
    
    return muti * ro * cos(phy)

# innitialize
ro = getro(t) 
the = getthe(t)
phy = getphy(t)
x = getx(ro ,the ,phy)
y = gety(ro ,the ,phy)
z = getz(ro ,the ,phy)

# plot
g1 = graph(title = "electron xy")
f1 = gcurve(color = color.blue , dot = True)
g2 = graph(title = "electron xz")
f2 = gcurve(color = color.red  , dot = True)
g3 = graph(title = "electron yz")
f3 = gcurve(color = color.cyan , dot = True)
g4 = graph(title = "elctron orbit")
f4 = gcurve(color = color.black , dot = True)

# 3D
background = canvas(center = vector(0,0,0) , width = 1000 , height = 800 , background = color.black , title = "eletron orbit yz")
electron = sphere(pos = vector(x , y ,z) , color = color.blue , radius  = 10**-12, make_trail = True ) 
core = sphere(pos = vector(0,0,0) , color = color.red , radius  = 10**-12, make_trail = True ) 
background = canvas(title = "electron")

# information
print("Angular Velocity of elctron doing circular motion : " ,om1)
print("The changin frequency of frame : " ,om2 / 2 * pi)
print("The frequency of stanging wave of electron : " ,om3 / 2 * pi)
print("angular velocity of frame" , B)
print("Time interval" , dt)



# simulating the electron trace
while(t < 3000) :
    rate(1000)
    ro = getro(t)
    the = getthe(t)
    phy = getphy(t)
    x = getx(ro ,the ,phy)
    y = gety(ro ,the ,phy)
    z = getz(ro ,the ,phy)
    f1.plot(x, y)
    f4.plot(t,ro)
    f3.plot(y,z)
    f2.plot(x, z)
    new = vector(x , y ,z) 
    if(new == vector(0,0,0)) :
        print(t)
        break; 
    electron.pos = new
    t = t + dt
