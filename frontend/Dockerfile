FROM nginx:1.11.10-alpine

# Make it easier to see logs when running with docker-compose
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

# Copy the static assets into place
COPY dist/ /var/www/deploythedocs/frontend/

# Replace the default configuration with our own
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
