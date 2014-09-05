PostgreSQL plugin for Boundary Premium
Requires Python, PsycoPG2 module (not currently auto installed)

To limit additional metrics the plugin currently provides the below metrics but can easily be extended to provide per DB metrics
(see code comments) Or make custom collections if required.

Currently provides these metrics:
Lock Stats:
PSQL_EXLocks
PSQL_RowExclusive
PSQL_ShareRowExclusive
PSQL_ShareUpdateExclusive
PSQL_Share
PSQL_AccessShare

Checkpoint/BGWriter stats:
PSQL_ChkPnt_Wrt_Time
PSQL_ChkPnts_Timed
PSQL_Buffers_Alloc
PSQL_Buffers_Clean
PSQL_Buffers_Backnd_fSync
PSQL_ChkPnt_Sync_Time
PSQL_ChkPnts_Req
PSQL_Buffers_Backend
PSQL_MaxWritten_Clean

Global DB Stats
PSQL_Buffers_ChkPnt
PSQL_blks_read
PSQL_disk_size
PSQL_xact_commit
PSQL_tup_deleted
PSQL_xact_rollback
PSQL_blks_hit
PSQL_tup_returned
PSQL_tup_fetched
PSQL_tup_updated
PSQL_tup_inserted
