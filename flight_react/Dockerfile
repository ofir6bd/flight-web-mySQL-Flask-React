# Use an official Node runtime as a parent image
FROM node:16-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY flight_react/package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY flight_react .

# Build the React app
RUN npm run build

EXPOSE 3000
# Set the command to run the React app
CMD [ "npm", "start" ]

