#using the model saved from hard disk 
import pickle 
# load the model from disk
filename = 'rf.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
P = [[62, 70, 3, 1, 0, 136, 5, 7900, 1]]
res = int(loaded_model.predict(P))
P = [[23, 70, 3, 1, 0, 136, 5, 7965, 1]]
res1 = int(loaded_model.predict(P))
print(res," ",res1)