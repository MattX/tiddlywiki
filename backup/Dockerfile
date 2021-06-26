FROM alpine:3.14

RUN apk add --no-cache git

COPY backup.sh ./
RUN echo "0 */6 * * * sh /backup.sh" >> /etc/crontabs/root
CMD ["crond", "-f"]
