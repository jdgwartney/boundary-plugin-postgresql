#PostgreSQL Plugin for Boundary Premium

##Pre requisites.
**Requires libpq-dev & PythonDev libraries on unix environments.**
**Requires Python, PsycoPG2 module (not currently auto installed)**
*Tested on OSX & Ubuntu, not yet tested on Windows*

The easiest way to install PsycoPG2 is using pip:  
>curl -s https://bootstrap.pypa.io/get-pip.py > get-pip.py  
sudo python get-pip.py  
pip install psycopg2  

##Install as a private plugin (during beta testing)
Use the command:

>curl https://api.graphdat.com/v1/plugins/private/PostgreSQL/leefarrar/BPPostgreSQLPlugin -X PUT -u <your email>:<Your API Token>
  
##Metrics
To limit additional metrics the plugin currently provides the below metrics but can easily be extended to provide per DB metrics
(see code comments) Or make custom collections if required.

**Currently provides these metrics:**  
**Lock Stats:**

+ PSQL\_EXLocks
+ PSQL\_RowExclusive.
+ PSQL\_ShareRowExclusive.
+ PSQL\_ShareUpdateExclusive.
+ PSQL\_Share.
*PSQL\_AccessShare

**Checkpoint/BGWriter stats:**

* PSQL\_ChkPnt\_Wrt_Time.
* PSQL\_ChkPnts_Timed.
* PSQL\_Buffers_Alloc.
* PSQL\_Buffers_Clean.
* PSQL\_Buffers\_Backnd_fSync.
* PSQL\_ChkPnt\_Sync_Time.
* PSQL\_ChkPnts_Req.
* PSQL\_Buffers_Backend.
* PSQL\_MaxWritten_Clean.

**Global DB Stats:**

* PSQL\_Buffers_ChkPnt
* PSQL\_blks_read
* PSQL\_disk_size
* PSQL\_xact_commit
* PSQL\_tup_deleted
* PSQL\_xact_rollback
* PSQL\_blks_hit
* PSQL\_tup_returned
* PSQL\_tup_fetched
* PSQL\_tup_updated
* PSQL\_tup_inserted
