#!/usr/bin/env python
import sys
import json
from postgresql import PgInfo

#grab connection info's. This is expected in the Format host/port/db/user/pwd
_host = sys.argv[1]
_port = sys.argv[2]
_database = sys.argv[3]
_user = sys.argv[4]
_password = sys.argv[5]
_source = sys.argv[6]

def poll():       
	_dbconn = PgInfo(_host, _port, _database, _user, _password)
	dbs =_dbconn.getDatabases()
	
	#global stats
	writerStats = _dbconn.getBgWriterStats()
	dbLocks = _dbconn.getLockStatsMode()
	dbStats = _dbconn.getDatabaseStats() #also gives individual DB stats
	
	#per db stats - not used in this version
	#locksByDB=_dbconn.getLockStatsDB()
	#connStats=_dbconn.getConnectionStats()
	
	#print writerStats
	#lock stats
	print("POSTGRESQL_EXCLUSIVE_LOCKS", dbLocks['all']['Exclusive'], _source
	print "POSTGRESQL_ROW_EXCLUSIVE_LOCKS",  dbLocks['all']['RowExclusive'], _source
	print "POSTGRESQL_SHARE_ROW_EXCLUSIVE_LOCKS", dbLocks['all']['ShareRowExclusive'], _source
	print "POSTGRESQL_SHARE_UPDATE_EXCLUSIVE_LOCKS", dbLocks['all']['ShareUpdateExclusive'], _source
	print "POSTGRESQL_SHARE_LOCKS", dbLocks['all']['Share'], _source
	print "POSTGRESQL_ACCESS_SHARE_LOCKS", dbLocks['all']['AccessShare'], _source
	
	#checkpoint/bgwriter stats
	print "POSTGRESQL_CHECKPOINT_WRITE_TIME", writerStats['checkpoint_write_time'], _source
	print "POSTGRESQL_CHECKPOINTS_TIMED", writerStats['checkpoints_timed'], _source
	print "POSTGRESQL_BUFFERS_ALLOCATED", writerStats['buffers_alloc'], _source
	print "POSTGRESQL_BUFFERS_CLEAN", writerStats['buffers_clean'], _source
	print "POSTGRESQL_BUFFERS_BACKEND_FSYNC", writerStats['buffers_backend_fsync'], _source
	print "POSTGRESQL_CHECKPOINT_SYNCHRONIZATION_TIME", writerStats['checkpoint_sync_time'], _source
	print "POSTGRESQL_CHECKPOINTS_REQUESTED", writerStats['checkpoints_req'], _source
	print "POSTGRESQL_BUFFERS_BACKEND", writerStats['buffers_backend'], _source
	print "POSTGRESQL_MAXIMUM_WRITTEN_CLEAN", writerStats['maxwritten_clean'], _source
	print "POSTGRESQL_BUFFERS_CHECKPOINT", writerStats['buffers_checkpoint'], _source

	#Global DB Stats
	print "POSTGRESQL_BLOCKS_READ", dbStats['totals']['blks_read'], _source
	print "POSTGRESQL_DISK_SIZE", dbStats['totals']['disk_size'], _source
	print "POSTGRESQL_TRANSACTION_COMMIT", dbStats['totals']['xact_commit'], _source
	print "POSTGRESQL_TUPLES_DELETED", dbStats['totals']['tup_deleted'], _source
	print "POSTGRESQL_TRANSACTION_ROLLBACK", dbStats['totals']['xact_rollback'], _source
	print "POSTGRESQL_BLOCKS_HIT", dbStats['totals']['blks_hit'], _source
	print "POSTGRESQL_TUPLES_RETURNED", dbStats['totals']['tup_returned'], _source
	print "POSTGRESQL_TUPLES_FETCHED", dbStats['totals']['tup_fetched'], _source
	print "POSTGRESQL_TUPLES_UPDATED", dbStats['totals']['tup_updated'], _source
	print "POSTGRESQL_TUPLES_INSERTED", dbStats['totals']['tup_inserted'], _source
	print "POSTGRESQL_TUPLES_FETCHED", dbStats['totals']['tup_fetched'], _source
	
poll()



