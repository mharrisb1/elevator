FROM debian:trixie-slim AS base

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3.13 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN useradd --create-home --shell /bin/bash app

USER app
WORKDIR /home/app

ENV UV_PYTHON_PREFERENCE=only-system

COPY pyproject.toml .

FROM base AS app
RUN uv sync --no-dev
COPY src/ src/
ENTRYPOINT ["uv", "run", "elevator"]

FROM base AS dev
RUN uv sync --only-dev
COPY src/ src/
COPY tests/ tests/
COPY .coveragerc .

ENTRYPOINT ["uv", "run"]