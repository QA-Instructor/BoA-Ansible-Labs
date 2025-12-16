#! venv/bin/python3
import yaml

def validate_pod(pod, prefix, port_range):
    valid = True
    for container in pod["spec"]["containers"]: # could be more than one container per pod
        if not container.get("image", "").startswith(prefix): # validate that the image has a given registry prefix
            valid = False
        for port in container.get("ports", dict()): # could be multiple, or no, ports defined
            if not (port_range[0] <= port.get("containerPort", 0) <= port_range[1]): # validate that the containerPort is within the defined range
                valid = False
    return valid

if __name__ == '__main__':
    with open('pod.yml', 'r') as podfile:
        pod = yaml.safe_load(podfile)
        validation = validate_pod(pod, prefix="my-registry.example.io/", port_range=(5000, 10000)) # call the function
        print(validation)