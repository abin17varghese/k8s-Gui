#!/usr/bin/python3
import cgi
import subprocess
import time

print("content-type: text/html")
print()

f=cgi.FieldStorage()

usr_need  = f.getvalue("x")

if ("run" in usr_need  and  "pod" in usr_need and "image" in usr_need ):
    usr_need = usr_need.split()
    image_name = usr_need[4]
    print(image_name) 
    pod_name = usr_need[9]
    print(pod_name)
    cmd = "sudo kubectl run {} --image {} --kubeconfig admin.conf".format(pod_name,image_name)
    print(cmd)
    output = subprocess.getoutput(cmd)
    print(output)


elif ("run" in usr_need  and  "deployment" in usr_need  and "image" in usr_need ):
    usr_need = usr_need.split()  
    
    image_name = usr_need[3]
  
    deployment_name = usr_need[9]

    cmd = "sudo kubectl create deployment  {} --image {} --kubeconfig admin.conf".format( deployment_name ,image_name)
    
    print(cmd)

    output = subprocess.getoutput(cmd)
  
    print(output)

elif ("expose" in usr_need and  "services" in usr_need ):
    usr_need = usr_need.split()

    port_number = usr_need[5]

    deployment_name = usr_need[8]

    cmd = "sudo kubectl expose deployment {} --port={}  --type=NodePort  --kubeconfig admin.conf".format( deployment_name ,port_number)

    output = subprocess.getoutput(cmd)
  
    print(output)

elif ("scale" in usr_need and  "replica" in usr_need and "deployment" in usr_need ):
    usr_need = usr_need.split()

    replica = usr_need[4]

    deployment_name = usr_need[7]

    cmd = "sudo kubectl scale deployment {} --replicas={} --kubeconfig admin.conf".format( deployment_name ,replica)

    output = subprocess.getoutput(cmd)
  
    print(output)

elif ("delete" in usr_need and  "complete" in usr_need and "environment" in usr_need ):

    cmd = "sudo kubectl delete all --all --kubeconfig admin.conf"

    output = subprocess.getoutput(cmd)
  
    print(output)

elif ("delete" in usr_need):
    
    usr_need = usr_need.split()
    
    print(usr_need)
    
    resource_to_be_deleted = usr_need[1]
    
    name_of_resource = usr_need[2]
    
    cmd = "sudo kubectl delete {} {} --kubeconfig admin.conf".format(resource_to_be_deleted, name_of_resource)
    
    output = subprocess.getoutput(cmd)
    
    print(output)

