# Stage 1: Build the Flutter web application
FROM cirrusci/flutter:3.19.0 as builder

WORKDIR /app

# Copy pubspec.yaml and pubspec.lock first to leverage Docker cache
COPY pubspec.* ./

# Get Flutter packages
RUN flutter pub get

# Copy the rest of the application code
COPY . .

# Build the Flutter web application
RUN flutter build web --release

# Stage 2: Serve the application with Nginx
FROM nginx:alpine

# Copy the built web application from the builder stage
COPY --from=builder /app/build/web /usr/share/nginx/html

# Copy custom Nginx configuration if it exists
# Ensure nginx.conf is present in the frontend_platform_all directory
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]