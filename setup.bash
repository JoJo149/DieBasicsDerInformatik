#!/bin/bash
check() {
    command -v "$1" >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "✅ $1 found"
    else
        echo "❌ $1 not found"
    fi
}

check python3
check pytest
check cc
check git

ROOT_DIR=$(git rev-parse --show-toplevel)
cd "$ROOT_DIR"

cat <<'EOF' > .git/hooks/pre-push
#!/bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color

current_branch=$(git rev-parse --abbrev-ref HEAD)

# The branch we don't want to push to main
restricted_branch="local-branch"
target_branch="main"

# Read from stdin — git pre-push provides the refs being pushed
while read local_ref local_sha remote_ref remote_sha
do
  # remote_ref looks like refs/heads/main
  if [[ "$current_branch" == "$restricted_branch" && "$remote_ref" == "refs/heads/$target_branch" ]]; then
      printf "${RED} Abgabe-error:You cannot push '$restricted_branch' to '$target_branch'.${NC}\n"
      exit 1
  fi
done

echo "Running all exercise tests before push..."

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    printf "${RED}Abgabe-error: There are uncommitted changes.${NC}\n"
    exit 1
else
    echo "All changes are committed."
fi

ROOT_DIR=$(git rev-parse --show-toplevel)
cd "$ROOT_DIR" || exit 1

for dir in Aufgabe*; do
  if [ -d "$dir" ]; then
      echo "▶ Testing $dir..."
      if ! pytest -s "$dir"; then
          printf "❌${RED}Abgabe-error: Tests failed for $dir ${NC}\n"
          exit 1
      fi
  fi
done

echo "✅ All tests passed. Proceeding with push."
EOF

chmod +x .git/hooks/pre-push
echo "✅ All dependencies present and git environment implemented."