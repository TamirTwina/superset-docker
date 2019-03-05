#!/bin/bash

set -e

# Initialize the database
superset db upgrade

# Create default roles and permissions
superset init
