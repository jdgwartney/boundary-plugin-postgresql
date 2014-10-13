Boundary PostgreSQL Plugin
==========================

**Awaiting Certification**

Prerequisites
-------------
The following items are required on the host platform in addition to the Boundary Premium [relay](http://premium-support.boundary.com/customer/portal/articles/1635550-plugins---how-to).
* Python 2.6.6 or later
* Requires libpq-dev & PythonDev libraries on unix environments.
* Requires Python, PsycoPG2 module (not currently auto installed)

*Tested on OSX & Ubuntu, not yet tested on Windows*

The easiest way to install PsycoPG2 is using pip:  
>curl -s https://bootstrap.pypa.io/get-pip.py > get-pip.py  
sudo python get-pip.py
pip install psycopg2

## Metrics
To limit additional metrics the plugin currently provides the below metrics but can easily be extended to provide per DB metrics
(see code comments) Or make custom collections if required.

### Lock Stats
The following collects regarding database wide locks.

|Metric Name                            |Metric Identifier                          |Description                    |
|:--------------------------------------|:------------------------------------------|:------------------------------|
|PostgreSQL Exclusive Locks             |POSTGRESQL\_EXCLUSIVE\_LOCKS               |                               |
|PostgreSQL Row Exclusive Locks         |POSTGRESQL\_ROW\_EXCLUSIVE\_LOCKS          | |
|PostgreSQL Share Row Exclusive Locks   |POSTGRESQL\_SHARE\_ROW_EXCLUSIVE\_LOCKS    | |
|PostgreSQL Share Update Exclusive Locks|POSTGRESQL\_SHARE\_UPDATE\_EXCLUSIVE\_LOCKS|
|PostgesSQL Share Locks                 |POSTGRESQL\_SHARE\_LOCKS                   | |


+ PSQL\_Share.
PSQL\_AccessShare

### Checkpoint/Background Writer Stats

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
### Global Database Stats

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
