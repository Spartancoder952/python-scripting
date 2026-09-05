servers = ["web-server-01", "web-server-02", "web-server-03", "web-server-04", "web-server-05" ]
cpu = [45, 92, 67, 88, 99]


for i in range(len(servers)):
    if cpu[i] > 85:
        print(f"checking {servers[i]}")
        print("warning: high cpu utilization")
    else:
        print(f"checking {servers[i]}")
        print("CPU is normal")

print("#############################")

for server, cpu_usage in zip(servers,cpu):   ####zip is only utilized when you have the related lists
    print(server ," ---------->  ", cpu_usage)