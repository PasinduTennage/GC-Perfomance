import sys
from random import randint
from jtlParameters import *
from gcParameters import  *
from uptimeParameters import  *

import csv




def getNRandomeColors(n):
    colors = []
    for i in range(n):
        colors.append('%06X' % randint(0, 0xFFFFFF))

    return colors


heap_sizes = ["100m", "1g"]
concurrent_users = [1, 500]
message_sizes= [50, 1024]
garbage_collectors= ["UseSerialGC", "UseG1GC"] #, "UseParallelGC" , "UseConcMarkSweepGC"

jtl_file_root = sys.argv[1]
gc_reports_root = sys.argv[2]
uptime_reports_root = sys.argv[3]
output_csv_file = sys.argv[4]



csv_file_records = []
headers = ['size', 'heap', 'user', 'collector', 'average_latency', 'min_latency', 'max_latency', 'percentile_90', 'percentile_95', 'percentile_99', 'throughput',
                       'footprint', 'footprintAfterFullGC', 'avgFreedMemoryByFullGC', 'avgfootprintAfterGC', 'avgFreedMemoryByGC',
                       'avgPause', 'minPause', 'maxPause', 'avgGCPause', 'avgFullGCPause', 'accumPause', 'fullGCPause',
                       'gcPause', 'gc_throughput', 'num_full_gc', 'num_minor_gc', 'freedMemoryPerMin', 'gcPerformance','fullGCPerformance',
                       'last_one_minutes_la', 'last_five_minutes_la', 'last_fifteen_minutes_la']
csv_file_records.append(headers)



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


                gc_parameters = readGCfile(gc_log_name)

                footprint  = gc_parameters["footprint"]

                footprintAfterFullGC = gc_parameters["footprintAfterFullGC"]

                avgFreedMemoryByFullGC = gc_parameters["avgFreedMemoryByFullGC"]

                avgfootprintAfterGC = gc_parameters["avgfootprintAfterGC"]

                avgFreedMemoryByGC = gc_parameters["avgFreedMemoryByGC"]

                avgPause = gc_parameters["avgPause"]

                minPause = gc_parameters["minPause"]

                maxPause = gc_parameters["maxPause"]

                avgGCPause = gc_parameters["avgGCPause"]

                avgFullGCPause = gc_parameters["avgFullGCPause"]

                accumPause = gc_parameters["accumPause"]

                fullGCPause = gc_parameters["fullGCPause"]

                gcPause = gc_parameters["gcPause"]

                gc_throughput = gc_parameters["throughput"]

                num_full_gc= gc_parameters["Number of full GC"]

                num_minor_gc = gc_parameters["Number of Minor GC"]

                freedMemoryPerMin = gc_parameters["freedMemoryPerMin"]

                gcPerformance = gc_parameters["gcPerformance"]

                fullGCPerformance = gc_parameters["fullGCPerformance"]




                load_averages = getLoadAverages(uptime_file_name)
                last_one_minutes_la = load_averages[1]
                last_five_minutes_la = load_averages[5]
                last_fifteen_minutes_la = load_averages[15]

                row = [size, heap, user, collector, average_latency, min_latency, max_latency, percentile_90, percentile_95, percentile_99, throughput,
                       footprint, footprintAfterFullGC, avgFreedMemoryByFullGC, avgfootprintAfterGC, avgFreedMemoryByGC,
                       avgPause, minPause, maxPause, avgGCPause, avgFullGCPause, accumPause, fullGCPause,
                       gcPause, gc_throughput, num_full_gc, num_minor_gc, freedMemoryPerMin, gcPerformance,fullGCPerformance,
                       last_one_minutes_la, last_five_minutes_la, last_fifteen_minutes_la]
                csv_file_records.append(row)

with open(output_csv_file, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in csv_file_records:
        writer.writerow(line)







