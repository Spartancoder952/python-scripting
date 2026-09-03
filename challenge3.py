servers = [
    {
        "name": "web-server-01",
        "cpu": 45,
        "memory": 60
    },
    {
        "name": "web-server-02",
        "cpu": 92,
        "memory": 75
    },
    {
        "name": "web-server-03",
        "cpu": 67,
        "memory": 90
    },
    {
        "name": "web-server-04",
        "cpu": 95,
        "memory": 92
    }
]

for server in servers:
    print(f"checking {server["name"]}")
    if server["cpu"] > 85 :
        print("CPU : HIGH")
    else:
        print("CPU : NORMAL")
        
    if server["memory"] > 85 :
        print("Memory : High")
    else:
        print("MEMORY : Normal")
        

# print("Bonus challenge")

for server in servers:
    server["environment"] = "production"

    
print(servers)