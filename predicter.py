from keras.models import load_model
model = load_model('my_model.h5')
import numpy as np
import json, codecs
import sys

inp = sys.argv[1]
inp = json.loads(inp)
x = np.array([inp['data']])
x = x.reshape(1, 28, 28, 1)
#print(x)
#a = np.zeros((1, 28, 28, 1))
res = model.predict(x)
res = json.dumps(res.tolist())
print(res)