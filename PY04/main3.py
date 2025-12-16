#! venv/bin/python3
import yaml
import json # add this import

def validate_pod(pod, prefix, port_range):
    valid = True
    results = {"validation results": []} # create dict to hold results
    with open("status_report.json", 'w') as outfile: # open json file
        for container in pod["spec"]["containers"]:
            if not container.get("image", "").startswith(prefix):
                valid = False
                results['validation results'].append({f'{container.get("name")} image validation': {'status': 'failed', 'reason': f'image {container.get("image")} not from expected registry: {prefix}'}}) # add the validation result and reason to outputs
            else:
                results['validation results'].append({f'{container.get("name")} image validation': {'status': 'passed', 'reason': f'image {container.get("image")} from expected registry: {prefix}'}})
            for port in container.get("ports", dict()):
                if not (port_range[0] <= port.get("containerPort", 0) <= port_range[1]):
                    valid = False
                    results['validation results'].append({f'{container.get("name")} port validation': {'status': 'failed', 'reason': f'port {port.get("containerPort")} not in range {port_range[0]} - {port_range[1]}'}})
                else:
                    results['validation results'].append({f'{container.get("name")} port validation': {'status': 'passed', 'reason': f'port {port.get("containerPort")} in required range {port_range[0]} - {port_range[1]}'}})
        json.dump(results, outfile, indent=2) # write out the results
        return valid
    

if __name__ == '__main__':
    with open('pod.yml', 'r') as podfile:
        pod = yaml.safe_load(podfile)
   
        validation = validate_pod(pod, prefix="my-registry.example.io/", port_range=(5000, 10000)) # call the function
        print(validation)

        validation2 = validate_pod(pod, prefix="", port_range=(80, 100)) # call the function with valid values
        print(validation2)

        if validation:
            print("all validations passed")
        else:
            print("validation failed - see status_report.json for details")