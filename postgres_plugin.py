#!/usr/bin/env python
import sys
import json
from postgresql import PgInfo

#grab connection info's. This is expected in the Format host/port/db/user/pwd
_source=sys.argv[6]
_host = sys.argv[1]
_port = sys.argv[2]
_database = sys.argv[3]
_user = sys.argv[4]
_password = sys.argv[5]

def poll():       
	_dbconn = PgInfo(_host, _port, _database, _user, _password)
	dbs=_dbconn.getDatabases()
	#global stats
	
	writerStats=_dbconn.getBgWriterStats()
	dbLocks= _dbconn.getLockStatsMode()

	#per db stats
	dbStats =_dbconn.getDatabaseStats()
	locksByDB=_dbconn.getLockStatsDB()
	connStats=_dbconn.getConnectionStats()
	
	#print dbLocks
	print "LF_PSQL_EXLocks ", dbLocks['all']['Exclusive'], _source
	print "LF_PSQL_RowExclusive",  dbLocks['all']['RowExclusive'], _source
	print "LF_PSQL_ShareRowExclusive", dbLocks['all']['ShareRowExclusive'], _source
	print "LF_PSQL_ShareUpdateExclusive", dbLocks['all']['ShareUpdateExclusive'], _source
	print "LF_PSQL_Share", dbLocks['all']['Share'], _host
	print "LF_PSQL_AccessShare", dbLocks['all']['AccessShare'], _source
	

poll()

"""_host = "127.0.0.1"
_port = "5432"
_database = "postgres"
_user = "leefarrar"
_password = "Password1"
"""

