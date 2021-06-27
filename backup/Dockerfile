FROM alpine:3.14

RUN apk add --no-cache git

COPY backup.sh ./
RUN echo "*/15 * * * * sh /backup.sh" >> /etc/crontabs/root
CMD ["crond", "-f"]
