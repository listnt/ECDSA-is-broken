echo $(date '+%Y-%m-%d %H:%M:%S') > timestamp.txt
git add ./
git commit -m "$(date '+%Y-%m-%d %H:%M:%S')"
git push