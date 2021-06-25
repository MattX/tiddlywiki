FROM node:16-alpine3.13

RUN npm install -g tiddlywiki@5.1.23
RUN mkdir mattwiki
COPY tiddlywiki.info mattwiki/tiddlywiki.info

ENTRYPOINT [ "tiddlywiki", "mattwiki", "--listen", "host=0.0.0.0" ]
