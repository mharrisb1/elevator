#!/bin/bash

docker build . -t elevator:dev --target dev

docker run --rm --name lint elevator:dev ruff check src/ tests/
docker run --rm --name static elevator:dev ty check src/ tests/
docker run --rm --name test elevator:dev pytest
