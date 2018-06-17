def readGCfile(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    content = content.split("\n")[3:-1]
    return content

def getAccumilatedFullGCTime(full_gc_times):
    return sum(full_gc_times)

def getAccumilatedMinorGCTime(minor_gc_times):
    return sum(minor_gc_times)


def getFullGCTimes(content):
    full_gc_times = []
    for entry in content:
        row = entry.split()
        if(len(row)>7):
            if((row[2][1:]+" "+row[3])=="Full GC"):
                full_gc_times.append(float(row[-2]))
    return full_gc_times

def getMinorGCTimes(content):
    minor_gc_times = []
    for entry in content:
        row = entry.split()
        if(len(row)>6):
            if((row[2][1:])=="GC"):
                minor_gc_times.append(float(row[-2]))
    return minor_gc_times

def getAccumilatedGCTime(full_gc_times, minor_gc_times):
    return sum(full_gc_times)+sum(minor_gc_times)

def getTotalExecutionTime(content):
    last_gc_entry = content[len(content)-1]
    if(len(last_gc_entry.split())>1):
        return float(last_gc_entry.split()[1][:-1])

def getGCThroughput(total_gc_time, total_execution_time):
    return (1-(total_gc_time/total_execution_time))

def getNumberOfMinorGCPauses(minor_gc_times):
    return len(minor_gc_times)

def getNumberOfFullGCPauses(full_gc_times):
    return len(full_gc_times)

def getNumberOfGCPauses(minor_gc_times, full_gc_times):
    return len(full_gc_times)+len(minor_gc_times)

def getMinPause(minor_gc_times, full_gc_times):
    return (min(min(minor_gc_times), min(full_gc_times)))

def getMaxPause(minor_gc_times, full_gc_times):
    return (max(max(minor_gc_times), max(full_gc_times)))




# content = readGCfile("/home/pasindu/Desktop/GCLogs/GCLogs/100m_Heap_2000_Users_UseSerialGC_collector_GCLog.txt")
# full_gc_times = getFullGCTimes(content)
# minor_gc_times = getMinorGCTimes(content)
#
# print("total_execution_time = " +str(getTotalExecutionTime(content)))
# print("accumilated_full_gc = " +str(getAccumilatedFullGCTime(full_gc_times)))
# print("accumilated_gc = " +str(getAccumilatedGCTime(full_gc_times, minor_gc_times)))
# print("gc_throughput = " +str(getGCThroughput(getAccumilatedGCTime(full_gc_times, minor_gc_times), getTotalExecutionTime(content))))
# print("number_of_minor gc_pauses = " +str(getNumberOfMinorGCPauses((minor_gc_times))))
# print("numer_of_full_gc_pauses = " +str(getNumberOfFullGCPauses(full_gc_times)))