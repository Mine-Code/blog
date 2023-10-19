#!/bin/bash

THIS_FILE_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "${THIS_FILE_DIR}/.." && pwd)"
BACK_DIR="${PROJECT_DIR}/backend"
ENV_FILE="${PROJECT_DIR}/.env"

if [ ! -f "${ENV_FILE}" ]; then
    echo ".env not found"
    exit 1
fi

echo "starting Docker compose..."

docker compose down
docker compose build
docker compose up -d

echo "Docker composed successfully"
