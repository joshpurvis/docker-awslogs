```
# set configs
export AWS_SECRET_ACCESS_KEY=YOURSECRET
export AWS_ACCESS_KEY_ID=YOURID
export AWS_DEFAULT_REGION=us-east-1
export AWS_LOGS_GROUP=YOURLOGGROUP

docker build -t awslogtest .

# run a loop which logs ~20k times
cid=$(docker run -d --log-driver=awslogs --log-opt awslogs-group=$AWS_LOGS_GROUP awslogtest python /test.py)

# logs come back, slightly out of order:
docker run -it -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY awslogstest /usr/bin/python /viewer.py --group=$AWS_LOGS_GROUP --stream=$cid
```
