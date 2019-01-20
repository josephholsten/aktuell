"""

create nlu interpreter
parse incoming queries

required arguments:
  model
  query

$ python console.py model_20190119-124624 "recommend garage rock from 1991"

"""


import argparse
import os
from rasa_nlu.model import Interpreter


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("model", help="name of nlu model")
    parser.add_argument("query", help="input query")
    args = parser.parse_args()
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model_dir = os.path.join(dir_path, "models", "nlu", "default", args.model)
    interpreter = Interpreter.load(model_dir)
    print(interpreter.parse(args.query))
    