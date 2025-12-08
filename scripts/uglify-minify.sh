#!/bin/bash

echo "Running JS uglification (recursive, in-place)..."

JS_DIR="staticfiles/js"

if [ ! -d "$JS_DIR" ]; then
    echo "No $JS_DIR directory — skipping."
    exit 0
fi

# Find all .js files recursively
find "$JS_DIR" -type f -name "*.js" ! -name "*.min.js" | while read -r file; do
    echo "Uglifying $file ..."
    terser "$file" --compress --mangle --output "$file"
done

echo "Uglification complete."
