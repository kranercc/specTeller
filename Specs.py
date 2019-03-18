import psutil
from time import sleep
import subprocess
subprocess.call("color a",shell=True)
#cpu
def cpuStats():
	cpuNumbers = psutil.cpu_count()

	cpuFrequence = psutil.cpu_freq()

	cpuUsage = psutil.cpu_percent()
	print("\n\nCPU STATS")
	print("Number of cores your cpu has: %d | Frequency of the processor: %f \nCPU USAGE: %s%s" % (cpuNumbers,cpuFrequence[0],cpuUsage,"%"))

#ram
def memory():
	vMemory = psutil.virtual_memory()
	print("\nRAM MEMORY > GB - MB - KB - Byte")
	print("Total RAM: %d | Avaliable RAM: %d | USED RAM: %d | Percent of RAM USED: %d %s \n"  %(vMemory[0],vMemory[1],vMemory[3],vMemory[2],"%"))

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

	print("\nNumber of partitions os the system: %d | Mount Point of the partitions: %s and Total Memory of Paritions : %s \n" % (partitionCount,mountPoint,totalMemory))

#network

while True:
	print("\n\n")
	sleep(1)
	subprocess.call("cls",shell=True)
	cpuStats()
	memory()
	diskSize()
	#network()
	print("\n\n\n\n\n\nRunning at 1 cycle a secound")
