import matplotlib
matplotlib.use('Agg')
import numpy as np
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt


heap_sizes = ["100m", "200m", "500m", "1g", "2g", "4g", "8g"]
colors = ['r', 'b', 'y', 'g', 'r', 'c', 'm']
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


plt.figure()

for i, heap in enumerate(latencies.keys()):
    latency_array = np.array(latencies[heap])
    gkde = gaussian_kde(latency_array)
    ind = np.linspace(min(latency_array), 50, 1000)
    kdepdf = gkde.evaluate(ind)
    plt.plot(ind, kdepdf, label=heap_sizes[i], color=colors[i])
    plt.title('Kernel Density Estimation Latency Distribution')
    plt.legend()




plt.savefig("/home/wso2/pasindu/apache-jmeter-4.0/bin/results_MS4j_Initial/1000_users/latencyGraph.png")
