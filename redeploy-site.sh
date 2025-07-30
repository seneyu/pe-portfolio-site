#!/bin/bash

cd pe-portfolio-site
git fetch && git reset origin/main --hard

# spin containers down to prevent out of memory issues on our VPS instances when building the next step
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
