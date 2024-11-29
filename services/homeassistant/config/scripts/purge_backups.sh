#!/bin/bash

# Folder to clean up
TARGET_FOLDER="/config/backups"

# Age threshold in minutes
AGE_DAYS=2  # Change this to the desired age threshold

# Find and delete files older than the specified age
find "$TARGET_FOLDER" -type f -mtime +$AGE_DAYS -exec rm -f {} \;