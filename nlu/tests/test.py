import pytest
from rasa_nlu.model import Interpreter

"""
The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute.

"""

@pytest.fixture
def nlu_parser():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model_dir = os.path.join(dir_path, "models", "nlu", "default", args.model)
    interpreter = Interpreter.load(model_dir)
    return interpreter

def test_parser(nlu_parser):
    pass