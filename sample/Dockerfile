FROM python:3

USER root
RUN apt-get update && apt-get upgrade -y
RUN apt-get install make

RUN useradd -ms /bin/bash -u 4000 executor
ADD Makefile /home/executor/imported/
ADD requirements.txt /home/executor/imported/
ADD sample.py /home/executor/imported/
RUN mkdir /home/executor/inputs/
RUN mkdir /home/executor/outputs/
RUN chown -R executor /home/executor/
USER executor
WORKDIR /home/executor/imported/

RUN make init
ENTRYPOINT ["python3", "sample.py"]
