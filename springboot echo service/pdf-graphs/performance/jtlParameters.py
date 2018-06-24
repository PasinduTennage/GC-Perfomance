import numpy as np
from scipy.stats.kde import gaussian_kde


def getAverageLatency(latencies):
    # Return average latency of given np array
    return np.average(latencies)

def getMinLatency(latencies):
    # Return min latency of given np array
    return np.min(latencies)

def getMaxLatency(latencies):
    # Return max latency of given np array
    return  np.max(latencies)

def getNPercentileLatency(latencies, N):
    # Return Nth percentile latency of given np array
    return np.percentile(latencies, N)

def getPDF(values):
    # Draws graphs of probability density functions for the given values distribution
    gkde = gaussian_kde(values)
    return gkde

def getThroughput(time_values):
    # Return the throughput
    num_items = len(time_values)
    return 1000*num_items/(time_values[num_items-1]-time_values[0])


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

def getErrorRate(jtl_file_name):
    jtl_file = open(jtl_file_name, "r")
    status = []
    data = jtl_file.readlines()
    for line in data[1:]:
        line = line.strip()
        line = line.split(",")
        status.append(line[3])
    jtl_file.close()
    num_error = 0
    for s in status:
        if( not(s.startswith("20"))):
            num_error = num_error+1
    return 100*(float(num_error)/float(len(status)))

latencies  = getLatencies("/home/pasindu/Desktop/results-measurement.jtl")
timeStamps = getTimeStamps("/home/pasindu/Desktop/results-measurement.jtl")


error_rate = getErrorRate("/home/pasindu/Desktop/results-measurement.jtl")
average_latency = getAverageLatency(np.array(latencies))
min_latency = getMinLatency(np.array(latencies))
max_latency = getMaxLatency(np.array(latencies))
percentile_90= getNPercentileLatency(np.array(latencies), 90)
percentile_95 = getNPercentileLatency(np.array(latencies), 95)
percentile_99 = getNPercentileLatency(np.array(latencies), 99)
throughput = getThroughput(timeStamps)

print(average_latency)
print(min_latency)
print(max_latency)
print(percentile_90)
print(percentile_95)
print(percentile_99)
print(throughput)
print(error_rate)