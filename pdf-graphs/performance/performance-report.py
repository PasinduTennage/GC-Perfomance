import sys
from random import randint
from performance.jtlParameters import *
from performance.gcParameters import *
import csv



def getLatencies(jtl_file_name):
    jtl_file = open(jtl_file_name, "r")
    latencies = []
    data = jtl_file.readlines()
    for line in data[1:]:
        line = line.strip()
        line = line.split(",")
        latencies.append(int(line[13]))
    jtl_file.close()
    return latencies

def getTimeStamps(jtl_file_name):
    jtl_file = open(jtl_file_name, "r")
    timeStamps = []
    data = jtl_file.readlines()
    for line in data[1:]:
        line = line.strip()
        line = line.split(",")
        timeStamps.append(int(line[0]))
    jtl_file.close()
    return timeStamps

def getNRandomeColors(n):

    colors = []
    for i in range(n):
        colors.append('%06X' % randint(0, 0xFFFFFF))

    return colors

heap_sizes = ["100m"]
concurrent_users = [2000]
message_sizes= [50, 1024, 10240, 102400]
garbage_collectors= ["UseSerialGC"] #, "UseParallelGC" , "UseConcMarkSweepGC"

jtl_file_root = sys.argv[1]
gc_file_root = sys.argv[2]
output_csv_file = sys.argv[3]

csv_file_records = []
csv_file_records.append(["Message Size","Heap", "Concurrent Users", "Garbage Collector", "Average Latency", "Min Latnecy", "Max Latnecy", "90% Percentile Latency", "95% Percentile Latency", "99% Percentile Latency", "Throughput (Requests per second)", "GC Throughput", "Full GC Pauses", "Minor GC Pauses", "Accumulated Minor GC Pauses", "Accumulated Full GC Pauses", "Min GC Pause", "Max GC Pause"])

for size in message_sizes:
    for heap in heap_sizes:
        for user in concurrent_users:
            for collector in garbage_collectors:
                jtl_file_name = jtl_file_root+"/"+str(user)+"_users/"+heap+"_heap/"+collector+"_collector/"+str(size)+"_message/results-measurement.jtl"
                gc_log_name = gc_file_root+"/GCLogs/"+heap+"_Heap_"+str(user)+"_Users_"+collector+"_collector_" +str(size)+"_size_GCLog.txt"


                gc_file = open(gc_log_name, "r")

                latencies  = getLatencies(jtl_file_name)
                timeStamps = getTimeStamps (jtl_file_name)



                average_latency = getAverageLatency(np.array(latencies))
                min_latency = getMinLatency(np.array(latencies))
                max_latency = getMaxLatency(np.array(latencies))
                percentile_90= getNPercentileLatency(np.array(latencies), 90)
                percentile_95 = getNPercentileLatency(np.array(latencies), 95)
                percentile_99 = getNPercentileLatency(np.array(latencies), 99)
                throughput = getThroughput(timeStamps)

                # "GC Throughput", "Full GC Pauses", "Minor GC Pauses", "Accumulated Minor GC Pauses", "Accumulated Full GC Pauses", "Min GC Pause", "Max GC Pause"

                content = readGCfile(gc_log_name)
                full_gc_times = getFullGCTimes(content)
                minor_gc_times = getMinorGCTimes(content)

                total_execution_time =  getTotalExecutionTime(content)
                accumilated_full_gc_time =  getAccumilatedFullGCTime(full_gc_times)
                accumilated_minor_gc_time = getAccumilatedGCTime(full_gc_times, minor_gc_times)
                gc_throughput = getGCThroughput(getAccumilatedGCTime(full_gc_times, minor_gc_times), getTotalExecutionTime(content))
                number_of_minor_gc_pauses = getNumberOfMinorGCPauses((minor_gc_times))
                numer_of_full_gc_pauses = getNumberOfFullGCPauses(full_gc_times)
                min_gc_pauses = getMinPause(minor_gc_times, full_gc_times)
                max_gc_pauses = getMaxPause(minor_gc_times, full_gc_times)


                row = [size, heap, user, collector, average_latency, min_latency, max_latency, percentile_90, percentile_95, percentile_99, throughput, gc_throughput, numer_of_full_gc_pauses, number_of_minor_gc_pauses, accumilated_minor_gc_time, accumilated_full_gc_time, min_gc_pauses, max_gc_pauses]
                csv_file_records.append(row)

with open(output_csv_file, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in csv_file_records:
        writer.writerow(line)







