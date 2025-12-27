#!/bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color

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

ROOT_DIR=$(git rev-parse --show-toplevel)
cd "$ROOT_DIR"

# write an pre-push hook to make sure test have to pass
if [ ! -f ".git/hooks/pre-commit" ]; then
cat <<'EOF' > .git/hooks/pre-commit
#!/bin/bash
ROOT_DIR=$(git rev-parse --show-toplevel)
bash "$ROOT_DIR/test.bash"
EOF
fi

# make pre-commit executable
chmod +x .git/hooks/pre-commit

pytest
