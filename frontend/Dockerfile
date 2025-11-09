FROM node:22-alpine

WORKDIR /app

COPY package*.json /app

RUN npm install

COPY src src
COPY public public

CMD ["npm", "start"]
