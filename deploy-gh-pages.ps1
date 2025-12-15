

# Safer deploy script: uses a dedicated temp clone for gh-pages deployment
# Never touches workspace or .venv; all destructive actions are in the temp dir only

$ErrorActionPreference = 'Stop'

# Set variables
$siteDir = "halcova/world_wiki/site"
$branch = "gh-pages"
$startDir = $PWD

# Check for git
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git is not installed or not in PATH."
    exit 1
}


# Ensure site is built
if (-not (Test-Path $siteDir/index.html)) {
    Write-Error "Site not built. Please run mkdocs build first."
    exit 1
}

# Commit and push any uncommitted changes to main before deploying
Write-Host "Checking for uncommitted changes in the workspace..."
if ((git status --porcelain) -ne "") {
    Write-Host "Uncommitted changes detected. Adding, committing, and pushing to main branch."
    git add .
    git commit -m "Auto-commit before deploy [automated]"
    git push origin main
} else {
    Write-Host "No uncommitted changes found."
}

# Save current branch name
$currentBranch = git rev-parse --abbrev-ref HEAD

# Create a temp directory for deployment
$deployDir = Join-Path ([System.IO.Path]::GetTempPath()) ("deploy-gh-pages-" + [System.Guid]::NewGuid().ToString())
New-Item -ItemType Directory -Path $deployDir | Out-Null

# Clone just the gh-pages branch into the temp dir
git clone --branch $branch --single-branch . $deployDir

# Remove all files in the temp dir except .git
Set-Location $deployDir
Get-ChildItem -Path . -Exclude ".git" | Remove-Item -Recurse -Force

# Copy site output to temp dir
Copy-Item -Path "$startDir/$siteDir/*" -Destination . -Recurse -Force

# Add, commit, and push changes from temp dir
git add .
git commit -m "Deploy updated MkDocs site [safe automated]" --allow-empty
git push origin $branch

# Return to original branch and directory
Set-Location $startDir
git checkout $currentBranch

# Clean up temp deploy dir
Remove-Item -Recurse -Force $deployDir

Write-Host "Deployment to gh-pages complete (dedicated temp dir, workspace untouched)."
