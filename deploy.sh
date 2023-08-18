#! /bin/sh
docker stop eportal
docker rm eportal
docker rmi askunlimited/eportal:latest
docker pull askunlimited/eportal:latest
docker run -t -d -p 80:8000 --name=eportal --env-file ./.env askunlimited/eportal:latest
#  chmod a+x deply.sh

# HOST = 139.59.139.220
# ROOT = root
# USER = django