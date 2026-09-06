import server_utils

server1 = {
    "name": "web-01",
    "cpu": 92
}

server_info=server_utils.check_server(server1, 45)
print(server_info)
