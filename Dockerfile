# Build stage: install dependencies into a virtual environment
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_DEV=1 \
    UV_PYTHON_DOWNLOADS=0

WORKDIR /app

# Install dependencies first (cached separately from source code)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# Copy source and install the project itself
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable


# Final stage: lean image without uv
FROM python:3.14-slim-bookworm

# Non-root user for security
RUN groupadd --system --gid 999 botuser \
    && useradd --system --gid 999 --uid 999 --no-create-home botuser \
    && mkdir -p /app/logs \
    && chown botuser:botuser /app/logs

WORKDIR /app

# Copy the built virtualenv and application from the builder
COPY --from=builder --chown=botuser:botuser /app/.venv /app/.venv
COPY --from=builder --chown=botuser:botuser /app /app

COPY --chown=botuser:botuser entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

USER botuser

CMD ["/app/entrypoint.sh"]