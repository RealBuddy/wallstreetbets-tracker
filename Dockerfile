    FROM python:3.8

COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENV TZ=America/New_York

RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

COPY ./ /app

WORKDIR /app

CMD ["bash"]

#docker run --link tradingplatform_timescaledb_1:database --net tradingplatform_default -v "$PWD":/app -it  wallstreetbetstracker:latest