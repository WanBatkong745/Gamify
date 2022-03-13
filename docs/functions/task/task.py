import json


from stat import *
from utils import *


class Task:
    def __init__(self, name, *stats):
        self.name = name
        self.stats = stats

        with open('docs/functions/task/config.json', 'r+') as taskJson:
            taskdata = json.load(taskJson)
            if taskdata['tasks'] == []:
                statlst = []
                for stat in stats:
                    values = stat.split(' + ')
                    statname = values[0]
                    statincrease = values[1]
                    tstats = {
                        "stat name": statname,
                        "stat increase": statincrease,
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
                for item in taskdata['tasks']:
                    if item['name'] == name:
                        print("This task already exists.")
                    else:
                        statlst = []
                        for stat in stats:
                            values = stat.split(' + ')
                            statname = values[0]
                            statincrease = values[1]
                            tstats = {
                                "stat name": statname,
                                "stat increase": statincrease,
                            }
                            statlst.append(tstats)
                        newtask = {
                            "name": self.name,
                            "stats": [statlst]
                        }
                        taskdata["tasks"].append(newtask)
                        taskJson.seek(0)
                        json.dump(taskdata, taskJson, indent=4)
