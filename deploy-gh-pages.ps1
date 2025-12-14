# This script will deploy the contents of the MkDocs site directory to the gh-pages branch for GitHub Pages hosting.
# Usage: Run this script from the root of your Worldbuilding workspace after building the site.

$ErrorActionPreference = 'Stop'

# Set variables
$siteDir = "halcova/world_wiki/site"

$siteDir = "halcova/world_wiki/site"
$branch = "gh-pages"

# Save current directory
$startDir = $PWD

# Check for git
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git is not installed or not in PATH."
    exit 1
}


# Save current branch name
$currentBranch = git rev-parse --abbrev-ref HEAD

# Ensure site is built
if (-not (Test-Path $siteDir/index.html)) {
    Write-Error "Site not built. Please run mkdocs build first."
    exit 1
}


# Switch to gh-pages branch (create if doesn't exist)
if (-not (git show-ref --verify --quiet refs/heads/$branch)) {
    git checkout --orphan $branch
    git rm -rf .
} else {
    git checkout $branch
}

# Remove all files in the branch (except .git)
Get-ChildItem -Path . -Exclude ".git" | Remove-Item -Recurse -Force

# Copy site output to branch root
Copy-Item -Path "$startDir/$siteDir/*" -Destination . -Recurse -Force

git push origin $branch
# Add and commit changes
git add .
git commit -m "Deploy updated MkDocs site [automated]" --allow-empty
git push origin $branch

# Switch back to original branch and directory
git checkout $currentBranch
Set-Location $startDir

Write-Host "Deployment to gh-pages complete."
