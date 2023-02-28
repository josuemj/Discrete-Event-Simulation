import simpy
from random import randint


class Process():

    def __init__(self,):
        self.instructions = randint(1,10)
        self.memory = randint(1,10)
        

class System:
    
    def __init__(self,ram,cpuInstructions):
        self.ram = ram
        self.cpuInstructions = cpuInstructions
        

def RunSystem(env,procedures,System):
    print("INITIAL RAM: "+str(System.ram))

    while True:

        #The process arrives to the system
        print("===============================================")
        randomProcess = Process()
        print("A process has arrived to the system at: "+str(env.now))
        print("This process memory: "+str(randomProcess.memory))
        print("CURRENT RAM MEMORY: "+str(System.ram))

        if randomProcess.memory<=System.ram:
            print("PASO EL PROCESOS A LA RAM")
            System.ram = System.ram-randomProcess.memory
            print("RAM ACTUAL: "+str(System.ram))
        else:
            print("ESTE PROCESO NE MEMES")
        
        yield env.timeout(1)
        print("===============================================")

        #The process checks if can get into RAM


mySystem = System(100,3)

#env = simpy.Environment() #Creating environment
#newQueue = simpy.Resource(env,25)
#env.process(RunSystem(env,25,10,newQueue,mySystem)) #Setting the process

#env.run(until=100) #Time that the simulation wil be ruuning
print(mySystem.ram)

#Running code
env = simpy.Environment()
env.process(RunSystem(env,25,mySystem))
env.run(until=25) #Until, the quantify of processes





