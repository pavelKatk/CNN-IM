from define_data import definition_data
from preprocessing_data import preprocessing
import numpy as np


definition_data()
preprocessing()
fi = open('result_data.txt')
data = [np.array([float(xs) for xs in x.split(",")]) for x in fi.readlines()]
data = np.array(data).reshape((169,600,3))

fu = open('diagnosis.txt','r')
result = [[int(x)] for x in fu.readlines()]
result_predict = []
k = 0

for i in range(169):
	test_data = np.array(data[i]).reshape(1, 600, 3)
	train_data = data[:i]
	train_data = np.array(np.append(train_data, data[i+1:])).reshape(168, 600, 3)

	test_result = list(result[i])
	train_result = result[:i]
	train_result = np.append(train_result, result[i+1:])
	k = k + 1
	print(k)
	pred = model(train_data, train_result, test_data)

	if pred > 0.5:
		pred = 1

	else:
		pred = 0
	print(pred)
	result_predict.append(pred)

print(result_predict)
with open('pred.txt', 'w') as fw:
	 json.dump(result_predict, fw)
