import sys

def createString(msg_size_in_bytes):
    string = ''
    num_characters = int(msg_size_in_bytes/2)
    for i in range(num_characters):
        string = string + 'a'

    return string

def generatePayloads(message_sizes):
    payloads = []
    for size in message_sizes:
        payloads.append(createString(size))
    return payloads

def writePayLoads(message_sizes, payloads):
    for i in range(len(message_sizes)):
        file_name = output_file_root+str(message_sizes[i])
        file = open(file_name, "w")
        file.write(payloads[i])

output_file_root = sys.argv[1]
message_sizes= [50, 100]
payloads = generatePayloads(message_sizes)
writePayLoads(message_sizes, payloads)
