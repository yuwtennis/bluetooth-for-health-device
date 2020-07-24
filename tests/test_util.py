import sys
sys.path.append('../src/')

from util import read_yaml
from const import UUID_LIST

def test_read_yaml():
    assert len(read_yaml('../src/' + UUID_LIST)) > 0
