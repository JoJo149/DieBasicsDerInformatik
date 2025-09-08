#!/bin/bash
check() {
    command -v "$1" >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "✅ $1 found"
    else
        echo "❌ $1 not found"
    fi
}

# checks if dependencies are present
check python3
check pytest
check cc
check git

ROOT_DIR=$(git rev-parse --show-toplevel)
cd "$ROOT_DIR"

echo "Setting up git hooks for test environment..."

# write an post-checkout hook to delete ghost folders and clear pytest cache
cat <<'EOF' > .git/hooks/post-checkout
#!/bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color
echo "🔄 post-checkout cleanup started..."

# first delete pytest cache
if [ -d ".pytest_cache" ]; then
    rm -rf .pytest_cache
fi

find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

# then delete git untracked folders and empty folders
git clean -fd>/dev/null

# find . -type d -empty -delete

echo "✅ post-checkout cleanup finished. Working tree is clean."
EOF

# make post-checkout executable
chmod +x .git/hooks/post-checkout

# write an pre-push hook to make sure test have to pass
cat <<'EOF' > .git/hooks/pre-push
#!/bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color

# fertig erstellte Aufgaben Branches
exercise_branches=("main" "master" "aufgabe-01")

current_branch=$(git rev-parse --abbrev-ref HEAD)

# check if user is on an valid branch
is_allowed=false
for branch in "${exercise_branches[@]}"; do
    if [[ "$current_branch" == "$branch" ]]; then
        is_allowed=true
        break
    fi
done

if $is_allowed; then
    echo "✅ Branch '$current_branch' is allowed."
else
    printf "${RED}Abgabe-error: You are on branch '$current_branch' and not on an 'aufgabe-__' or main branch.\n${NC}"
    exit 1
fi

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    printf "${RED}Abgabe-error: There are uncommitted changes.${NC}\n"
    exit 1
else
    echo "✅ All changes are committed."
fi

ROOT_DIR=$(git rev-parse --show-toplevel)
cd "$ROOT_DIR" || exit 1

# do tests and check if they fail
for dir in Aufgabe*; do
    if [ -d "$dir" ]; then
        echo "Testing $dir..."
        if ! pytest -s "$dir"; then
            printf "${RED}Abgabe-error: Tests failed for $dir ${NC}\n"
            exit 1
        fi
    fi
done

echo "✅ All tests passed. Well done. Proceeding with push."
echo ""
EOF

# make pre-push executable
chmod +x .git/hooks/pre-push

echo "✅ All dependencies present and git environment implemented."