@echo off
REM Managed-only full update: scrape /managed/ -> detect changes -> translate new+updated via Claude CLI
REM Target: bring docs/managed-ru/ up to parity with docs/managed/ (currently 67/263 = 25%)

cd /d "C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"

echo ============================================================
echo  MANAGED FULL UPDATE  (scrape + detect + translate)
echo  Started: %date% %time%
echo ============================================================
echo.

REM ----- STAGE 0: Scrape /managed/ only -----
echo === STAGE 0: Scrape docs.dynatrace.com/managed/ -^> docs\managed
echo (~263+ pages, ~5-9 min, 1 req/sec)
echo.
python -u scripts\scrape_docs.py --output docs\managed --max-pages 1500
if errorlevel 1 (
    echo.
    echo [ERROR] Scrape failed
    pause
    exit /b 1
)

REM ----- STAGE 1: Detect changes -----
echo.
echo === STAGE 1: Detect changes docs\managed ^<^-^> docs\managed-ru
echo.
python scripts\detect_changes.py ^
    --source-dir docs/managed ^
    --target-dir docs/managed-ru ^
    --repo Yerkebulan-Ardabayev/dynatrace-docs-website ^
    --report changes_report.json ^
    --markdown changes_report.md
if errorlevel 1 (
    echo [ERROR] detect_changes failed
    pause
    exit /b 1
)

echo.
echo --- changes_report.md ---
type changes_report.md
echo.

REM ----- STAGE 2: Translate via Claude Code CLI -----
echo === STAGE 2: Translate new + updated via 'claude -p' CLI
echo (~2-3 min per file, 196 max for full coverage)
echo.
python -u scripts\translate_managed.py --report changes_report.json --max-articles 250

echo.
echo ============================================================
echo  DONE: %date% %time%
echo  Translations in: docs\managed-ru\
echo  No git push performed (review locally first)
echo ============================================================
pause
