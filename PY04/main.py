#! venv/bin/python3
import yaml

if __name__ == '__main__':
    with open('pod.yml', 'r') as podfile:
        pod = yaml.safe_load(podfile)
        print(pod)