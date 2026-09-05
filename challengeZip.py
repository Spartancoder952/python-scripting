# What zip() is doing

# It pairs the values by position for related lists:





servers = ["web-server-01", "web-server-02", "web-server-03", "web-server-04", "web-server-05"]
cpu = [45, 92, 67, 88, 99]

for server, cpu_usages in zip(servers, cpu):
    if cpu > 85:
        print(server, "-> HIGH CPU")
    else:
        print(server, "-> Normal")