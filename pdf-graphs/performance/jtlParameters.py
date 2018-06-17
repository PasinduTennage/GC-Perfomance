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