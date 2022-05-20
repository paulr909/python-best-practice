# Database Connections

For Python projects connecting to MySQL based databases:

[https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html](https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html)

```shell
pip install mysql-connector-python
```

The package is available on Windows, macOS and Linux operating systems.

For details on connection setup use this link below:

[https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)

## Examples with Connector/Python
[https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html)

## For installing MySQL locally (All Operating Systems)

Windows: [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/)

MacOS: [https://dev.mysql.com/doc/refman/5.7/en/macos-installation-pkg.html](https://dev.mysql.com/doc/refman/5.7/en/macos-installation-pkg.html)

Linux (Ubuntu): [https://ubuntu.com/server/docs/databases-mysql](https://ubuntu.com/server/docs/databases-mysql) 

### cd into db/seed directory then: Create Test Database

You could run each command individually, but as a package the first 3 scripts can be run together. 
Then run the Drop Database command once tests have completed.

Note that the -m flag represents a Module/Package and the .py extension is not needed to run the below package. 
```shell
python -m create_db
```

### Create Database
```shell
python create_db.py
```

### Create Tables
```shell
python create_tables.py
```

### Seed Database
```shell
python seed_db.py
```

### Drop Database
```shell
python drop_db.py
```