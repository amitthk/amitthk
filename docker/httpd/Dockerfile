FROM alpine:latest

COPY entrypoint.sh /entrypoint.sh

RUN apk update && apk upgrade && \
    apk add apache2 libxml2-dev apache2-utils &&\
	chmod 766 /entrypoint.sh

COPY ./html/ /usr/local/apache2/htdocs/

VOLUME /var/www/localhost/htdocs

VOLUME /var/log/apache2

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/etc/init.d/apache2 start"]