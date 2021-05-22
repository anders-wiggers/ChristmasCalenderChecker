FROM pytorch/pytorch

WORKDIR /usr/src/app

COPY . ./

RUN pip3 install -r requirements.txt

CMD [ "python3" ,"server/index.py"]
