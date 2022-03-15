from asyncio import tasks
import json


import stat
from utils import *


class Task:
    def __init__(self, name, *stats):
        self.name = name
        self.stats = stats
    
        with open('docs/functions/task/config.json', 'r+') as taskJson:
            taskdata = json.load(taskJson)
            if taskdata['tasks'] == []:
                statlst = []
                for stat in self.stats:
                    values = stat.split(' + ')
                    statname = values[0]
                    statincrease = values[1]
                    tstats = {
                        "stat name": statname,
                        "stat xp increase": statincrease,
                    }
                    statlst.append(tstats)
                newtask = {
                    "name": self.name,
                    "stats": [statlst]
                }
                taskdata["tasks"].append(newtask)
                taskJson.seek(0)
                json.dump(taskdata, taskJson, indent=4)
            else:
                for item in taskdata["tasks"]: 
                    if self.name != item["name"]:
                        statlst = []
                        for stat in self.stats:
                            values = stat.split(' + ')
                            statname = values[0]
                            statincrease = values[1]
                            tstats = {
                                "stat name": statname,
                                "stat xp increase": statincrease,
                            }
                            statlst.append(tstats)
                        newtask = {
                            "name": self.name,
                            "stats": [statlst]
                        }
                        taskdata["tasks"].append(newtask)
                        taskJson.seek(0)
                        json.dump(taskdata, taskJson, indent=4)
                    else:
                        typing_print("This task already exists.")
                    

    def run_task(self):
        with open('docs/functions/task/log.json', 'r+') as logJson:
            logdata = json.load(logJson)
            for task in logdata:
                if logdata["log"] == []:
                    newlog = {
                        "task name": self.name,
                        "number of completions": 1
                    }
                    logdata["log"].append(newlog)
                    logJson.seek(0)
                    json.dump(logdata, logJson, indent=4)
                else:
                    for name in task["task name"]:
                        new_num = name["number of completions"]
                        if name == self.name:
                            new_num += 1
                            newlog = {
                                "task name": self.name,
                                "number of completions": new_num
                            }