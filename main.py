import json
from os.path import join, isfile
from os import listdir
import os

final_file_name = "yourworldname.points"

def parse(filename):
    try:
        return json.load(filename)
    except ValueError as e:
        print('invalid json: %s' % e)
        return "ERROR - %s \n\n" % e

def take_all_files(path):
    onlyfiles = [ f for f in listdir(path) if isfile(join(path, f))]
    print(onlyfiles)
    percorsi = []
    for file in onlyfiles:
        if ".json" in file:
            percorsi.append(str(path+"/"+file))
    return percorsi

def get_dimensions(dimensions):
    stringa=""
    for dimension in dimensions:
        stringa+=str(dimension)+"#"
    return stringa

def main():
    files = take_all_files("input")
    filesJson =[]
    for file in files:
        with open(file) as f:
            json_imported = parse(f)
            filesJson.append(json_imported)
    lines = []
    lines.append("subworlds:\n")
    lines.append("oldNorthWorlds:\n")
    lines.append("seeds:\n")
    for file in filesJson:
        stringa = "name:"+ file['name']+","

        stringa+=" x:" +str(file['x'])+","
        stringa+=" z:" +str(file['z'])+","
        stringa+=" y:" +str(file['y'])+","

        stringa+="enabled:" +str(file['enable'])+","
        stringa+=" red:" +"0.0,"
        stringa+=" green:" +"0.0,"
        stringa+=" blue:" +"0.0,"

        stringa+="suffix:,"
        stringa+="world:,"
        
        stringa+="dimensions:"+get_dimensions(file['dimensions'])+"\n"

        lines.append(stringa)
    try:
        os.mkdir("output")
    except FileExistsError as e:
        print("directory already exist")
    file = open("output/"+final_file_name,"w+")
    file.writelines(lines)

main()

