FROM gcc:12.2.0

RUN mkdir /code

WORKDIR /code

COPY . .

RUN  apt update -y
RUN  apt install --no-install-recommends libasio-dev -y
RUN  g++ main.cpp -lpthread -o program.out

ENTRYPOINT ./program.out