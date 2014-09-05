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
	dbStats =_dbconn.getDatabaseStats() #also gives individual DB stats
	
	#per db stats - not used in this version
	#locksByDB=_dbconn.getLockStatsDB()
	#connStats=_dbconn.getConnectionStats()
	
	#print writerStats
	#lock stats
	print "LF_PSQL_EXLocks ", dbLocks['all']['Exclusive'], _source
	print "LF_PSQL_RowExclusive",  dbLocks['all']['RowExclusive'], _source
	print "LF_PSQL_ShareRowExclusive", dbLocks['all']['ShareRowExclusive'], _source
	print "LF_PSQL_ShareUpdateExclusive", dbLocks['all']['ShareUpdateExclusive'], _source
	print "LF_PSQL_Share", dbLocks['all']['Share'], _source
	print "LF_PSQL_AccessShare", dbLocks['all']['AccessShare'], _source
	
	#checkpoint/bgwriter stats
	print "LF_PSQL_ChkPnt_Wrt_Time", writerStats['checkpoint_write_time'], _source
	print "LF_PSQL_ChkPnts_Timed", writerStats['checkpoints_timed'], _source
	print "LF_PSQL_Buffers_Alloc", writerStats['buffers_alloc'], _source
	print "LF_PSQL_Buffers_Clean", writerStats['buffers_clean'], _source
	print "LF_PSQL_Buffers_Backnd_fSync", writerStats['buffers_backend_fsync'], _source
	print "LF_PSQL_ChkPnt_Sync_Time", writerStats['checkpoint_sync_time'], _source
	print "LF_PSQL_ChkPnts_Req", writerStats['checkpoints_req'], _source
	print "LF_PSQL_Buffers_Backend", writerStats['buffers_backend'], _source
	print "LF_PSQL_MaxWritten_Clean", writerStats['maxwritten_clean'], _source
	print "LF_PSQL_Buffers_ChkPnt", writerStats['buffers_checkpoint'], _source

	#Global DB Stats
	print "LF_PSQL_blks_read", dbStats['totals']['blks_read'], _source
	print "LF_PSQL_disk_size", dbStats['totals']['disk_size'], _source
	print "LF_PSQL_xact_commit", dbStats['totals']['xact_commit'], _source
	print "LF_PSQL_tup_deleted", dbStats['totals']['tup_deleted'], _source
	print "LF_PSQL_xact_rollback", dbStats['totals']['xact_rollback'], _source
	print "LF_PSQL_blks_hit", dbStats['totals']['blks_hit'], _source
	print "LF_PSQL_tup_returned", dbStats['totals']['tup_returned'], _source
	print "LF_PSQL_tup_fetched", dbStats['totals']['tup_fetched'], _source
	print "LF_PSQL_tup_updated", dbStats['totals']['tup_updated'], _source
	print "LF_PSQL_tup_inserted", dbStats['totals']['tup_inserted'], _source
	print "LF_PSQL_tup_fetched", dbStats['totals']['tup_fetched'], _source

	
	
poll()



