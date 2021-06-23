from vpython import * 


"""
y
^
|
z - > x

"""
# object attr
# in the environment of latitude 30 degree
# the degree of pendalm is 5 

m = 1  # mass of the ball
T = m * 9.8 # Tension Force
l = 9.8  # length of the rope (m)
omega = 3.646 * 10**(-5) ; # the angular speed of the earth
alpha = 1 ;  # sqrt(T / l)
t = 0 
dt = 0.01 # small time interval

"""
q = exp (A * exp() + B * exp())

"""
A = 0.42706  # caculate by l * sin(degree of pendalm)
B = 0.42706  # B = A , so the ball will pass the origin

# uupdate the theta
def thetaup(t) :
    return t * alpha
# equation of position
def getx(t) :
    d1 = radians(alpha * t) 
    d2 = radians(omega * t )
    p1 = A * (cos(d1) * cos(d2) + sin(d1) * sin(d2))
    p2 = B * (cos(d1) * cos(d2) - sin(d1) * sin(d2))
    return p1 + p2
def getz(t) :
    d1 = radians(alpha * t) 
    d2 = radians(omega * t )
    p1 = A * (-1 * cos(d1) * sin(d2) + sin(d1) * cos(d2))
    p2 = B * (-1 * cos(d1) * sin(d2) - sin(d1) * cos(d2))
    return p1 + p2
# equation of velocity
def getvx(t) :
    d1 = radians(alpha * t)
    d2 = radians(omega * t )
    t1 = d1 - d2
    t2 = d1 + d2
    p1 = -1 * A * sin(t1) * (alpha - omega)
    p2 = -1 * B * sin(t2) * (alpha + omega)
    return p1 + p2 
def getvz(t) :
    d1 = radians(alpha * t) 
    d2 = radians(omega * t )
    t1 = d1 - d2
    t2 = d1 + d2
    p1 = A * cos(t1) * (alpha - omega)
    p2 = -1 * B * cos(t2) * (alpha + omega)
    return p1 + p2 
# fricton force
def fric(v) : # air drag
    mu = 0.1
    direct = 1
    if(v < 0):
        direct = -1 
    f =  -1 * mu * 0.0098
    a = f / m
    dv = a * dt
    return dv * direct



# the scene
g1 = graph(title = "Foucault Pendulum with friction", wide = 1000 , height = 800)
f1 =  gcurve(color=color.blue) # friction
f2 = gcurve(color= color.red ) # without friction

# simulating the Foucault Pendulu
#original positoin at t = 0
ox = getx(t)
oz = getz(t)
oxp = ox
ozp = oz
# record the velocity in last time interval
px = getvx(t)
pz = getvz(t)
# fixed velocity
vx = px
vz = pz

# the fix term of the velocity
vfx = 0 
vfz = 0

while(t < 1000) :
    # if the direction changes , recalculate the fix term
    if(abs(px) + abs(getvx(t)) != abs(px + getvx(t))) :
        vfx = 0
    if(abs(pz) + abs(getvz(t)) != abs(pz + getvz(t))) :
        vfz = 0
    vx = getvx(t) + vfx # the fixed velocity
    vz = getvz(t) + vfz
    dvx = fric(vx) # fixed term
    dvz = fric(vz) 
    oxp = oxp + getvx(t) * dt # pure
    ozp = ozp + getvz(t) * dt
    ox = ox  + dvx * dt + vx * dt #drag
    oz = oz  + dvz * dt + vz * dt
    f2.plot(oxp,ozp)
    if(abs(vx) <= abs(getvx(t)) and abs(vz) <= abs(getvz(t))): # check if it follows the real situation
        f1.plot(ox , oz)
    px = vx
    pz = vz
    vfx = dvx
    vfz = dvz
    t = t + dt
