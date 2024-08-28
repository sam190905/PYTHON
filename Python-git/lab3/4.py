import math

ball1=(4,5,6)
ball2=(5,4,6)
def check_collision(ball1,ball2):
    x1,y1,r1=ball1
    x2,y2,r2=ball2
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    radsum=r1+r2
    return distance<=radsum

print(check_collision(ball1,ball2))

