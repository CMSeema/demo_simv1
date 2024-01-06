'''dict = {
  "locationid": "dghf",
  "trialyear": "jfgddhg",
  "trialtypeid": "fjdgf",
  "varietycode": "dhfdh",
  "replication": "r1",
  "l1": "21",
  "l2": "21",
  "l3": "21",
  "l4": "21",
  "canopy": "21",
  "remarks":"sdkjhghjdgf"
}

keys = dict.keys()

inserts = ""
lst =[]

for key in dict.keys():
    if key in ['locationid', 'trialyear', 'trialtypeid', 'varietycode', 'replication']:
        if key == 'replication':
            lst.append(dict.get(key))
        else:
            lst.append(dict.get(key))

lst3 = []
for key in dict.keys():
    lst2 = []
    if key not in ['locationid', 'trialyear', 'trialtypeid', 'varietycode', 'replication']:
        header = inserts
        observationline = key
        observedvalu = dict.get(key)
        lst2.append(key)
        lst2.append(dict.get(key))
        lst3.append(lst2)
    else:
        pass

for sublist in lst3:
    result = []
    result.extend(lst)
    result.extend(sublist)
    print(result)'''

input_data = {
  "locationid": "dghf",
  "trialyear": "jfgddhg",
  "trialtypeid": "fjdgf",
  "varietycode": "dhfdh",
  "replication": "r1",
  "l1": "21",
  "l2": "21",
  "l3": "21",
  "l4": "21",
  "canopy": "21",
  "remarks": "sdkjhghjdgf"
}

# Get the common keys (excluding 'replication')
keys = [key for key in input_data.keys() if key != 'replication']

# Iterate over keys and create combinations
output_list = []
for key in keys:
    output = [input_data["locationid"], input_data["trialyear"], input_data["trialtypeid"],
              input_data["varietycode"], input_data["replication"], key, input_data[key]]
    output_list.append(output)

# Print the result
for item in output_list:
    print(item)



        
