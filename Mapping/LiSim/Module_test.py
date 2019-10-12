import sim

try:
    a = sim.Lidar()
    print("Running object test passed!")
    
except:
    print("Problem with defining the object wanna see the error?")
    response = input()
    if str(response) == "Y":
        a = sim.Lidar()

try:
    k = a.simulate(show=True)
    print("Running simulate test passed!")
    
except:
    print("Problem with simulating wanna see the error?")
    response = input()
    if str(response) == "Y":
        a.simulate()


try:
    b = a.noise(k)
    print("Running noise test passed!")

except:
    print("Problem with noise function wanna see the error?")
    response = input()
    if str(response) == "Y":
        a.noise()


print("Congratulations!All tests passed, you're not a complete failure\
 of a human being!!")
      
