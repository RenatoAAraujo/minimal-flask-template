import os

os.system("docker-compose down --volumes --remove-orphans && docker-compose up --build")
