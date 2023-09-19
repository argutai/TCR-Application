git stash
git submodule foreach 'git stash'
git pull
git submodule update --init --recursive
git submodule update --recursive --remote
sudo systemctl reload apache2

query=$(curl https://localhost:443 --insecure)
SUB='TCR Analysis Home'
if [[ "$query" == *"$SUB"* ]]; then 
    Green='\033[0;32m'
    NC='\033[0m'
    echo -e "${Green}Deployment updated successfully.${NC}"
fi