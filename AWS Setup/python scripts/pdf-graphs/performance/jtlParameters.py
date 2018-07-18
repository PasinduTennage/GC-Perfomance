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


def readDashboard(dashboard_js_file):
    # Return average latency of given np array
    dashboard = open(dashboard_js_file)
    stat_table = ""
    content = dashboard.readlines()

    for line in content:
        if "#statisticsTable" in line:
            stat_table = line
            break

    stat_table = stat_table.strip().split(",")
    jtl_stat = {}
    jtl_stat["error"] =  stat_table[5].strip()
    jtl_stat["average"] = stat_table[6].strip()
    jtl_stat["min"] = stat_table[7].strip()
    jtl_stat["max"] = stat_table[8].strip()
    jtl_stat["percentile_90"] = stat_table[9].strip()
    jtl_stat["percentile_95"] = stat_table[10].strip()
    jtl_stat["percentile_99"] = stat_table[11].strip()
    jtl_stat["throughput"] = stat_table[12].strip()

    return jtl_stat

# print(readDashboard("/home/pasindu/Desktop/test/content/js/dashboard.js"))
