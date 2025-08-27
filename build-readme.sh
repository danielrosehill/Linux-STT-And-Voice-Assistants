#!/bin/bash
# Build script to generate README.md from template and sections

set -e

echo "Building README.md from template and sections..."

# Check if template exists
if [ ! -f "README.template.md" ]; then
    echo "Error: README.template.md not found"
    exit 1
fi

# Check if sections directory exists
if [ ! -d "sections" ]; then
    echo "Error: sections/ directory not found"
    exit 1
fi

# Run the Python build script
python3 build-readme.py

echo "✓ README.md built successfully"
echo "✓ Run this script anytime you update section files"
