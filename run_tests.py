import os

print("\n#### Checking test coverage! ####")
os.system("docker-compose exec api pytest --cov=app tests/")
print("#### Runnig unit tests! ####")
os.system("docker-compose exec api pytest -v -c tests/pytest.ini")
