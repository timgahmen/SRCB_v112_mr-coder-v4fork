function git-upstream-merge() {
  # Fetch the latest changes from the upstream repository
  echo "Fetching and merging latest changes from upstream..."
  git fetch upstream
  
  # Reset local branch to match upstream repository
  git reset --hard upstream/patch-1
}

git-upstream-merge
