import os

print("#### Executing isort! ####")
os.system("docker-compose exec api isort ./")
print("\n#### Executing black! ####")
os.system("docker-compose exec api black ./")
print("\n#### Executing pylint! ####")
os.system("docker-compose exec api pylint --rcfile=./.pylintrc ./app")
