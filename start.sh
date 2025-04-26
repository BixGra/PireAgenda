echo "docker build . -t pireagenda"

docker build . -t pireagenda

echo "docker compose up -d --remove-orphans"

docker compose up -d --remove-orphans

echo "docker image prune -a"

docker system prune -a