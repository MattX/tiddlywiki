# Self-Hosted TiddlyWiki

This repo holds a docker setup for a personal TiddlyWiki.

There are five containers, orchestrated through docker-compose:
 - backup: periodic backup script
 - dynamic-dns: script that runs periodically to update my personal IP address with Gandi; (TODO unfinished)
 - nginx: reverse proxy that provides HTTPS and OAuth2 authentication;
 - oauth2-proxy: I use this as an authenticator for nginx. It uses Google OAuth;
 - tiddlywiki: the Tiddly Wiki process itself

The reverse proxy serves directly on port 80/443, so I assume this is the only web server running on the system. If I want to add other web apps to this server, I'll probably just add new containers to this repo and wire them through the same reverse proxy.

The Tiddlywiki install contains [the TWCrossLinks](https://github.com/akhater/TWCrossLinks) plugin.

## Setup

1. Create a file named `client-secret.txt` containing the OAuth client secret. Make sure you don't have spaces or a newline after the secret!
2. Create a file named `github-api-key.txt` 
3. (Unnecessary for now) Create a file named `gandi-api-key.txt` containing the Gandi API key.
4. Generate Let's Encrypt certificates with certbot, and leave them in the default location (`/etc/letsencrypt/live/wiki.terbium.io/`)
6. Initialize a git repo at `/var/wiki` and add an `origin` remote. Make sure the local branch (which can be anything you want) has an upstream set.
5. Run `docker-compose up --build`

### For a different wiki

Here are a few places where I've hardcoded info specific to this installation:
* Backup script has my GitHub username, email, and repo name
* Dynamic DNS has my subdomain
* OAuth proxy has my Google Client ID and my email address
* ...

If you want to use this setup elsewhere, you'd need to edit these files.

## TODO

* Finish dynamic-dns script
* Figure out if there's a nice way to enable certbot auto-renewals
* Systemd startup file for docker-compose? Currently if the system goes down, I'll have to restart docker-compose manually.

## Dev notes

Unfortunately the docker-compose file is not super conducive to testing in a local environment.

To generate a self-signed cert:

```shell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx-selfsigned.key -out nginx-selfsigned.crt
```
