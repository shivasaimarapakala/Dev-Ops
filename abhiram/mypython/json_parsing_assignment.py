
json_obj = {
        "Id": "0b8dccc201b0be71d47ede92cb9e1801069f9e0b39505a7c6a32cabf7ada633a",
        "Created": "2016-12-29T10:30:07.119045211Z",
        "Path": "nginx",
        "Args": [
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "exited",
            "Running": 'false',
            "Paused": 'false',
            "Restarting": 'false',
            "OOMKilled": 'false',
            "Dead": 'false',
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2016-12-29T10:30:07.306439621Z",
            "FinishedAt": "2016-12-29T11:29:11.656689419Z"
        },
        "Image": "sha256:bbea2fdd9bd70486473de13686f0e4ef767a54e27f2bb88c2b1b603f27e989d5",
        "ResolvConfPath": "/var/lib/docker/containers/0b8dccc201b0be71d47ede92cb9e1801069f9e0b39505a7c6a32cabf7ada633a/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/0b8dccc201b0be71d47ede92cb9e1801069f9e0b39505a7c6a32cabf7ada633a/hostname",
        "HostsPath": "/var/lib/docker/containers/0b8dccc201b0be71d47ede92cb9e1801069f9e0b39505a7c6a32cabf7ada633a/hosts",
        "LogPath": "/var/lib/docker/containers/0b8dccc201b0be71d47ede92cb9e1801069f9e0b39505a7c6a32cabf7ada633a/0b8dccc201b0be71d47ede92cb9e1801069f9e0b39505a7c6a32cabf7ada633a-json.log",
        "Name": "/myhttpv1",
        "RestartCount": 0,
        "Driver": "aufs",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": 'null',
        "HostConfig": {
            "Binds": 'null',
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "80"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": 'false',
            "VolumeDriver": "",
            "VolumesFrom": 'null',
            "CapAdd": 'null',
            "CapDrop": 'null',
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": 'null',
            "GroupAdd": 'null',
            "IpcMode": "",
            "Cgroup": "",
            "Links": 'null',
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": 'false',
            "PublishAllPorts": 'false',
            "ReadonlyRootfs": 'false',
            "SecurityOpt": 'null',
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": 'null',
            "BlkioDeviceReadBps": 'null',
            "BlkioDeviceWriteBps": 'null',
            "BlkioDeviceReadIOps": 'null',
            "BlkioDeviceWriteIOps": 'null',
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DiskQuota": 0,
            "KernelMemory": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": -1,
            "OomKillDisable": 'false',
            "PidsLimit": 0,
            "Ulimits": 'null',
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0
        },
        "GraphDriver": {
            "Name": "aufs",
            "Data": 'null'
        },
        "Mounts": [],
        "Config": {
            "Hostname": "0b8dccc201b0",
            "Domainname": "",
            "User": "",
            "AttachStdin": 'false',
            "AttachStdout": 'true',
            "AttachStderr": 'true',
            "ExposedPorts": {
                "443/tcp": {},
                "80/tcp": {}
            },
            "Tty": 'false',
            "OpenStdin": 'false',
            "StdinOnce": 'false',
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "myhttpv1",
            "Volumes": 'null',
            "WorkingDir": "",
            "Entrypoint": 'null',
            "OnBuild": 'null',
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "b36880b7f8db0193b3c3789505653d677d2e0f8e9bc0de23b5b031e2c0339be9",
            "HairpinMode": 'false',
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": 'null',
            "SandboxKey": "/var/run/docker/netns/b36880b7f8db",
            "SecondaryIPAddresses": 'null',
            "SecondaryIPv6Addresses": 'null',
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "MacAddress": "",
            "Networks": {
                "bridge": {
                    "IPAMConfig": 'null',
                    "Links": 'null',
                    "Aliases": 'null',
                    "NetworkID": "46c6a4f3e05c9e7785b581708fc2200a3385294f5fefb7c9f707cdd48a110e92",
                    "EndpointID": "",
                    "Gateway": "",
                    "IPAddress": "",
                    "IPPrefixLen": 0,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": ""
                }
            }
        }
    }

# docker ps -a
# The desired output should be
#CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                   PORTS               NAMES
#0b8dccc201b0        myhttpv1            "nginx -g 'daemon off"   5 weeks ago         Exited (0) 5 weeks ago                       myhttpv1

title = "ACONTAINER ID        IMAGE               COMMAND CREATED             STATUS                   PORTS               NAMES"
a = "0b8dccc201b0"
b = "myhttpv1"


#print (title)
#print (a, b)
#print ("%s %s" % (a, b))

def dump_full_json_obj(myobject):
    print (myobject)
    return 

def dump_container_desc(myobject):
    print ("CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                   PORTS               NAMES")
    print(myobject['Id'])
    print(myobject['Id'][0:12])
    print(myobject['Config'])
    return

def sample_output():
    print ("CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS                   PORTS               NAMES")
    expe_output = """0b8dccc201b0        myhttpv1            "nginx -g 'daemon off"   5 weeks ago         Exited (0) 5 weeks ago myhttpv1"""
    print (expe_output)
    print ()

def main():
    # dump_full_json_obj(json_obj)
    # sample_output()
    # dump_container_desc(json_obj)
    return()

if (__name__ == "__main__"):
    main()
    


########code
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

    print(f"{container_id:<20} {image:<20} {command:<24} {created:<20} {status:<24} {ports:<20} {name}")


def main():
    dump_container_desc(json_obj)
if __name__ == "__main__":
    main()