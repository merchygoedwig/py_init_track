from prettytable import PrettyTable
import json

def dataimport():
    with open("playerdata.json","r") as player_data:
        data=json.load(player_data)
    
    for i in range(len(data)):
        data[i]["id"]=i+1
    return data

def tableprint(data):
    t=PrettyTable(['Index', 'Character Name', 'Initiative Bonus'])
    for i in range(len(data)):    
        t.add_row([data[i]["id"],data[i]["name"],data[i]["bonus"]])
    
    print(t)
    return

def initialise():
    global data
    data=dataimport()
    print('The following data have been initialised from memory:')
    tableprint(data)
    print('There are',len(data),' options available:')