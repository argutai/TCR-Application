#!/bin/bash
username=$1
password=$2


git stash
git submodule foreach 'git stash'
git pull
git submodule update --init --recursive
git submodule update --recursive --remote
sudo systemctl reload apache2

sed -i.bak "s/^    username = .*/    username = \"$username\"/g" 'app/render_doc.py'
sed -i.bak "s/^    password = .*/    password = \"$password\"/g" 'app/render_doc.py'
rm 'app/render_doc.py.bak'

query=$(curl https://localhost:443 --insecure)
SUB='TCR Analysis Home'
RED='\033[0;31m'; GREEN='\033[0;32m'; NC='\033[0m'

if [[ "$query" == *"$SUB"* ]]; then 
    echo -e "${GREEN}Deployment updated successfully.${NC}"
else
    tail -n 5 /var/log/apache2/error.log
    echo -e "${RED}Deployment update failed.${NC}"
fi
