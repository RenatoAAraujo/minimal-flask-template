import os

os.system(
    "docker-compose exec -T mysql mysqldump -uroot -proot db > initdb/dumps/db.sql"
)
os.system("gzip -f initdb/dumps/db.sql")
