# Development Prepare
## Docker prepare

Reference: https://hub.docker.com/\_/postgres

For archlinux:
```
yay -S docker
systemctl start docker
sudo docker info
sudo docker pull postgres
sudo docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

## SQL
Reference: https://www.postgresql.org/docs/current/index.html
### Create & Enter Database
```
sudo docker start some-postgres
sudo docker exec -it some-postgres bash
root@8fff12486254:/# su postgres
postgres@8fff12486254:/$ createdb mydb
postgres@8fff12486254:/$ psql mydb
psql (14.2 (Debian 14.2-1.pgdg110+1))
Type "help" for help.

mydb=#
```
### [Create tables](./flaskr/schema.sql)

### Recome back
```
sudo docker exec -u postgres -it some-postgres psql mydb
```
# Test go
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
