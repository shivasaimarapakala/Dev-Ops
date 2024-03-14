import datetime
import json
import sys
from datetime import datetime


def parse_created(created):
    # Truncate the datetime string to remove extra characters
    created_truncated = created[:23]
    created_datetime = datetime.strptime(created_truncated, "%Y-%m-%dT%H:%M:%S.%f")
    now = datetime.now()
    delta = now - created_datetime
    weeks_ago = delta.days // 7
    return f"{weeks_ago} weeks ago"

def dump_container_desc(container):
    container_id = container['Id'][:12]
    image = container['Config']['Image']
    # Remove semicolon from the end of the command string
    command = ' '.join(container['Config']['Cmd']).rstrip(';')
    created = parse_created(container['Created'])
    status = container['State']['Status']
    ports = ', '.join(container['HostConfig']['PortBindings'].keys()) if container['HostConfig']['PortBindings'] else ''
    name = container['Name'][1:]  # Removing the leading '/'



    print(f"container_id = {container_id}")
    print(f"image = {image}")
    print(f"command = {command}")
    print(f"created = {created}")
    print(f"status = {status}")
    print(f"ports = {ports}")
    print(f"name = {name}")
    




def main():
    # Open the JSON file and read its contents
    with open("t.json", "r") as file:
        json_obj = json.load(file)
    # Pass the JSON object to the dump_container_desc function
    dump_container_desc(json_obj)
    
if __name__ == "__main__":
    main()