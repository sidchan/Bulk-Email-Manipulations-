import sys
import os
import couchdb
import json

JSON_MBOX=sys.argv[1]
DB=os.path.basename(JSON_MBOX).split('.')[0]
server=couchdb.Server('http://localhost:5984')
db=server.create(DB)
docs=json.loads(open(JSON_MBOX).read())
db.update(docs,all_or_nothing=True)