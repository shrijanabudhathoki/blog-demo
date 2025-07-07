FROM node:18 AS BUILD

WORKDIR /App
COPY . .
RUN npm install
RUN yarn build

FROM nginx:1.27.5-alpine AS PROD

COPY --from=BUILD /App/dist /var/www/html/
COPY --from=BUILD /App/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]