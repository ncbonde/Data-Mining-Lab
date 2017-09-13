import math

def min_max_normalization(data1):
	data=data1[:]
	new_min = int(input('Enter new_min:-'))
	new_max = int(input('Enter new_max:-'))
	max_in_data = max(data)
	min_in_data = min(data)
	number_of_elements = len(data)

	for i in range(0,number_of_elements):
		data[i]= ((data[i]-min_in_data)/(max_in_data-min_in_data)) * (new_max-new_min) + new_min

	return data

def variance(data):
	if len(data)==0:
		return None
	number_of_elements = len(data)
	mean_of_data = sum(data)/number_of_elements	
	_sum=0
	for i in range(0,number_of_elements):
		_sum+=(data[i]-mean_of_data)**2
	data_variance = (1/(number_of_elements-1) * _sum)
	return data_variance
	

def zs_normalization(data1):
	data=data1[:]
	number_of_elements = len(data)
	mean_of_data = sum(data)/number_of_elements
	data_standard_deviation = (variance(data))**0.5
	
	for i in range(0,number_of_elements):
		data[i]= (data[i]-mean_of_data)/data_standard_deviation

	return data


if __name__=="__main__":
	data = list(map(int,input('Enter Elements: ').split()))
	print('Data Before Normalization:-')
	print(data)	
	dataz = zs_normalization(data)
	print('Data after z-score Normalized Data:-')
	print(dataz)
	datam=min_max_normalization(data)
	print('Data after min-max Normalized Data:-')
	print(datam)


