#!/usr/bin/env python
import sys
from postgresql import PgInfo

#grab connection info's. This is expected in the Format host/port/db/user/pwd
_host = sys.argv[1]
_port = sys.argv[2]
_database = sys.argv[3]
_user = sys.argv[4]
_password = sys.argv[5]

def poll():       
	_dbconn = PgInfo(_host, _port, _database, _user, _password)
	dbs=_dbconn.getDatabases()
	#global stats
	dbStats =_dbconn.getDatabaseStats()
	writerStats=_dbconn.getBgWriterStats()
	dbLocks= _dbconn.getLockStatsMode()

	#per db stats
	locksByDB=_dbconn.getLockStatsDB()
	connStats=_dbconn.getConnectionStats()

	print "LF_PSQL_DBCount ", len(dbs), _host

poll()

"""_host = "127.0.0.1"
_port = "5432"
_database = "postgres"
_user = "leefarrar"
_password = "Password1"
"""

