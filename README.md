Boundary PostgreSQL Plugin
==========================

**Awaiting Certification**

Prerequisites
-------------
The following items are required on the host platform in addition to the Boundary Premium [relay](http://premium-support.boundary.com/customer/portal/articles/1635550-plugins---how-to).
* Python 2.6.6 or later
* PsycoPG2 module which the requires the following to install: 
-- PostreSQL libpq-dev 
-- PythonDev 

### Installation of the PsycoPG2 library using pip:
Other methods are available, pip is suggested as the simplest
1. Install [pip](http://pip.readthedocs.org/en/latest/installing.html) if not already installed

     ```bash
      $ curl -s https://bootstrap.pypa.io/get-pip.py > get-pip.py
      $ sudo python get-pip.py
     ```
2. Install the `psycopy2` module

     ```bash
      $ pip install psycopg2
     ```

## Metrics
The plugin currently provides the below indicated metrics below, but can easily be extended to provide per database metrics or custom metrics if required.

### Lock Stats
The following collects regarding database wide locks.

|Metric Name                                    |Metric Identifier                            |Description                                    |
|:----------------------------------------------|:--------------------------------------------|:----------------------------------------------|
|PostgreSQL - Locks Access Share                |POSTGRESQL\_ACCESS\_SHARE\_LOCKS             |PostgreSQL - Locks Access Share                |
|PostgreSQL - Locks Exclusive                   |POSTGRESQL\_EXCLUSIVE\_LOCKS                 |PostgreSQL - Locks Exclusive                   |
|PostgreSQL - Locks Row Exclusive               |POSTGRESQL\_ROW\_EXCLUSIVE\_LOCKS            |PostgreSQL - Locks Row Exclusive               |
|PostgreSQL - Locks Share Row Exclusive         |POSTGRESQL\_SHARE\_ROW\_EXCLUSIVE\_LOCKS     |PostgreSQL - Locks Share Row Exclusive         |
|PostgreSQL - Locks Share Update Exclusive Locks|POSTGRESQL\_SHARE\_UPDATE\_EXCLUSIVE\_LOCKS  |PostgreSQL - Locks Share Update Exclusive Locks|
|PostgreSQL - Locks Share                       |POSTGRESQL\_SHARE\_LOCKS                     |PostgreSQL - Locks Share                       |


### Checkpoint/Background Writer Stats

|Metric Name                                    |Metric Identifier                            |Description                                    |
|:----------------------------------------------|:--------------------------------------------|:----------------------------------------------|
|PostgreSQL - Buffers Allocated                 |POSTGRESQL\_BUFFERS\_ALLOCATED               |PostgreSQL Buffers Allocated                   |
|PostgreSQL - Buffers Backend Fsync             |POSTGRESQL\_BUFFERS\_BACKEND\_FSYNC          |PostgreSQL - Buffers Backend Fsync             |
|PostgreSQL - Buffers Backend                   |POSTGRESQL\_BUFFERS\_BACKEND                 |PostgreSQL - Buffers Backend                   |
|PostgreSQL - Buffers Clean                     |POSTGRESQL\_BUFFERS\_CLEAN                   |PostgreSQL - Buffers Clean                     |
|PostgreSQL - Checkpoints Timed                 |POSTGRESQL\_CHECKPOINTS\_TIMED               |PostgreSQL - Checkpoints Timed                 |
|PostgreSQL - Checkpoint Write Time             |POSTGRESQL\_CHECKPOINT\_WRITE\_TIME          |PostgreSQL Checkpoint Write Time               |
|PostgreSQL - Checkpoint Synchronization Time   |POSTGRESQL\_CHECKPOINT\_SYNCHRONIZATION\_TIME|PostgreSQL - Checkpoint Synchronization Time   |
|PostgreSQL - Checkpoints Requested             |POSTGRESQL\_CHECKPOINTS\_REQUESTED           |PostgreSQL - Checkpoints Requested             |
|PostgreSQL - Maximum Written Clean             |POSTGRESQL\_MAXIMUM\_WRITTEN\_CLEAN          |PostgreSQL - Maximum Written Clean             |

### Global Database Stats

|Metric Name                                    |Metric Identifier                            |Description                                    |
|:----------------------------------------------|:--------------------------------------------|:----------------------------------------------|
|PostgreSQL - Blocks Hit                        |POSTGRESQL\_BLOCKS\_HIT                      |PostgreSQL - Blocks Hit                        |
|PostgreSQL - Blocks Read                       |POSTGRESQL\_BLOCKS\_READ                     |PostgreSQL - Blocks Read                       |
|PostgreSQL - Buffers Checkpoint                |POSTGRESQL\_BUFFERS\_CHECKPOINT              |PostgreSQL - Buffers Checkpoint                |
|PostgreSQL - Disk Size                         |POSTGRESQL\_DISK\_SIZE                       |PostgreSQL - Disk Size                         |
|PostgreSQL - Transaction Committed             |POSTGRESQL\_TRANSACTIONS\_COMMITTED          |PostgreSQL - Transaction Committed             |
|PostgreSQL - Transactions Rolledback           |POSTGRESQL\_TRANSACTIONS\_ROLLEDBACK         |PostgreSQL - Transactions Rolledback           |
|PostgreSQL - Tuples Deleted                    |POSTGRESQL\_TUPLES\_DELETED                  |PostgreSQL - Tuples Deleted                    |
|PostgreSQL - Tuples Fetched                    |POSTGRESQL\_TUPLES\_FETCHED                  |PostgreSQL - Tuples Fetched                    |
|PostgreSQL - Tuples Inserted                   |POSTGRESQL\_TUPLES\_INSERTED                 |PostgreSQL - Tuples Inserted                   |
|PostgreSQL - Tuples Returned                   |POSTGRESQL\_TUPLES\_RETURNED                 |PostgreSQL - Tuples Returned                   |
|PostgreSQL - Tuples Updated                    |POSTGRESQL\_TUPLES\_UPDATED                  |PostgreSQL - Tuples Updated                    |
