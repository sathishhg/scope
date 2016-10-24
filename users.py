from operator import itemgetter

# we can store test data in this module like users

users = [
	{"name": "scope-admin", "username": "sathisha-admin", "password": "sathisha"}
]

def get_user(name):
	try:
		return (user for user in users if user["name"] == name).next()
	except:
		print "\n     User %s is not defined, enter a valid user.\n" %name