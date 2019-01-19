import os
from rasa_nlu.model import Interpreter

model_dir = os.path.join()

interpreter = Interpreter.load(model_dir)
interpreter.parse(u'')
