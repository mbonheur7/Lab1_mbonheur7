#!/bin/bash
if [! -d "archive" ]; then
mkdir archive
fi
timestamp = $(date +"%Y%m%d-%H%M%S")