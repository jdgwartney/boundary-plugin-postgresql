#!/usr/bin/env python
import sys
import json
from postgresql import PgInfo
from os import path
import time

# get params from file
paramFile = "param.json"

if path.isfile(paramFile):
    with open(paramFile) as data_file:
        params = json.load(data_file)
    _host = params["host"]
    _port = params["port"]
    _database = params["database"]
    _user = params["username"]
    _password = params["password"]
    _source = params["source"]

else:
    sys.stderr.write("Either params file is missing or is not readable")
    sys.exit(1)


def poll():
    _dbconn = PgInfo(_host, _port, _database, _user, _password)
    dbs = _dbconn.getDatabases()

    # global stats
    writerStats = _dbconn.getBgWriterStats()
    dbLocks = _dbconn.getLockStatsMode()
    dbStats = _dbconn.getDatabaseStats()  # also gives individual DB stats

    # per db stats - not used in this version
    # locksByDB=_dbconn.getLockStatsDB()
    # connStats=_dbconn.getConnectionStats()

    # print writerStats
    # lock stats
    print("POSTGRESQL_EXCLUSIVE_LOCKS {0} {1}".format(dbLocks['all']['Exclusive'], _source))
    print("POSTGRESQL_ROW_EXCLUSIVE_LOCKS {0} {1}".format(dbLocks['all']['RowExclusive'], _source))
    print("POSTGRESQL_SHARE_ROW_EXCLUSIVE_LOCKS {0} {1}".format(dbLocks['all']['ShareRowExclusive'], _source))
    print("POSTGRESQL_SHARE_UPDATE_EXCLUSIVE_LOCKS {0} {1}".format(dbLocks['all']['ShareUpdateExclusive'], _source))
    print("POSTGRESQL_SHARE_LOCKS {0} {1}".format(dbLocks['all']['Share'], _source))
    print("POSTGRESQL_ACCESS_SHARE_LOCKS {0} {1}".format(dbLocks['all']['AccessShare'], _source))

    # checkpoint/bgwriter stats
    # Check if the key exists before deferencing not all versions of PostgreSQL contains the same stats
    if 'checkpoint_write_time' in writerStats:
        print("POSTGRESQL_CHECKPOINT_WRITE_TIME {0} {1}".format(writerStats['checkpoint_write_time'], _source))
    if 'checkpoints_timed' in writerStats:
        print("POSTGRESQL_CHECKPOINTS_TIMED {0} {1}".format(writerStats['checkpoints_timed'], _source))
    if 'buffers_alloc' in writerStats:
        print("POSTGRESQL_BUFFERS_ALLOCATED {0} {1}".format(writerStats['buffers_alloc'], _source))
    if 'buffers_clean' in writerStats:
        print("POSTGRESQL_BUFFERS_CLEAN {0} {1}".format(writerStats['buffers_clean'], _source))
    if 'buffers_backend_fsync' in writerStats:
        print("POSTGRESQL_BUFFERS_BACKEND_FSYNC {0} {1}".format(writerStats['buffers_backend_fsync'], _source))
    if 'checkpoint_sync_time' in writerStats:
        print("POSTGRESQL_CHECKPOINT_SYNCHRONIZATION_TIME {0} {1}".format(writerStats['checkpoint_sync_time'], _source))
    if 'checkpoints_req' in writerStats:
        print("POSTGRESQL_CHECKPOINTS_REQUESTED {0} {1}".format(writerStats['checkpoints_req'], _source))
    if 'buffers_backend' in writerStats:
        print("POSTGRESQL_BUFFERS_BACKEND {0} {1}".format(writerStats['buffers_backend'], _source))
    if 'maxwritten_clean' in writerStats:
        print("POSTGRESQL_MAXIMUM_WRITTEN_CLEAN {0} {1}".format(writerStats['maxwritten_clean'], _source))
    if 'buffers_checkpoint' in writerStats:
        print("POSTGRESQL_BUFFERS_CHECKPOINT {0} {1}".format(writerStats['buffers_checkpoint'], _source))

    # Global DB Stats
    print("POSTGRESQL_BLOCKS_READ {0} {1}".format(dbStats['totals']['blks_read'], _source))
    print("POSTGRESQL_DISK_SIZE {0} {1}".format(dbStats['totals']['disk_size'], _source))
    print("POSTGRESQL_TRANSACTIONS_COMMITTED {0} {1}".format(dbStats['totals']['xact_commit'], _source))
    print("POSTGRESQL_TUPLES_DELETED {0} {1}".format(dbStats['totals']['tup_deleted'], _source))
    print("POSTGRESQL_TRANSACTIONS_ROLLEDBACK {0} {1}".format(dbStats['totals']['xact_rollback'], _source))
    print("POSTGRESQL_BLOCKS_HIT {0} {1}".format(dbStats['totals']['blks_hit'], _source))
    print("POSTGRESQL_TUPLES_RETURNED {0} {1}".format(dbStats['totals']['tup_returned'], _source))
    print("POSTGRESQL_TUPLES_FETCHED {0} {1}".format(dbStats['totals']['tup_fetched'], _source))
    print("POSTGRESQL_TUPLES_UPDATED {0} {1}".format(dbStats['totals']['tup_updated'], _source))
    print("POSTGRESQL_TUPLES_INSERTED {0} {1}".format(dbStats['totals']['tup_inserted'], _source))

    sys.stdout.flush()


while True:
    poll()
    time.sleep(1)
