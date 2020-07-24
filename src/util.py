
import yaml
from typing import Dict

def read_yaml(name: str) -> Dict:
    """Opens yaml file and retun data.

    Args:
        name: File name contains yaml

    Returns:
        Yaml data

    Raises:
        None
    """
    with open(name, 'r') as fd:
        return yaml.load(fd, yaml.FullLoader)
