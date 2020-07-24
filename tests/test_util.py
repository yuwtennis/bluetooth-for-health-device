import sys
sys.path.append('../')

from src.util import *
from src.const import *

def test_read_yaml():
    assert len(read_yaml('../src/' + UUID_LIST)) > 0
