#!/bin/sh
set -e

tortoise upgrade
exec python main.py
