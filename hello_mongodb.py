# program to connect to mongodb using pymongo and returning output on localhost using bottle framework
import bottle

import pymongo

@bottle.route("/")
def index():
     ##connection to the mongodb
     connect = pymongo.MongoClient('localhost', 27017)
     # connect to test databse
     db = connect.test
     #get handle for names collection
     names = db.names
     # find a single document
     item = names.find_one()

     return "hello %s" % item["name"]

bottle.run(host='localhost', port = 8082)
