import matplotlib
matplotlib.use('Agg')
import numpy as np
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt


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



gkde = []

for i, heap in enumerate(latencies.keys()):
    latency_array = np.array(latencies[heap])
    print("Heap size = "+str(heap)+" Min Latency = "+str(min(latency_array))+" , Max Latency = "+str(max(latency_array)))
    gkde.append(gaussian_kde(latency_array))

# 0 - 50
plt.figure()
for i in range(len(gkde)):
    ind = np.linspace(min(latency_array), 50, 1000)
    kdepdf = gkde[i].evaluate(ind)
    plt.plot(ind, kdepdf, label=heap_sizes[i], color=colors[i])
    plt.legend()

plt.title('Kernel Density Estimation Latency Distribution from 0 to 50')
plt.savefig("/home/wso2/pasindu/apache-jmeter-4.0/bin/results_MS4j_Initial/1000_users/latencyGraph0_50.png")

# 50 - 100
plt.figure()
for i in range(len(gkde)):
    ind = np.linspace(50, 100, 1000)
    kdepdf = gkde[i].evaluate(ind)
    plt.plot(ind, kdepdf, label=heap_sizes[i], color=colors[i])
    plt.legend()

plt.title('Kernel Density Estimation Latency Distribution from 50 to 100')
plt.savefig("/home/wso2/pasindu/apache-jmeter-4.0/bin/results_MS4j_Initial/1000_users/latencyGraph50_100.png")

# 100 - 150
plt.figure()
for i in range(len(gkde)):
    ind = np.linspace(100, 150, 1000)
    kdepdf = gkde[i].evaluate(ind)
    plt.plot(ind, kdepdf, label=heap_sizes[i], color=colors[i])
    plt.legend()

plt.title('Kernel Density Estimation Latency Distribution from 100 to 150')
plt.savefig("/home/wso2/pasindu/apache-jmeter-4.0/bin/results_MS4j_Initial/1000_users/latencyGraph100_150.png")

# 150 - 200
plt.figure()
for i in range(len(gkde)):
    ind = np.linspace(150, 200, 1000)
    kdepdf = gkde[i].evaluate(ind)
    plt.plot(ind, kdepdf, label=heap_sizes[i], color=colors[i])
    plt.legend()

plt.title('Kernel Density Estimation Latency Distribution from 150 to 200')
plt.savefig("/home/wso2/pasindu/apache-jmeter-4.0/bin/results_MS4j_Initial/1000_users/latencyGraph150_200.png")

# 0 - 1000
plt.figure()
for i in range(len(gkde)):
    ind = np.linspace(0, 1000, 1000)
    kdepdf = gkde[i].evaluate(ind)
    plt.plot(ind, kdepdf, label=heap_sizes[i], color=colors[i])
    plt.legend()

plt.title('Kernel Density Estimation Latency Distribution from 0 to 1000')
plt.savefig("/home/wso2/pasindu/apache-jmeter-4.0/bin/results_MS4j_Initial/1000_users/latencyGraph0_1000.png")







