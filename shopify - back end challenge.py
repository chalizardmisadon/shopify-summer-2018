#main problem --------------------------------------------------------
import json #python 3 comes with json library
import urllib3 #remember to pip install urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #disable insecure warning

current_page = 1 #read first webpage
menus = [] #declare blank menus
newData = [1] #need to declare newData outside while loop

while (newData != []): #check if current_page has data
    url = "https://backend-challenge-summer-2018.herokuapp.com/" \
          "challenges.json?id=1&page=" + str(current_page) #set url
    webSource = urllib3.PoolManager().request("GET", url) #get data
    data = json.loads(webSource.data) #convert json to dict
    newData = data["menus"] #read newData
    menus += newData #add to menus
    current_page += 1 #read next webpage

##for node in menus:
##    print(node)
##print()

def check_cyclical(current_id, parent_list):
    node = menus[current_id-1] #read current node data
    menus[current_id-1] = {} #clear node data (so won't be read later)
    parent_list.append(current_id) #add to parent list
    child_list = []
    valid = True
    
    for child_id in node["child_ids"]:
        if child_id in parent_list: #if child_id is a cyclical references
            return False, [current_id] #return current child
        else: #check for its childs
            check, childs = check_cyclical(child_id, parent_list)
            valid = valid and check #verify child_ids
            child_list = child_list + childs #add childs into child_list
    child_list = [current_id]+child_list #add self into child_list
    return valid, child_list #return states of its childs

outData = {"valid_menus":[], "invalid_menus":[]} #set up dictionary

for node in menus: #go through nodes
    if (0 < len(node)): #check if node has been read
        cycle, children = check_cyclical(node["id"], [])
        root_id = children[0] #get root_id (first in list)
        if (cycle): #add valid_menus
            outData["valid_menus"].append({"root_id":root_id, "children":children[1:]})
        else: #add invalid_menus
            outData["invalid_menus"].append({"root_id":root_id, "children":children})

jsonOut = json.dumps(outData) #convert dict to json
print(jsonOut) #print to shell since challenge did not specify how to output
print()

##---------------------------------------------------------------------------
#Extra challenge

current_page = 1 #read first webpage
menus = [] #declare blank menus
newData = [1] #need to declare newData outside while loop

while (newData != []): #check if current_page has data
    url = "https://backend-challenge-summer-2018.herokuapp.com/" \
          "challenges.json?id=2&page=" + str(current_page) #set url
    webSource = urllib3.PoolManager().request("GET", url) #get data
    data = json.loads(webSource.data) #convert json to dict
    newData = data["menus"] #read newData
    menus += newData #add to menus
    current_page += 1 #read next webpage

##for node in menus:
##    print(node)
##print()

outData = {"valid_menus":[], "invalid_menus":[]} #set up dictionary

for node in menus: #go through nodes
    if (0 < len(node)): #check if node has been read
        cycle, children = check_cyclical(node["id"], [])
        root_id = children[0] #get root_id (first in list)
        children.sort() #sort children_ids just in case challenge requires
        if (cycle): #add valid_menus
            outData["valid_menus"].append({"root_id":root_id, "children":children[1:]})
        else: #add invalid_menus
            outData["invalid_menus"].append({"root_id":root_id, "children":children})


jsonOut = json.dumps(outData) #convert dict to json
print(jsonOut) #print to shell since challenge did not specify how to output
print()

##-------------------------------------------------------------------
#Test example to confirm consistency
##data = {
##  "menus":[
##    {
##      "id":1,
##      "data":"House",
##      "child_ids":[3]
##    },
##    {
##      "id":2,
##      "data":"Company",
##      "child_ids":[4]
##    },
##    {
##      "id":3,
##      "data":"Kitchen",
##      "parent_id":1,
##      "child_ids":[5]
##    },
##    {
##      "id":4,
##      "data":"Meeting Room",
##      "parent_id":2,
##      "child_ids":[6]
##    },
##    {
##      "id":5,
##      "data":"Sink",
##      "parent_id":3,
##      "child_ids":[1]
##    },
##    {
##      "id":6,
##      "data":"Chair",
##      "parent_id":4,
##      "child_ids":[]
##    }
##  ],
##  "pagination":{
##    "current_page":1,
##    "per_page":5,
##    "total":19
##  }
##}
##
##newData = data["menus"] #read newData
##menus = newData #add to menus
##
##outData = {"valid_menus":[], "invalid_menus":[]} #set up dictionary
##
##for node in menus: #go through nodes
##    if (0 < len(node)): #check if node has been read
##        cycle, children = check_cyclical(node["id"], [])
##        root_id = children[0] #get root_id (first in list)
##        children.sort() #sort children_ids just in case challenge requires
##        if (cycle): #add valid_menus
##            outData["valid_menus"].append({"root_id":root_id, "children":children[1:]})
##        else: #add invalid_menus
##            outData["invalid_menus"].append({"root_id":root_id, "children":children})
##
##jsonOut = json.dumps(outData) #convert dict to json
##print(jsonOut) #print to shell since challenge did not specify how to output
##print()
##
