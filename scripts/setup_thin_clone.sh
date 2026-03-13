#!/usr/bin/env bash
# =============================================================================
# Thin Clone Setup — минимизация дискового пространства на ноутбуке
# =============================================================================
# Использует: Git sparse-checkout + shallow clone + LFS
# Результат: ~50-80% экономии места (только нужные директории)
#
# Usage:
#   bash scripts/setup_thin_clone.sh <repo-url> [target-dir]
#
# Example:
#   bash scripts/setup_thin_clone.sh https://github.com/user/dynatrace-docs-website.git ~/docs-thin
# =============================================================================

set -euo pipefail

REPO_URL="${1:?Usage: $0 <repo-url> [target-dir]}"
TARGET_DIR="${2:-dynatrace-docs-thin}"

echo "=== Thin Clone Setup ==="
echo "Repo:   $REPO_URL"
echo "Target: $TARGET_DIR"
echo ""

# Step 1: Shallow clone with no checkout
echo "[1/5] Creating shallow clone (depth=1)..."
git clone --depth 1 --filter=blob:none --sparse "$REPO_URL" "$TARGET_DIR"
cd "$TARGET_DIR"

# Step 2: Configure sparse-checkout — only pull what we need
echo "[2/5] Configuring sparse-checkout..."
git sparse-checkout init --cone
git sparse-checkout set \
    scripts/ \
    .github/workflows/ \
    mkdocs.yml \
    requirements.txt \
    .env.example \
    docs/ru/ \
    docs/assets/ \
    docs/index.md \
    docs/common/

# Note: docs/en/ is NOT included — it's only needed during CI scraping.
# If you need English docs locally, run:
#   git sparse-checkout add docs/en/

# Step 3: Install Git LFS
echo "[3/5] Setting up Git LFS..."
if command -v git-lfs &> /dev/null; then
    git lfs install --local
    git lfs pull
    echo "  LFS configured"
else
    echo "  WARNING: git-lfs not installed. Run: brew install git-lfs (macOS) or apt install git-lfs (Linux)"
fi

# Step 4: Configure git to minimize space
echo "[4/5] Optimizing git config..."
git config core.compression 9          # Max compression
git config gc.auto 256                  # More frequent GC
git config pack.windowMemory 256m      # Limit pack memory
git config fetch.prune true            # Auto-prune old refs

# Step 5: Show results
echo "[5/5] Done!"
echo ""

TOTAL_SIZE=$(du -sh . | cut -f1)
echo "=== Thin Clone Summary ==="
echo "Location:  $(pwd)"
echo "Size:      $TOTAL_SIZE"
echo ""
echo "Included directories:"
git sparse-checkout list
echo ""
echo "To add English docs: git sparse-checkout add docs/en/"
echo "To run full pipeline: python scripts/sync_and_deploy.py"
echo "========================="
