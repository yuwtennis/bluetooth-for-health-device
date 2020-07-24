import yaml

def read_yaml(file):
    with open(file, 'r') as fd:
        return yaml.load(fd, yaml.FullLoader)
