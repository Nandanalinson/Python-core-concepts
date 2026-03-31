# JSON (javascript object notation)
#==================================
# light weight format data transfer through internet


# API (application programming intergface)
#=========================================
# communication in between two or more application 
# (request and response) entirely in json format


import json

data = {
    "employee" : {
        "name" : "john",
        "age"  : 30,
        "city" : "New York",
        "Skills" : ["javascript", "python"]
    }
}


print(type(data))       # <class 'dict'>

data_n = json.dumps(data)  # converting dict (our native) to json

print(data_n)       # {"employee": {"name": "john", "age": 30, "city": "New York", "Skills": ["javascript", "python"]}}

print(type(data_n))     # <class 'str'>

new = json.loads(data_n) # convert json to our native (here , dicitionary)

print(type(new))        # <class 'dict'>

# all these above process is called serialization and deserialization