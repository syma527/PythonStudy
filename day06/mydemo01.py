test_dict = {"host":'192.168.1.1',"port":"332222","user":"root","pwd":"test123"}
port = test_dict['user']

print(port)
res = test_dict.get("host1","test")
print(res)