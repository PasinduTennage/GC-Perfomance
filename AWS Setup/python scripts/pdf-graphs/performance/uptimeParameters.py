def getLoadAverages(uptime_file_output):
    load_averages = {}
    file = open(uptime_file_output, "r")
    line = file.readlines()[0].strip()
    content = line.split(",")
    load_averages[15] = content[len(content)-1].strip()
    load_averages[5] = content[len(content) - 2].strip()
    load_averages[1] = content[len(content) - 3].replace("load average:", "").strip()
    return load_averages
