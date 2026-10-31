# Json : javascript object notation
# used to store and exchange data
# very common in APIs,webapps,databases
# looks like python dictionary
import json
data={
    "name":"Rahul",
    "age":54,
    "skills":['python','sql']
}

json_str=json.dumps(data)
print(json_str)