def binning_by_mean(data,bins,bin_size,no_of_elements):
	dataset=data[:]
	for bin_no in range(bins):
		if((bin_no+1)*bin_size < no_of_elements):
			mean=sum(dataset[bin_no*bin_size:(bin_no+1)*bin_size])/bin_size
		else:
			mean=sum(dataset[bin_no*bin_size:])/len(dataset[bin_no*bin_size:])
		const=bin_size*bin_no
		for i in range(bin_size):
			if(const+i < no_of_elements):
				dataset[const+i]=mean
	return dataset


def binning_by_range(data,bins,bin_size,no_of_elements):
	dataset=data[:]
	for bin_no in range(bins):
		minimum=dataset[bin_no*bin_size]
		if((bin_no+1)*bin_size < no_of_elements):
			maximum=dataset[(bin_no+1)*bin_size]
		else:
			maximum=dataset[-1]
		const=bin_size*bin_no
		for i in range(1,bin_size-1):
			if(const+i < no_of_elements):
				dis_min=dataset[const+i]-minimum
				dis_max=maximum-dataset[const+i]
				if(dis_min<dis_max):
					dataset[const+i]=minimum
				else:
					dataset[const+i]=maximum
	return dataset

def equiwt_binning(data,bins,bin_size,no_of_elements):
	dataset=data[:]
	for bin_no in range(bins):
		minimum=dataset[bin_no*bin_size]
		if((bin_no+1)*bin_size < no_of_elements):
			maximum=dataset[(bin_no+1)*bin_size]
		else:
			maximum=dataset[-1]
			last=len(dataset[(bin_no)*bin_size:])
		const=bin_size*bin_no
		for i in range(1,bin_size-1):
			if(const+i < no_of_elements):
				if(const+i < no_of_elements):
					dataset[const+i]=(minimum-maximum)*bin_size
				else:
					dataset[const+i]=(minimum-maximum)*last
	return dataset


def print_bins(dataset,bins,bin_size,no_of_elements):
	for bin_no in range(bins):
		print "Elements in bin"+str(bin_no +1)+" :-"
		if((bin_no+1)*bin_size<no_of_elements):
			print dataset[bin_no*bin_size:(bin_no+1)*bin_size]
		else:
			print dataset[bin_no*bin_size:]	
	

if __name__=="__main__":
	data=map(int,raw_input("Enter dataset:-").split())
	bins=int(raw_input("Enter no. of bins to be created:-"))
	data.sort()
	print""
	print "Before binning"
	print data
	
	no_of_elements=len(data)
	if(no_of_elements%bins==0):
		bin_size=no_of_elements/bins
	else:
		bin_size=no_of_elements/bins+1
	mean_binning_data=binning_by_mean(data,bins,bin_size,no_of_elements)
	range_binning_data=binning_by_range(data,bins,bin_size,no_of_elements)
	equiwt_binning_data=equiwt_binning(data,bins,bin_size,no_of_elements)
	print ""	
	print "After Mean binning"
	print_bins(mean_binning_data,bins,bin_size,no_of_elements)
	print ""
	print "After Range binning"
	print_bins(range_binning_data,bins,bin_size,no_of_elements)
	print ""
	print "After EquiWt binning"
	print_bins(equiwt_binning_data,bins,bin_size,no_of_elements)
	print ""
