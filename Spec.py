import psutil
from time import sleep
import subprocess
from win32process import EnumProcesses
from win32process import GetCurrentProcessId




subprocess.call("color a",shell=True)
#cpu
def cpuStats():
	cpuNumbers = psutil.cpu_count()
	cpuFrequence = psutil.cpu_freq()
	cpuUsage = psutil.cpu_percent()

	print("\n\nCPU STATS\n")
	print("Number of cores your cpu has: %d \nFrequency of the processor: %f \nCPU USAGE: %s%s" % (cpuNumbers,cpuFrequence[0],cpuUsage,"%"))



#ram
def memory():
	vMemory = psutil.virtual_memory()
	print("\n\nRAM MEMORY > GB - MB - KB - Byte\n")
	print("Total RAM: %d \nAvaliable RAM: %d \nUSED RAM: %d \nPercent of RAM USED: %d %s \n\n"  %(vMemory[0],vMemory[1],vMemory[3],vMemory[2],"%"))



#disk
def diskSize():
	partitions = psutil.disk_partitions()
	#number of partitions
	partitionCount = 0
	for p in partitions:
		partitionCount +=1
	
	#label of the device ( partition )
	mountPoint = ''
	for i in range(partitionCount):
		mountPoint+=partitions[i][0] + " | "
	
	#size of partition
	pSizes = []
	for i in range(partitionCount):
		#print(psutil.disk_usage(partitions[i][0]))
		pSizes.append(psutil.disk_usage(partitions[i][0]))
	
	#totalMemory
	totalMemory = ''
	for i in range(len(pSizes)):
		totalMemory += str(pSizes[i][0]) + " | "

	print("\nNumber of partitions os the system: %d \nMount Point of the partitions: %s \nTotal Memory on said Paritions : %s \n" % (partitionCount,mountPoint,totalMemory))

#network

def network(): #monitor traffic WIP
	pass


def options():
	choice = input("1. System Monitoring\n2. Kill Process\nSelect option: ")
	return choice



def monitorSystem():
	while True:
		print("\n\n")
		sleep(1)
		subprocess.call("cls",shell=True)
		cpuStats()
		memory()
		network()
		try:
			diskSize()
		except Exception:
			print("A disk has a problem, it may be because it's unusuable (nothing inserted in it)")
		print("\n\n\n\nRunning at 1 cycle a secound")


def processKill():
	killCommand = "taskkill /f /PID "
	processList = EnumProcesses()
	idAndName = {}

	for p in processList:
		idAndName[psutil.Process(p).name()] = p
	
	whoToKill = input("Enter name of the process you want to kill: ")
	whoToKill = whoToKill + ".exe"
	#good matching nothing to do.
	if whoToKill in idAndName.keys():
		print("We are terminating: ",whoToKill)
		killCommand+=whoToKill
		subprocess.call(killCommand,shell=True)
		sleep(10)
		exit()

	#helping user find out the name of the process
	print("\nHere is a hint, try looking it up.\n")
	for key in idAndName.keys():
		if len(key) == len(whoToKill):
			print(key+"\n")

op = options()
if op == "1":
	monitorSystem()
if op == "2":
	processKill()

