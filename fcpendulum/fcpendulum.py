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
pmega = 10
alpha = 1 ;  # sqrt(T / l)
t = 0 
dt = 0.01 # small time interval
"""
q = exp (A * exp() + B * exp())

"""
A = 0.42706  # caculate by l * sin(degree of pendalm)
B = 0.42706  # B = A , so the ball will pass the origin

#equation of theta

def thetaup(t) :
    return t * alpha

#equation of position
def getx(t) :
    a = thetaup(t)
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

# simulating the Foucault Pendulum
g = graph(title = "Foucault Pendulum" ,wide = 1000 , height = 800)
f= gcurve(color = color.cyan)
while(t < 10000):
    t = t +dt 
    f.plot(getx(t) , getz(t))
