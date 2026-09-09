<#
.SYNOPSIS
    Antigravity IDE Skills Manager (PowerShell Native)
.DESCRIPTION
    Easily activate, layer, clear, and list Agent Skills from AAS v17.0.0 and Context7.
.EXAMPLE
    .\scripts\manage-skills.ps1 -Clear -Bundle "Essentials"
    .\scripts\manage-skills.ps1 -Add "Web Wizard", "TypeScript & JavaScript"
    .\scripts\manage-skills.ps1 -ListActive
    .\scripts\manage-skills.ps1 -RestoreCurated
#>

[CmdletBinding()]
param(
    [Parameter(Position=0)]
    [string[]]$Bundle,

    [switch]$Clear,
    [switch]$RestoreCurated,
    [switch]$ListActive,
    [switch]$ListBundles
)

$BaseDir = "$env:USERPROFILE\.gemini\config"
$SkillsDir = "$BaseDir\skills"
$LibraryDir = "$BaseDir\skills_library"
$RepoDir = "$BaseDir\skills_repo"
$ArchivePrefix = "$BaseDir\skills_archive"
$Helper = "$RepoDir\tools\scripts\get-bundle-skills.py"

if ($ListActive) {
    Write-Host "`n=== ACTIVE ANTIGRAVITY SKILLS ===" -ForegroundColor Cyan
    $active = Get-ChildItem -Path $SkillsDir -Directory | Sort-Object Name
    Write-Host "Total active skills: $($active.Count)" -ForegroundColor Green
    foreach ($s in $active) {
        $hasMd = Test-Path "$($s.FullName)\SKILL.md"
        $status = if ($hasMd) { "[OK]" } else { "[MISSING SKILL.MD]" }
        Write-Host "  $status $($s.Name)" -ForegroundColor $(if ($hasMd) { "Gray" } else { "Red" })
    }
    return
}

if ($ListBundles) {
    Write-Host "`n=== AVAILABLE AAS v17.0.0 EDITORIAL BUNDLES ===" -ForegroundColor Cyan
    $manifestPath = "$RepoDir\data\editorial-bundles.json"
    if (Test-Path $manifestPath) {
        $data = Get-Content $manifestPath -Raw | ConvertFrom-Json
        foreach ($b in $data.bundles) {
            Write-Host ("`n• " + $b.title) -ForegroundColor Yellow
            Write-Host ("  ID: " + $b.id) -ForegroundColor DarkGray
            Write-Host ("  Skills (" + $b.skills.Count + "): " + ($b.skills -join ", ")) -ForegroundColor White
        }
    } else {
        Write-Host "Manifest not found at $manifestPath" -ForegroundColor Red
    }
    return
}

if ($RestoreCurated) {
    $Bundle = @(
        "Essentials", "Web Wizard", "Web Designer", "Full-Stack Developer",
        "TypeScript & JavaScript", "Creative Director", "DevOps & Cloud",
        "Systems Programming", "Mobile Developer", "Architecture & Design",
        "DDD & Evented Architecture", "Documents & Presentations",
        "OSS Maintainer", "Skill Author", "Security Developer"
    )
    $Clear = $true
}

if (-not $Bundle -and -not $Clear) {
    Write-Host "Please specify a bundle name (e.g. -Bundle 'Essentials') or use -ListActive / -ListBundles." -ForegroundColor Yellow
    return
}

if ($Clear) {
    Write-Host "`n[RESET] Archiving current active skills..." -ForegroundColor Yellow
    $timestamp = (Get-Date).ToString("yyyyMMdd_HHmmss")
    $archiveDir = "${ArchivePrefix}_$timestamp"
    if (Test-Path $SkillsDir) {
        robocopy $SkillsDir $archiveDir /E /MOVE /NFL /NDL /NJH /NJS | Out-Null
        Write-Host "Archived active skills to: $archiveDir" -ForegroundColor DarkGray
    }
    New-Item -ItemType Directory -Path $SkillsDir -Force | Out-Null
}

$skillsToActivate = [System.Collections.Generic.HashSet[string]]::new()

foreach ($b in $Bundle) {
    Write-Host "Resolving bundle: $b..." -ForegroundColor Cyan
    $resolved = & python $Helper $b
    foreach ($line in ($resolved -split "`r?`n")) {
        $s = $line.Trim()
        if ($s) {
            [void]$skillsToActivate.Add($s)
        }
    }
}

# Always ensure context-7 and custom skills are preserved
if (Test-Path "$LibraryDir\context-7") { [void]$skillsToActivate.Add("context-7") }
if (Test-Path "$LibraryDir\academic-thesis-auditor") { [void]$skillsToActivate.Add("academic-thesis-auditor") }
if (Test-Path "$LibraryDir\tauri-ipc-architecture") { [void]$skillsToActivate.Add("tauri-ipc-architecture") }
if (Test-Path "$LibraryDir\canvas-performance") { [void]$skillsToActivate.Add("canvas-performance") }

Write-Host "`nDeploying $($skillsToActivate.Count) skills into active directory..." -ForegroundColor Green
$activated = 0

foreach ($s in ($skillsToActivate | Sort-Object)) {
    $src = "$LibraryDir\$s"
    $dst = "$SkillsDir\$s"
    if (Test-Path $dst) {
        Write-Host "  . $s (already active)" -ForegroundColor DarkGray
        $activated++
    } elseif (Test-Path $src) {
        robocopy $src $dst /E /NFL /NDL /NJH /NJS | Out-Null
        Write-Host "  + $s" -ForegroundColor White
        $activated++
    } else {
        Write-Host "  - $s (not found in library)" -ForegroundColor Red
    }
}

Write-Host "`nDone! Antigravity active skills: $activated." -ForegroundColor Green
