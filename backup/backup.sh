set -e

pushd /wiki/tiddlers
git add .

git diff --cached --exit-code || (echo "No changes detected, exiting"; exit 0)

git commit -m "Automatic commit at $(date --rfc-3339 seconds --utc)"
git config user.name "Matthieu Felix"
git config user.email "matthieufelix@gmail.com"
git remote set-url origin "https://MattX:$(cat /etc/github-api-key.txt)@github.com/MattX/wiki"
git push
