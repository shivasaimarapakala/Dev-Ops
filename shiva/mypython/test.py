import json

filename = "t.json"
file = open(filename)
# print(type(file))

json_obj = json.load(file)
file.close()

# print(type(json_obj))

print(json.dumps(json_obj,sort_keys=True,indent=4))
# print(json_obj.keys())

# print(json_obj["Id"][:12])

Id = json_obj["Id"][:12]

image = json_obj['Image']

# print(json_obj["Config"].keys())
# print(json_obj['Config']['Cmd'])
command = json_obj['Config']['Cmd']

# print(json_obj['State'].keys())

created = json_obj['State']['StartedAt']
status = json_obj['State']['FinishedAt']    

# print(json_obj['NetworkSettings'].keys())
Ports = json_obj['NetworkSettings']['Ports']

names = json_obj['Name']

print(f' ID         : {Id}')
print(f' Image      : {image}')
print(f' Command    : {command}')
print(f' Created    : {created}')
print(f' status     : {status}')
print(f' Ports      : {Ports}')
print(f' names      : {names}')



# if type(json_obj["Config"]) == type(json_obj):
#     print("True")

# print(json_obj['Name'])
