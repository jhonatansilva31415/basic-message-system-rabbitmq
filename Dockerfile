FROM python:3.9 

WORKDIR /usr/src/app 

ENV PYTHONUNBUFFERED=1 

COPY ./requirements/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
RUN rm requirements.txt

COPY . . 

CMD "make" $RUN_COMMAND
