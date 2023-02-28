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

def RunSystem(env,ram,cpuInstructions,interval,processQt):
    mainSystem = System(100,3)
    print("INITIAL RAM: "+str(mainSystem.ram))
    SystemProcedures = mainSystem.generateProcess(processQt) #This will be defaultly the waiting as well
    RAM_queue = []
    while True:
        for i in range(interval):
            print("YILED 1")
            print("=====================")
            print("RAM: "+str(mainSystem.ram))

            try:
                print("Process memory: "+str(SystemProcedures[0].memory))
                print("Process instructions: "+str(SystemProcedures[0].instructions))

                if SystemProcedures[0].memory <= mainSystem.ram:
                    
                    print("Process taken at: "+str(env.now))
                    mainSystem.ram = mainSystem.ram - SystemProcedures[0].memory
                    RAM_queue.append(SystemProcedures[0])
                    SystemProcedures.pop(0)
                
                    print("RAM: "+str(mainSystem.ram))

                else:
                    print("Process could not be taken at: "+str(env.now))
            except:
                pass



        yield env.timeout(1) #READY QUEUE SET

        for i in range(interval):

            print("YIELD 2")

            try:
                processRunning = RAM_queue[0]

                print("===============")
                print("Instructions: "+str(processRunning.instructions))
                print("INSTRUCTIONS RUNABLE: "+str(mainSystem.cpuInstructions))

                if processRunning.instructions <= mainSystem.cpuInstructions:
                    print("Process succesfully completed at: "+str(env.now))
                    mainSystem.ram = mainSystem.ram + processRunning.memory
                    print("RAM: "+str(mainSystem.ram))
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

#env = environment
#ram = ram memory size
#cpuInstructions = instructions that cpu can run per process
#Interval = interval of processes
#Process = Quant of process (25,50, etc...)


#def RunSystem(env,ram,cpuInstructions,interval,processQt):

env = simpy.Environment()
env.process(RunSystem(env,100,3,5,500))
env.run() #Until




