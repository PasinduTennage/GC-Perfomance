heap_sizes = ["100MB", "200MB", "500MB", "1GB", "2GB", "4GB", "8GB"]
latencies = {}
for heap in heap_sizes:
    file_name = "home/wso2/pasindu/apache-jmeter-4.0/bin/results/1000_users/"+heap+"_heap/results-measurement.jtl"
    file = open(file_name, "r")
    heap_latencies = []
    data = file.readlines()
    for line in data:
        line = line.strip()
        line = line.split(",")
        latencies.append(int(line[1]))
    latencies[heap] = heap_latencies



