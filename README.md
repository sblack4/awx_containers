# awx containers
Friendlier AWX containers 

## About 
see [AWX](https://github.com/ansible/awx)

The containers for AWX version 5+ require certain config files to run. That is inconvenient as passing these values in through secrets or environmental variables is much easier. Hence this repo. 


## Getting Started 

Follow the AWX install instructions but provide a few secrets as environmental variables:

```
SECRET_KEY=awxsecret
DATABASE_USER=awx
DATABASE_NAME=awx
DATABASE_HOST=my.rds.instance.amazonaws.com
DATABASE_PORT=5432
DATABASE_PASSWORD=mysupersecurepassword12345
MEMCACHED_HOST=memcached
MEMCACHED_PORT=11211
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
AWX_ADMIN_USER=admin
AWX_ADMIN_PASSWORD=awxpassword12345
```
