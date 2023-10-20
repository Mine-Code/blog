#!/bin/bash

THIS_FILE_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "${THIS_FILE_DIR}/.." && pwd)"
BACK_DIR="${PROJECT_DIR}/backend"
DB_DATA_DIR="${PROJECT_DIR}/etc/mysql/dbdata"
ENV_FILE="${PROJECT_DIR}/.env"

echo "Are you sure you want to reset the database? (y/n)"
read -p "y/n: " yn

case "$yn" in [yY]*) ;; *)
  exit
  ;;
esac

echo "Stopping Docker..."

docker compose down

echo "Stopping Docker... Done!"

echo "Removing DB data..."

sudo rm -rf "${DB_DATA_DIR}"

echo "Removing DB data... Done!"

echo "Starting Docker..."

docker compose up -d --build

echo "Starting Docker... Done!"
