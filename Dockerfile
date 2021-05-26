FROM centos:latest

ADD /profit_predictor  .

RUN yum install python3 -y  && pip3 install -r requirements.txt

ENTRYPOINT ["./profit_predictor.py"]
