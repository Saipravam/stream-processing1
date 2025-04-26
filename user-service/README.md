from console of STREM-PROCESSING1
execute: 
docker-compose build
docker-compose up

Check the logs, if any failure on user-service
execute - from console of STREM-PROCESSING1\user-service :
docker-compose rm user-service
docker-compose build user-service
docker-compose up user-service

To clean and rebuild:
docker-compose down
docker-compose up

To access FastAPI swagger :
http://127.0.0.1:8000/docs#

To get 