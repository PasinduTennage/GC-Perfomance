import sys
from random import randint
from performance.jtlParameters import *
from performance.GCParameters import *
import csv



def getLatencies(jtl_file):
    latencies = []
    data = jtl_file.readlines()
    for line in data[1:]:
        line = line.strip()
        line = line.split(",")
        latencies.append(int(line[13]))
    return latencies

def getTimeStamps(jtl_file):
    timeStamps = []
    data = jtl_file.readlines()
    for line in data[1:]:
        line = line.strip()
        line = line.split(",")
        timeStamps.append(int(line[0]))
    return timeStamps

def getNRandomeColors(n):

    colors = []
    for i in range(n):
        colors.append('%06X' % randint(0, 0xFFFFFF))

    return colors

heap_sizes = ["50m", "100m"]
concurrent_users = [1, 5]
garbage_collectors=("UseSerialGC", "UseParallelGC") #add UseConcMarkSweepGC UseG1GC

jtl_file_root = sys.argv[1]
gc_file_root = sys.argv[2]
output_csv_file = sys.argv[3]

csv_file_records = []
csv_file_records.append("Concurrent Users", "Heap", "Garbage Collector", "Average Latency", "Min Latnecy", "Max Latnecy", "90% Percentile Latency", "95% Percentile Latency", "99% Percentile Latency", "Throughput (Requests per second)", "GC Throughput", "Full GC Pauses", "GC Pauses", "Accumulated Pauses", "Accumulated Full GC Pauses")


for heap in heap_sizes:
    for user in concurrent_users:
        for collector in garbage_collectors:
            jtl_file_name = jtl_file_root+"/"+user+"_users/"+heap+"_heap/"+collector+"_collector/results-measurement.jtl"
            gc_log_name = gc_file_root+"/"+heap+"_Heap_"+user+"_Users_"+collector+"_collector_GCLog.txt"

            jtl_file = open(jtl_file, "r")
            gc_file = open(gc_log_name, "r")

            latencies  = getLatencies(jtl_file)
            timeStamps = getTimeStamps (jtl_file)

            average_latency = getAverageLatency(latencies)
            min_latency = getMinLatency(latencies)
            max_latency = getMaxLatency(latencies)
            percentile_90= getNPercentileLatency(latencies, 90)
            percentile_95 = getNPercentileLatency(latencies, 95)
            percentile_99 = getNPercentileLatency(latencies, 99)
            throughput = getThroughput(timeStamps)

            gc_throughput = getGCThroughput()
            full_gc_pauses = getFullGCPauses()
            gc_pauses = getGCPauses()
            accumulated_pauses = getAccumulatedPauses()
            accumulated_full_gc_pauses = getAccumulatedFullGCPauses()

            csv_file_records.append("Concurrent Users", "Heap", "Garbage Collector", "Average Latency", "Min Latnecy",
                                    "Max Latnecy", "90% Percentile Latency", "95% Percentile Latency",
                                    "99% Percentile Latency", "Throughput (Requests per second)", "GC Throughput",
                                    "Full GC Pauses", "GC Pauses", "Accumulated Pauses", "Accumulated Full GC Pauses")
            row = [user, heap, collector, average_latency, min_latency, max_latency, percentile_90, percentile_95, percentile_99, throughput, gc_throughput, full_gc_pauses, gc_pauses, accumulated_pauses, accumulated_full_gc_pauses]
            csv_file_records.append(row)

with open(output_csv_file, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in csv_file_records:
        writer.writerow(line)







