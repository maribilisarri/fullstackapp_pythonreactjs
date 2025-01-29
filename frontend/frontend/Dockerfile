FROM node:18-alpine
WORKDIR /app
COPY .package*.json /app
RUN yarn install --silent
RUN yarn global add react-scripts@5.0.1
COPY . ./
CMD ["yarn","start"]