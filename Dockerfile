FROM node:latest

WORKDIR /home/data

COPY . .

RUN npm install

EXPOSE 8080

ENTRYPOINT ["node", "server.js"]