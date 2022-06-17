#!/bin/bash
set -e

echo "Init databases restore"
mysql -quiet -uroot -p"$MYSQL_ROOT_PASSWORD" -e 'create database db'

echo "Restoring db"
gunzip < /docker-entrypoint-initdb.d/dumps/db.sql.gz | mysql -quiet -uroot -p"$MYSQL_ROOT_PASSWORD" db

echo "Database restored! ;)"
