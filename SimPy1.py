import simpy

#Defiinig a process

def traffic_light(env):
    while True:
        print("Light turned green at t = "+str(env.now)+"s")
        yield  env.timeout(30) #Will stay green for 30 seconds

        print("Light turned yellow at t = "+str(env.now)+"s")
        yield env.timeout(5)

        print("Light turned red at t = " + str(env.now) + "s")
        yield env.timeout(20)

env = simpy.Environment() #Creating environment
env.process(traffic_light(env)) #Setting the process
env.run(until=100) #Time that the simulation wil be ruuning




