import sys

user_id = sys.argv[1] #commandline arg 1 - user id
services = sys.argv[2] #commandline agr 2 - list of services
Strava ={"fixed": ["SRT","CVT","Perkiomen"]}
RWGPS = {"fixed":["CVT","Perkiomen", "Welsh Mountain"]}
Komoot = {"fixed":["SRT","Welsh Mountain","Oaks to Philly"]}
Strava["user"] = [user_id +k for k in Strava["fixed"]]
RWGPS["user"] = [k+user_id for k in RWGPS["fixed"]]
Komoot["user"] = [user_id + k + user_id for k in Komoot["fixed"]]

def allroutes():
	print("All routes:",Strava["fixed"]+RWGPS["fixed"]+Komoot["fixed"])

def uniqueroutes():
	print("Unique routes:",list(set(Strava["fixed"]+RWGPS["fixed"]+Komoot["fixed"])))

def alluserroutes():
	print('For user ' + str(user_id)+ ':%s'% (Strava["user"]+RWGPS["user"]+Komoot["user"]))
	
def userroutesbyservice():
	#services = str(input("Enter services separated by space: "))
	#services = services.split()
	routes = [] #will add to this based on user input and print
	if "Strava" in services:
		routes = routes + Strava["user"]
	if "RWGPS" in services:
		routes = routes + RWGPS["user"]
	if "Komoot" in services:
		routes = routes + Komoot["user"]

	print("For user "+user_id+"  services %s" % routes)	
	
allroutes()
uniqueroutes()
alluserroutes()
userroutesbyservice()
