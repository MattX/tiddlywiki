# Self-Hosted TiddlyWiki

This repo holds a docker setup for a personal TiddlyWiki.

There are five containers, orchestrated through docker-compose:
 - backup: periodic backup script (TODO)
 - dynamic-dns: script that runs periodically to update my personal IP address with Gandi; (TODO unfinished)
 - nginx: reverse proxy that provides HTTPS and OAuth2 authentication;
 - oauth2-proxy: I use this as an authenticator for nginx. It uses Google OAuth;
 - tiddlywiki: the Tiddly Wiki process itself

The reverse proxy serves directly on port 80/443, and the `dynamic-dns` script sort of assumes this is the only web server running on the system. If I want to add other web apps to this server, I'll probably just add new containers to this repo and wire them with the same reverse proxy.

## Setup

1. Create a file under `/etc/client-secret.txt` containing the OAuth client secret. Make sure you don't have spaces or a newline after the secret!
2. Create a file under `/etc/gandi-api-key.txt` containing the Gandi API key.
3. Generate Let's Encrypt certificates with certbot, and leave them in the default location (`/etc/letsencrypt/live/wiki.terbium.io/`)
4. ??? config for backup
5. Run `docker-compose up --build`

I should look into creating a systemd startup file to start the docker-compose

## TODO

* Finish dynamic-dns script
* Write backup script
* Figure out if there's a nice way to enable certbot auto-renewals
* Find a good Tiddlywiki theme

## Dev notes

Unfortunately the docker-compose file is not super conducive to testing in a local environment.

To generate a self-signed cert:

```shell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx-selfsigned.key -out nginx-selfsigned.crt
```

