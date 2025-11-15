FROM node:22-alpine AS dev

WORKDIR /app

COPY package*.json /app

RUN npm install

COPY src src
COPY public public

RUN npm run build

CMD ["npm", "start"]

FROM nginx:stable-alpine AS prod

COPY --from=dev /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]