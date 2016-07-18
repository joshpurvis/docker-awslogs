FROM ubuntu:14.04.4
RUN apt-get update && apt-get install python-dev python-pip -y
RUN pip install pip boto3 --upgrade 
 
ENV AWS_ACCESS_KEY_ID XXX
ENV AWS_SECRET_ACCESS_KEY XXX
ENV AWS_DEFAULT_REGION us-east-1

COPY test.py /test.py
COPY viewer.py /viewer.py
CMD ["/usr/bin/python"]
