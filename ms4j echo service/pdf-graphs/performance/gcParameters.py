def readGCfile(gc_log_name):
    gc_parameters = {}
    file = open(gc_log_name, "r")
    content = file.readlines()
    for line in content:
        sline = line.replace(",", "")
        entries = sline[:-1].split(";")

        if(entries[0]=="throughput"):
            gc_parameters["throughput"] = entries[1].strip()

        elif(entries[0]=="Number of full GC"):
            gc_parameters["num_full_gc"] =  entries[1].strip()

        elif (entries[0] == "Number of Minor GC"):
            gc_parameters["num_minor_gc"] = entries[1].strip()

        elif (entries[0] == "minPause"):
            gc_parameters["min_pause"] = entries[1].strip()

        elif (entries[0] == "maxPause"):
            gc_parameters["max_pause"] = entries[1].strip()

        elif (entries[0] == "gcPause"):
            gc_parameters["accumulated_minor_gc_pause"] = entries[1].strip()

        elif (entries[0] == "fullGCPause"):
            gc_parameters["accumulated_full_gc_pause"] = entries[1].strip()

        elif (entries[0] == "avgfootprintAfterFullGC"):
            gc_parameters["avg_foot_print_after_full_gc"] = entries[1].strip()

        elif (entries[0] == "avgfootprintAfterFullGCσ"):
            gc_parameters["avg_foot_print_after_full_GC_σ"] = entries[1].strip()


        elif (entries[0] == "freedMemoryByFullGC"):
            gc_parameters["freed_memory_by_full_GC"] = entries[1].strip()


        elif (entries[0] == "avgFreedMemoryByFullGC"):
            gc_parameters["avg_freed_memory_by_full_GC"] = entries[1].strip()


        elif (entries[0] == "avgfootprintAfterGC"):
            gc_parameters["avg_foot_print_after_GC"] = entries[1].strip()


        elif (entries[0] == "avgfootprintAfterGCσ"):
            gc_parameters["avg_foot_print_after_GC_σ"] = entries[1].strip()


        elif (entries[0] == "freedMemoryByGC"):
            gc_parameters["freed_memory_by_GC"] = entries[1].strip()


        elif (entries[0] == "avgFreedMemoryByGC"):
            gc_parameters["avg_freed_memory_by_GC"] = entries[1].strip()


        elif (entries[0] == "avgPause"):
            gc_parameters["avg_pause"] = entries[1].strip()


        elif (entries[0] == "gcPerformance"):
            gc_parameters["gc_performance"] = entries[1].strip()


        elif (entries[0] == "fullGCPerformance"):
            gc_parameters["full_GC_performance"] = entries[1].strip()



    return gc_parameters

def getGCThroughput(gc_parameters):
    return gc_parameters["throughput"]

def getMinGCPause(gc_parameters):
    return gc_parameters["min_pause"]

def getMaxGCPause(gc_parameters):
    return gc_parameters["max_pause"]

def getNumMinorGCPauses(gc_parameters):
    return gc_parameters["num_minor_gc"]

def getNumFullGCPauses(gc_parameters):
    return gc_parameters["num_full_gc"]

def getAccumilatedMinorGCTime(gc_parameters):
    return gc_parameters["accumulated_minor_gc_pause"]

def getAccumilatedFullGCTime(gc_parameters):
    return gc_parameters["accumulated_full_gc_pause"]

def getAvgfootprintAfterFullGC(gc_parameters):
    return gc_parameters["avg_foot_print_after_full_gc"]

def getAvgfootprintAfterFullGCσ(gc_parameters):
    return gc_parameters["avg_foot_print_after_full_GC_σ"]

def getFreedMemoryByFullGC(gc_parameters):
    return gc_parameters["freed_memory_by_full_GC"]

def getAvgFreedMemoryByFullGC(gc_parameters):
    return gc_parameters["avg_freed_memory_by_full_GC"]

def getAvgfootprintAfterGC(gc_parameters):
    return gc_parameters["avg_foot_print_after_GC"]

def getAvgfootprintAfterGCσ(gc_parameters):
    return gc_parameters["avg_foot_print_after_GC_σ"]

def getFreedMemoryByGC(gc_parameters):
    return gc_parameters["freed_memory_by_GC"]

def getAvgFreedMemoryByGC(gc_parameters):
    return gc_parameters["avg_freed_memory_by_GC"]

def getAvgPause(gc_parameters):
    return gc_parameters["avg_pause"]

def getGCPerformance(gc_parameters):
    return gc_parameters["gc_performance"]

def getFullGCPerformance(gc_parameters):
    return gc_parameters["full_GC_performance"]