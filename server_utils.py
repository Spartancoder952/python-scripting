
def check_server(server, threshold=85):
    if server.get("cpu") > threshold:
        status="HIGH-CPU"
    else:
        status="NORMAL-CPU"

    return server.get("name"), status


     

# check_server(server1)
# check_server(server2)
