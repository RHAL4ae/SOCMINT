# Dockerfile for socmint_dashboard Flutter Web (deployment only)
FROM nginx:alpine
COPY build/web /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]