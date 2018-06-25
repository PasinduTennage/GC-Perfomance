def readGCfile(gc_log_name):
    gc_parameters = {}
    file = open(gc_log_name, "r")
    content = file.readlines()
    for line in content:
        sline = line.replace(",", "")
        entries = sline[:-1].split(";")

        if(entries[0]=="footprint"):
            gc_parameters["footprint"] = entries[1].strip()

        elif(entries[0]=="footprintAfterFullGC"):
            gc_parameters["footprintAfterFullGC"] =  entries[1].strip()

        elif (entries[0] == "avgFreedMemoryByFullGC"):
            gc_parameters["avgFreedMemoryByFullGC"] = entries[1].strip()

        elif (entries[0] == "avgfootprintAfterGC"):
            gc_parameters["avgfootprintAfterGC"] = entries[1].strip()

        elif (entries[0] == "avgFreedMemoryByGC"):
            gc_parameters["avgFreedMemoryByGC"] = entries[1].strip()

        elif (entries[0] == "avgPause"):
            gc_parameters["avgPause"] = entries[1].strip()

        elif (entries[0] == "minPause"):
            gc_parameters["minPause"] = entries[1].strip()

        elif (entries[0] == "maxPause"):
            gc_parameters["maxPause"] = entries[1].strip()

        elif (entries[0] == "avgGCPause"):
            gc_parameters["avgGCPause"] = entries[1].strip()

        elif (entries[0] == "avgFullGCPause"):
            gc_parameters["avgFullGCPause"] = entries[1].strip()

        elif (entries[0] == "accumPause"):
            gc_parameters["accumPause"] = entries[1].strip()

        elif (entries[0] == "fullGCPause"):
            gc_parameters["fullGCPause"] = entries[1].strip()

        elif (entries[0] == "gcPause"):
            gc_parameters["gcPause"] = entries[1].strip()

        elif (entries[0] == "throughput"):
            gc_parameters["throughput"] = entries[1].strip()

        elif (entries[0] == "Number of full GC"):
            gc_parameters["Number of full GC"] = entries[1].strip()

        elif (entries[0] == "Number of Minor GC"):
            gc_parameters["Number of Minor GC"] = entries[1].strip()

        elif (entries[0] == "freedMemoryPerMin"):
            gc_parameters["freedMemoryPerMin"] = entries[1].strip()

        elif (entries[0] == "gcPerformance"):
            gc_parameters["gcPerformance"] = entries[1].strip()

        elif (entries[0] == "fullGCPerformance"):
            gc_parameters["fullGCPerformance"] = entries[1].strip()

    return gc_parameters

# gc_parameters = readGCfile("/home/pasindu/Desktop/100m_Heap_10_Users_UseG1GC_collector_100_size_GCReport.csv")
#
# footprint  = gc_parameters["footprint"]
#
# footprintAfterFullGC = gc_parameters["footprintAfterFullGC"]
#
# avgFreedMemoryByFullGC = gc_parameters["avgFreedMemoryByFullGC"]
#
# avgfootprintAfterGC = gc_parameters["avgfootprintAfterGC"]
#
# avgFreedMemoryByGC = gc_parameters["avgFreedMemoryByGC"]
#
# avgPause = gc_parameters["avgPause"]
#
# minPause = gc_parameters["minPause"]
#
# maxPause = gc_parameters["maxPause"]
#
# avgGCPause = gc_parameters["avgGCPause"]
#
# avgFullGCPause = gc_parameters["avgFullGCPause"]
#
# accumPause = gc_parameters["accumPause"]
#
# fullGCPause = gc_parameters["fullGCPause"]
#
# gcPause = gc_parameters["gcPause"]
#
# gc_throughput = gc_parameters["throughput"]
#
# num_full_gc= gc_parameters["Number of full GC"]
#
# num_minor_gc = gc_parameters["Number of Minor GC"]
#
# freedMemoryPerMin = gc_parameters["freedMemoryPerMin"]
#
# gcPerformance = gc_parameters["gcPerformance"]
#
# fullGCPerformance = gc_parameters["fullGCPerformance"]
#
# print(footprint)
# print(footprintAfterFullGC)
# print(avgFreedMemoryByFullGC)
# print(avgfootprintAfterGC)
# print(avgFreedMemoryByGC)
# print(avgPause)
# print(minPause)
# print(maxPause)
# print(avgGCPause)
# print(avgFullGCPause)
# print(accumPause)
# print(fullGCPause)
# print(gcPause)
# print(gc_throughput)
# print(num_full_gc)
# print(num_minor_gc)
# print(freedMemoryPerMin)
# print(gcPerformance)
# print(fullGCPerformance)