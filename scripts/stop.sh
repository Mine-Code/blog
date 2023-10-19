#!/bin/bash

THIS_FILE_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "${THIS_FILE_DIR}/.." && pwd)"
BACK_DIR="${PROJECT_DIR}/backend"
ENV_FILE="${PROJECT_DIR}/.env"

docker compose down
