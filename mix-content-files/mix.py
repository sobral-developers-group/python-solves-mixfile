peoples = open("files/people.txt","r").read().split('\n')	
jobs = open("files/job.txt","r").read().split('\n')	

def attr(parameter, index):
	return parameter.split(":")[index].strip()

def auth(people, job):
	return attr(job, 0) == attr(people, 1)

def put(people, job, file):
	file.write("%s:%s\n" %( attr(people, 0), attr(job, 1)))

mix = open("mix.txt","w")

map(
	lambda people: filter(None, map(
		lambda job:  put(people, job, mix) if auth(people, job) else None, jobs)), peoples)

mix.close();


