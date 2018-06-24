import sys
from random import randint
from jtlParameters import *
from gcParameters import  *
from uptimeParameters import  *

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


heap_sizes = ["100m", "1g", "4g"]
concurrent_users = [1, 500, 1000]
message_sizes= [50, 1024]
garbage_collectors= ["UseSerialGC", "UseG1GC", "UseParallelGC"] #, "UseParallelGC" , "UseConcMarkSweepGC"

jtl_file_root = sys.argv[1]
gc_reports_root = sys.argv[2]
uptime_reports_root = sys.argv[3]
output_csv_file = sys.argv[4]



csv_file_records = []
headers = ['size', 'heap', 'user', 'collector', 'average_latency', 'min_latency', 'max_latency', 'percentile_90', 'percentile_95', 'percentile_99', 'throughput',
                       'gc_throughput', 'min_pause', 'max_pause', 'avg_pause', 'num_minor_gc', 'num_full_gc', 'accumulated_minor_gc_pause', 'accumulated_full_gc_pause', 'avg_foot_print_after_full_gc', 'avg_foot_print_after_full_GC_σ',
                       'freed_memory_by_full_GC', 'avg_freed_memory_by_full_GC', 'avg_foot_print_after_GC', 'avg_foot_print_after_GC_σ', 'freed_memory_by_GC', 'avg_freed_memory_by_GC', 'gc_performance', 'full_gc_performance',
                       'last_one_minutes_la', 'last_five_minutes_la', 'last_fifteen_minutes_la']
csv_file_records.append(["Message Size","Heap", "Concurrent Users", "Garbage Collector", "Average Latency", "Min Latnecy", "Max Latnecy", "90% Percentile Latency", "95% Percentile Latency", "99% Percentile Latency", "Throughput (Requests per second)", "GC Throughput", "Full GC Pauses", "Minor GC Pauses", "Accumulated Minor GC Pauses", "Accumulated Full GC Pauses", "Min GC Pause", "Max GC Pause"])



for size in message_sizes:
    for heap in heap_sizes:
        for user in concurrent_users:
            for collector in garbage_collectors:
                jtl_file_name = jtl_file_root+"/"+str(user)+"_users/"+heap+"_heap/"+collector+"_collector/"+str(size)+"_message/results-measurement.jtl"
                gc_log_name = gc_reports_root+"/"+heap+"_Heap_"+str(user)+"_Users_"+collector+"_collector_" +str(size)+"_size_GCReport.csv"
                uptime_file_name = uptime_reports_root+"/uptime_dir/"+heap+"_Heap_"+str(user)+"_Users_"+collector+"_collector_" +str(size)+"_size_uptime.txt"

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

                gc_parameters = readGCfile(gc_log_name)

                gc_throughput = getGCThroughput(gc_parameters)
                min_pause = getMinGCPause(gc_parameters)
                max_pause = getMaxGCPause(gc_parameters)
                avg_pause = getAvgPause(gc_parameters)
                num_minor_gc = getNumMinorGCPauses(gc_parameters)
                num_full_gc = getNumFullGCPauses(gc_parameters)
                accumulated_minor_gc_pause = getAccumilatedMinorGCTime(gc_parameters)
                accumulated_full_gc_pause = getAccumilatedFullGCTime(gc_parameters)
                avg_foot_print_after_full_gc = getAvgfootprintAfterFullGC(gc_parameters)
                avg_foot_print_after_full_GC_σ = getAvgfootprintAfterFullGCσ(gc_parameters)
                freed_memory_by_full_GC = getFreedMemoryByFullGC(gc_parameters)
                avg_freed_memory_by_full_GC = getAvgFreedMemoryByFullGC(gc_parameters)
                avg_foot_print_after_GC = getAvgfootprintAfterGC(gc_parameters)
                avg_foot_print_after_GC_σ = getAvgfootprintAfterGCσ(gc_parameters)
                freed_memory_by_GC = getFreedMemoryByGC(gc_parameters)
                avg_freed_memory_by_GC =  getAvgFreedMemoryByGC(gc_parameters)
                gc_performance =  getGCPerformance(gc_parameters)
                full_gc_performance = getFullGCPerformance(gc_parameters)



                load_averages = getLoadAverages(uptime_file_name)
                last_one_minutes_la = load_averages[1]
                last_five_minutes_la = load_averages[5]
                last_fifteen_minutes_la = load_averages[15]

                row = [size, heap, user, collector, average_latency, min_latency, max_latency, percentile_90, percentile_95, percentile_99, throughput,
                       gc_throughput, min_pause, max_pause, avg_pause, num_minor_gc, num_full_gc, accumulated_minor_gc_pause, accumulated_full_gc_pause, avg_foot_print_after_full_gc, avg_foot_print_after_full_GC_σ,
                       freed_memory_by_full_GC, avg_freed_memory_by_full_GC, avg_foot_print_after_GC, avg_foot_print_after_GC_σ, freed_memory_by_GC, avg_freed_memory_by_GC, gc_performance, full_gc_performance,
                       last_one_minutes_la, last_five_minutes_la, last_fifteen_minutes_la]
                csv_file_records.append(row)

with open(output_csv_file, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in csv_file_records:
        writer.writerow(line)







