FROM node:16-alpine3.13

RUN npm install -g tiddlywiki@5.1.23
RUN mkdir mattwiki
COPY tiddlywiki.info wiki/tiddlywiki.info
COPY plugins wiki/plugins

ENTRYPOINT [ "tiddlywiki", "wiki", "--listen", "host=0.0.0.0" ]
