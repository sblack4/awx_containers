# awx containers
[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/sblack4/awx_task?label=awx_task%20docker%20build)](https://cloud.docker.com/repository/docker/sblack4/awx_task)
[![Docker Pulls](https://img.shields.io/docker/pulls/sblack4/awx_task?label=awx_task%20docker%20pulls)](https://cloud.docker.com/repository/docker/sblack4/awx_task)
[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/sblack4/awx_web?label=awx_web%20docker%20build)](https://cloud.docker.com/u/sblack4/repository/docker/sblack4/awx_web)
[![Docker Pulls](https://img.shields.io/docker/pulls/sblack4/awx_web?label=awx_web%20docker%20pulls)](https://cloud.docker.com/u/sblack4/repository/docker/sblack4/awx_web)

Friendlier AWX containers 

## About 
see [AWX](https://github.com/ansible/awx)

The containers for AWX version 5+ require certain config files to run. That is inconvenient as passing these values in through secrets or environmental variables is much easier. Hence this repo. 


## Getting Started 

Follow the AWX install instructions but provide a few secrets as environmental variables. 
Not all of these are necessary as some can use defaults. 

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
