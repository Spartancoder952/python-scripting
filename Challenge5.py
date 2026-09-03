servers = [
    {
        "name": "web-01",
        "environment": "production",
        "cpu": 92,
        "memory": 70,
        "ip": "10.0.1.10"
    },
    {
        "name": "web-02",
        "environment": "production",
        "cpu": 65,
        "memory": 88
    },
    {
        "name": "web-03",
        "environment": "staging",
        "cpu": 45,
        "memory": 55,
        "ip": "10.0.1.30"
    }
]

for server in servers:
    print(server.get("name"))

    if server.get("cpu") > 85:
        print("HIGH CPU")
    else:
        print("NORMAL CPU")
        
    if server.get("memory") > 85:
        print("HIGH memory")
    else:
        print("Normal memory")
    
    if server.get("ip") is None:
        print("ip doesn't exists")
    else:
        print("IP exists")

    if server.get("cpu") > 85:
        server.update({"alert" : "HIGH CPU"})