import simpy
from random import randint


class Process():

    def __init__(self):
        self.instructions = randint(1,10)
        self.memory = randint(1,10)
        

class System:
    
    def __init__(self,ram,cpuInstructions):
        self.ram = ram
        self.cpuInstructions = cpuInstructions

    #Method returns an array of n procedures.
    def generateProcess(self,proceduresQt):
        proceduresList = []

        for i in range(proceduresQt):
            newProcess = Process()
            print(str(i+1),". OBJ: "+str(newProcess),"MEMORY GEN: "+str(newProcess.memory))
            proceduresList.append(newProcess)
        print(proceduresList)
        return proceduresList

def RunSystem(env,mainSystem,interval,processQt):
    print("INITIAL RAM: "+str(mainSystem.ram))

    SystemProcedures = mainSystem.generateProcess(processQt) #This will be defaultly the waiting as well

    #for obj in SystemProcedures: #memory checker iterator
    #    print(obj.memory)

    RAM_queue = []
   

    while True:
        for i in range(interval):

            print("=====================")
            print("RAM: "+str(mainSystem.ram))

            try:
                print("Process memory: "+str(SystemProcedures[0].memory))
                print("Process instructions: "+str(SystemProcedures[0].instructions))

                if SystemProcedures[0].memory <= mainSystem.ram:
                    
                    print("Process taken at: "+str(env.now))
                    mainSystem.ram = mainSystem.ram - SystemProcedures[0].memory
                    SystemProcedures.pop(0)
                    RAM_queue.append(SystemProcedures[i])
                
                    print("RAM: "+str(mainSystem.ram))

                else:
                    print("Process could not be taken at: "+str(env.now))
            except:
                pass



        yield env.timeout(1) #READY QUEUE SET

        for i in range(interval):

            try:
                processRunning = RAM_queue[i]

                if processRunning.instructions <= mainSystem.cpuInstructions:
                    print("Process succesfully completed at: "+str(env.now))
                    #Process might now feel free to go
                    RAM_queue.pop(0)

                else:
                    print("Process could not be completed at: "+str(env.now))
                    processRunning.instructions = processRunning.instructions - mainSystem.cpuInstructions
                    print("Restant instructions: "+str(processRunning.instructions))
                    SystemProcedures.append(processRunning)
                    

            except:
                pass

        yield env.timeout(1)







mySystem = System(100,3)
env = simpy.Environment()
env.process(RunSystem(env,mySystem,1,25))
env.run(until=100) #Until, the quantify of processes

#def RunSystem(env,mainSystem,interval,processQt):




