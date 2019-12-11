import IMU



dt=1
t = 10
v = 0
pos = 0
for i in range(1,t,dt):
     v += IMU.accelerometre(t)*dt
     pos += v*dt

print(v)
print(pos)
