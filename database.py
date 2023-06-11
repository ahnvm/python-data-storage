import json

def findpos(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
        returnlist = []
        for item in data:
            if(item["id"] == 0):
                continue
            else:
                returnlist.append(item)  
        return(returnlist)
    except:
        return(returnlist)

def read(filepath,datapos):
    with open(filepath,"r") as f:
        data = json.load(f)
    for item in data:
        if(item["id"] == datapos):
            return(item)


def add(filepath, data):
    with open(filepath,"r") as f:
        temp = json.load(f)
    data["id"] = temp[-1]["id"] +1
    temp.append(data)
    with open(filepath, "w") as f:
        json.dump(temp,f,indent=3)

def update(filepath, dataPos, data):
    with open(filepath,"r") as f:
        temp = json.load(f)
    for item in temp:
        if(item["id"] == dataPos):
            item["id"] = item["id"]
            item["name"] = data["name"]
            item["content"] = data["content"]
    with open(filepath, "w") as f:
        json.dump(temp,f,indent=3)

def delete(filepath, dataPos):
    with open(filepath,"r") as f:
        temp = json.load(f)
    deletepos = 0
    for item in temp:
        if item["id"] == dataPos:
            break
        deletepos +=1
    temp.pop(deletepos)
    with open(filepath, "w") as f:
        json.dump(temp,f,indent=3)