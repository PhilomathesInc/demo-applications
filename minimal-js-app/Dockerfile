FROM node:12-alpine
ARG PORT

WORKDIR /usr/src/app
ENV PORT=$PORT

COPY package*.json ./

# Install production dependencies.
RUN npm install --only=production

COPY index.js ./

EXPOSE $PORT

# Run the web service on container startup.
CMD [ "npm", "start" ]
