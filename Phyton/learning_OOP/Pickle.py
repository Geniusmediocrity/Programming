import pickle


a = {1: 2, 3: [1, 2, 3]}
b = pickle.dumps(a)
print(b)