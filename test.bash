#!/bin/bash

RED='\033[0;31m' # Color Red
NC='\033[0m' # No Color

# check if dependencies have version (are present)
check() {
    if ! command -v "$1" >/dev/null 2>&1; then
        printf "❌$RED $1 not found$NC \n"
        exit 1
    fi
}

# checks if dependencies are present
check python3
check pytest
check cc
check git

echo "✅ All dependencies found"

# go into root of project
ROOT_DIR=$(git rev-parse --show-toplevel)
cd "$ROOT_DIR"

# write an pre-push hook to make sure test run before at least once commit
if [ ! -f ".git/hooks/pre-push" ]; then
cat <<'EOF' > .git/hooks/pre-push
#!/bin/bash
ROOT_DIR=$(git rev-parse --show-toplevel)
bash "$ROOT_DIR/test.bash"
EOF

# make pre-push executable
chmod +x .git/hooks/pre-push
fi

# check if an directory has changed, if so use tests for the directory
for dir in Aufgabe??/; do
    [ -d "$dir" ] || continue
    if git status --porcelain "$dir" | grep -q .; then
        echo "🧪 Changes detected in $dir → running pytest"
        pytest "$dir"
    fi
done
