FROM jwilder/docker-gen

# VOLUME ["/var/run/docker.sock:/var/run/docker.sock"]
# COPY /var/run/docker.sock /tmp/docker.sock
RUN mkdir -p /etc/docker-gen/templates/
ADD ./nginx.tmpl /etc/docker-gen/templates/nginx.tmpl


# ENTRYPOINT ["/usr/local/bin/docker-gen", "-notify-sighup", "nginx", "-watch", "-only-exposed", "-wait", "5s:30s", "/etc/docker-gen/templates/nginx.tmpl", "/etc/nginx/conf.d/default.conf"]
