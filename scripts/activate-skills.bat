@echo off
setlocal EnableDelayedExpansion

:: --- CONFIGURATION FOR ANTIGRAVITY IDE ---
set "BASE_DIR=%USERPROFILE%\.gemini\config"
set "SKILLS_DIR=%BASE_DIR%\skills"
set "LIBRARY_DIR=%BASE_DIR%\skills_library"
set "REPO_DIR=%BASE_DIR%\skills_repo"
set "ARCHIVE_PREFIX=%BASE_DIR%\skills_archive"
set "BUNDLE_HELPER=%REPO_DIR%\tools\scripts\get-bundle-skills.py"
set "PYTHON_BIN=python"

echo ========================================================
echo   Antigravity Skills Manager (AAS v17.0.0 + Context7)
echo ========================================================

:: --- ARGUMENT HANDLING ---
set "DO_CLEAR=0"
set "EXTRA_ARGS="
set "SKILLS_LIST_FILE=%TEMP%\skills_list_%RANDOM%_%RANDOM%.txt"

if "%~1"=="" (
    echo Usage:
    echo   activate-skills.bat [--clear] ^<Bundle or Skill Name^>
    echo Examples:
    echo   activate-skills.bat --clear Essentials
    echo   activate-skills.bat "Web Wizard" "TypeScript & JavaScript"
    echo   activate-skills.bat --clear "DevOps & Cloud"
    echo   activate-skills.bat --restore-curated
    echo.
    set /p "USER_CHOICE=Enter bundle name or press Enter for Essentials: "
    if "!USER_CHOICE!"=="" (
        set "EXTRA_ARGS=Essentials"
    ) else (
        set "EXTRA_ARGS=!USER_CHOICE!"
    )
) else (
    for %%a in (%*) do (
        if /I "%%~a"=="--clear" (
            set "DO_CLEAR=1"
        ) else if /I "%%~a"=="--restore-curated" (
            set "DO_CLEAR=1"
            set "EXTRA_ARGS=Essentials \"Web Wizard\" \"Web Designer\" \"Full-Stack Developer\" \"TypeScript & JavaScript\" \"DevOps & Cloud\" \"Systems Programming\" \"Architecture & Design\" \"DDD & Evented Architecture\" \"Documents & Presentations\" \"OSS Maintainer\" \"Skill Author\" \"Security Developer\""
        ) else (
            if "!EXTRA_ARGS!"=="" (set "EXTRA_ARGS=%%a") else (set "EXTRA_ARGS=!EXTRA_ARGS! %%a")
        )
    )
)

:: --- ARCHIVE ACTIVE SKILLS IF --CLEAR ---
if "!DO_CLEAR!"=="1" (
    echo [CLEAR] Archiving current active skills...
    if exist "%SKILLS_DIR%" (
        set "ts=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%"
        set "ts=!ts: =0!"
        robocopy "%SKILLS_DIR%" "%ARCHIVE_PREFIX%_!ts!" /E /MOVE /NFL /NDL /NJH /NJS >nul 2>&1
    )
    mkdir "%SKILLS_DIR%" 2>nul
)

:: --- EXPAND BUNDLES ---
echo Resolving bundle skills...
if exist "%SKILLS_LIST_FILE%" del "%SKILLS_LIST_FILE%" 2>nul

if exist "%BUNDLE_HELPER%" (
    "%PYTHON_BIN%" "%BUNDLE_HELPER%" !EXTRA_ARGS! > "%SKILLS_LIST_FILE%" 2>nul
)

:: Always ensure context-7 is included if clearing or requested
if exist "%LIBRARY_DIR%\context-7" (
    echo context-7 >> "%SKILLS_LIST_FILE%"
)

:: --- RESTORE SELECTED SKILLS ---
echo Deploying skills into active directory...
set "ACTIVATED_COUNT=0"

if exist "%SKILLS_LIST_FILE%" (
    for /f "usebackq delims=" %%s in ("%SKILLS_LIST_FILE%") do (
        set "SKILL_NAME=%%s"
        set "SKILL_NAME=!SKILL_NAME:/=\!"
        if exist "%SKILLS_DIR%\!SKILL_NAME!" (
            echo   . !SKILL_NAME! ^(already active^)
            set /a ACTIVATED_COUNT+=1
        ) else if exist "%LIBRARY_DIR%\!SKILL_NAME!" (
            echo   + !SKILL_NAME!
            robocopy "%LIBRARY_DIR%\!SKILL_NAME!" "%SKILLS_DIR%\!SKILL_NAME!" /E /NFL /NDL /NJH /NJS >nul 2>&1
            set /a ACTIVATED_COUNT+=1
        ) else (
            echo   - !SKILL_NAME! ^(not found in library^)
        )
    )
    del "%SKILLS_LIST_FILE%" 2>nul
)

echo.
echo Active skills updated: !ACTIVATED_COUNT! skills now active in Antigravity.
echo Skills directory: %SKILLS_DIR%
echo.
endlocal
