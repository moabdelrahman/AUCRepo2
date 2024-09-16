import math
def isInside(x1,y1,r1,x2,y2,r2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 )
    if r2 >= r1 + dist:
        return True
    else:
        return False

RefCirc = input("enter x,y,r of the reference circle:").split()
refx = int(RefCirc[0])
refy = int(RefCirc[1])
refRad = int(RefCirc[2])
n = int(input("enter number of circles:"))
c=0
for i in range(1,n+1):
    Circ = input("enter data of a circle").split()
    x = int(Circ[0])
    y = int(Circ[1])
    Rad = int(Circ[2])
    if isInside(x,y,Rad,refx,refy,refRad):
        print("this circle is insdie the ref circle")
        c = c+1
    else:
        print("not inside")
print(c, "circles are inside")



