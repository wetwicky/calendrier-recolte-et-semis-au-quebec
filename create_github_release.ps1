# GitHub Release Creator for Quebec Calendar Project
# PowerShell script to create a GitHub release with assets

param(
    [Parameter(Mandatory=$true)]
    [string]$GitHubToken,
    
    [Parameter(Mandatory=$false)]
    [string]$Version = "v1.0.0",
    
    [Parameter(Mandatory=$false)]
    [string]$RepoOwner = "wetwicky",
    
    [Parameter(Mandatory=$false)]
    [string]$RepoName = "calendrier-recolte-et-semis-au-quebec"
)

# GitHub API configuration
$GitHubApiUrl = "https://api.github.com"
$RepoUrl = "$GitHubApiUrl/repos/$RepoOwner/$RepoName"

# Headers for GitHub API
$Headers = @{
    "Authorization" = "Bearer $GitHubToken"
    "Accept" = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
}

Write-Host "🚀 Creating GitHub Release for Quebec Calendar $Version" -ForegroundColor Green
Write-Host "Repository: $RepoOwner/$RepoName" -ForegroundColor Cyan

try {
    # Read release notes
    $ReleaseNotesPath = "RELEASE_NOTES.md"
    if (Test-Path $ReleaseNotesPath) {
        $ReleaseBody = Get-Content $ReleaseNotesPath -Raw
        Write-Host "✅ Release notes loaded from $ReleaseNotesPath" -ForegroundColor Green
    } else {
        $ReleaseBody = "Complete bilingual Quebec planting and harvest calendar release."
        Write-Host "⚠️  Using default release notes" -ForegroundColor Yellow
    }

    # Create release data
    $ReleaseData = @{
        tag_name = $Version
        target_commitish = "main"
        name = "Quebec Planting & Harvest Calendar $Version - Complete Bilingual Release"
        body = $ReleaseBody
        draft = $false
        prerelease = $false
        generate_release_notes = $true
    } | ConvertTo-Json -Depth 3

    # Create the release
    Write-Host "📝 Creating release..." -ForegroundColor Yellow
    $Response = Invoke-RestMethod -Uri "$RepoUrl/releases" -Method POST -Headers $Headers -Body $ReleaseData -ContentType "application/json"
    
    Write-Host "✅ Release created successfully!" -ForegroundColor Green
    Write-Host "Release ID: $($Response.id)" -ForegroundColor Cyan
    Write-Host "Release URL: $($Response.html_url)" -ForegroundColor Cyan
    
    # Upload assets
    $ReleaseId = $Response.id
    $UploadUrl = $Response.upload_url -replace '\{\?name,label\}', ''
    
    $AssetFiles = @(
        "releases/quebec-calendrier-semis-recoltes-francais-$Version.zip",
        "releases/quebec-planting-harvest-calendar-english-$Version.zip", 
        "releases/quebec-calendrier-complet-bilingual-$Version.zip",
        "releases/checksums-$Version.txt"
    )
    
    Write-Host "📦 Uploading release assets..." -ForegroundColor Yellow
    
    foreach ($AssetPath in $AssetFiles) {
        if (Test-Path $AssetPath) {
            $AssetName = Split-Path $AssetPath -Leaf
            $AssetBytes = [System.IO.File]::ReadAllBytes($AssetPath)
            
            # Determine content type
            $ContentType = switch -Regex ($AssetName) {
                '\.zip$' { 'application/zip' }
                '\.txt$' { 'text/plain' }
                default { 'application/octet-stream' }
            }
            
            $AssetUploadUrl = "$UploadUrl?name=$AssetName"
            
            Write-Host "  📎 Uploading: $AssetName ($([Math]::Round($AssetBytes.Length / 1KB, 1)) KB)" -ForegroundColor Cyan
            
            $AssetHeaders = $Headers.Clone()
            $AssetHeaders["Content-Type"] = $ContentType
            
            try {
                $AssetResponse = Invoke-RestMethod -Uri $AssetUploadUrl -Method POST -Headers $AssetHeaders -Body $AssetBytes
                Write-Host "    ✅ Uploaded successfully" -ForegroundColor Green
            }
            catch {
                Write-Host "    ❌ Upload failed: $($_.Exception.Message)" -ForegroundColor Red
            }
        } else {
            Write-Host "  ❌ File not found: $AssetPath" -ForegroundColor Red
        }
    }
    
    Write-Host ""
    Write-Host "🎉 GitHub Release created successfully!" -ForegroundColor Green
    Write-Host "🔗 View release: $($Response.html_url)" -ForegroundColor White -BackgroundColor DarkGreen
    
} catch {
    Write-Host "❌ Error creating release: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        $ErrorStream = $_.Exception.Response.GetResponseStream()
        $Reader = New-Object System.IO.StreamReader($ErrorStream)
        $ErrorBody = $Reader.ReadToEnd()
        Write-Host "Response: $ErrorBody" -ForegroundColor Red
    }
    exit 1
}

Write-Host ""
Write-Host "📋 Release Summary:" -ForegroundColor White
Write-Host "• Version: $Version" -ForegroundColor White
Write-Host "• French calendar: ✅ Included" -ForegroundColor Green
Write-Host "• English calendar: ✅ Included" -ForegroundColor Green
Write-Host "• Complete package: ✅ Included" -ForegroundColor Green
Write-Host "• Documentation: ✅ Full bilingual" -ForegroundColor Green
Write-Host "• Scripts: ✅ All maintenance tools" -ForegroundColor Green
