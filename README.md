# Docker prepare

Reference: https://hub.docker.com/\_/postgres

For archlinux:
```
yay -S docker
systemctl start docker
sudo docker info
sudo docker pull postgres
sudo docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

# SQL
Reference: https://www.postgresql.org/docs/current/index.html
## Create database
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
## Create tables
```
CREATE TABLE weather (
    city            varchar(80),
    temp_lo         int,           -- low temperature
    temp_hi         int,           -- high temperature
    prcp            real,          -- precipitation
    date            date
);
CREATE TABLE cities (
    name            varchar(80),
    location        point
);
INSERT INTO weather VALUES ('San Francisco', 46, 50, 0.25, '1994-11-27');
INSERT INTO cities VALUES ('San Francisco', '(-194.0, 53.0)');
INSERT INTO weather (city, temp_lo, temp_hi, prcp, date)
    VALUES ('San Francisco', 43, 57, 0.0, '1994-11-29');
INSERT INTO weather (date, city, temp_hi, temp_lo)
    VALUES ('1994-11-29', 'Hayward', 54, 37);
```
## Come back
```
sudo docker exec -u postgres -it some-postgres psql mydb
```
