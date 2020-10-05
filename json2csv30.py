import csv
import json
import os


def combinecsv():
	#writes the header
	csv_header='condition,Condition_cui,label,labe_cui,labe_score,label_semantic_types,label ncts,label_bucket,label_ncts_counts'
	csv_out='combined.csv'
	csv_dir='outputcsv/'
	csv_list=[]
	filenames=os.listdir(r'outputcsv/')
	
	
	for file in filenames:
		loc=[os.path.join(csv_dir,file)]
		
	csv_merge=open(csv_out,'w')
	csv_merge.write(csv_header)
	csv_merge.write('\n')
	for files in loc:
		#print(file)
		csv_in=open(files,'r')
		for line in csv_in:
			if line.startswith(csv_header):
				continue
			csv_merge.write(line)
		csv_in.close()
		csv_merge.close()
	print("verify file "+ csv_out)


	
	f=csv.writer(open(csvoutputfolder+'combined.csv',"w"),delimiter=",")
	for x in data:
		f.writerow(x)	



def jsontocsv(jsonfilepath,csvfilepath):
	#print(jsonfilepath,csvfilepath)
	f=csv.writer(open(csvfilepath,"w"),delimiter=",")
	jsonfile=open(jsonfilepath,"r")
	jsondata=json.load(jsonfile)

	


	count=0
	data=[]
	#for x in jsondata:
	#	f.writerow(x.values())
	#print(jsondata.keys())
	level1key=jsondata.keys()
	for x in level1key: 
		history=[x for x in jsondata[x].keys() if x=="have_had" or x=="looking_for"]
	#print(jsondata["aneurysm"][  x in level])

	#print(jsondata)
	f.writerow(["condition","Condition_cui",'label','labe_cui','labe_score','label_semantic_types','label ncts','label_bucket','label_ncts_counts'])
	for k,val in jsondata.items():	
	# 	#data.append(jsondata.keys())
		for his in history:	
			for y,x in jsondata[k][his].items():
				data.append([k,val["cui"],y,jsondata[k][his][y]["cui"],
					jsondata[k][his][y]["score"],
					jsondata[k][his][y]["label_semantic_types"],
					jsondata[k][his][y]["ncts"],his,
					jsondata[k][his][y]["label_ncts_counts"]])
	
	for x in data:
		f.writerow(x)
	return data



#enter directory with multiple json files
working_dir=r'jsonfiles/'

#lists the files in the directory
file_names=os.listdir(r'jsonfiles/')


data=[]
#loops through each file name
for x in file_names:
	#joins the folder location and file name
	jsonfilepath=os.path.join(working_dir,x)
	#gves the custom file name of output files
	csvfilepath='outputcsv/my{}.csv'.format(x)
	#function call to convert multiple files
	jsontocsv(jsonfilepath,csvfilepath)
	


# function to combine multiple csv files into one
combinecsv()