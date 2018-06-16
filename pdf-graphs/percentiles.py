import matplotlib
matplotlib.use('Agg')
import numpy as np


heap_sizes = ["100m", "200m", "500m", "1g", "2g", "4g", "8g"]
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
latencies = {}
for heap in heap_sizes:
    file_name = "/home/wso2/pasindu/apache-jmeter-4.0/bin/results_MS4j_Initial/1000_users/"+heap+"_heap/results-measurement.jtl"
    file = open(file_name, "r")
    heap_latencies = []
    data = file.readlines()
    for line in data[1:]:
        line = line.strip()
        line = line.split(",")
        heap_latencies.append(int(line[1]))
    latencies[heap] = heap_latencies





for i, heap in enumerate(latencies.keys()):
    latency_array = np.array(latencies[heap])
    print("Heap size = "+str(heap)+" ,Min Latency = "+str(min(latency_array))+" ,Max Latency = "+str(max(latency_array)) + " ,90% percentile =  "+ str(np.percentile(latency_array, 90)) + " ,95% percentile =  "+ str(np.percentile(latency_array, 95)) + " ,99% percentile =  "+ str(np.percentile(latency_array, 99)))
