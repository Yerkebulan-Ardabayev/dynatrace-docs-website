@echo off
REM Managed-only update: scrape /managed/ -> detect changes vs docs/managed-ru/
REM Does NOT translate (wait for user OK after seeing report)

cd /d "C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"

echo ============================================================
echo  MANAGED UPDATE — scrape + detect
echo  Started: %date% %time%
echo ============================================================
echo.

echo === STAGE 0: Scrape /managed/ only -^> docs\managed ===
echo (BASE_URL: https://docs.dynatrace.com/managed/  ~263+ pages, ~5 min)
echo.
python -u scripts\scrape_docs.py --output docs\managed --max-pages 1500
if errorlevel 1 (
    echo.
    echo [ERROR] Scrape failed
    pause
    exit /b 1
)

echo.
echo === STAGE 1: Detect changes docs\managed ^<^-^> docs\managed-ru ===
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
echo ============================================================
echo  REPORT (also saved to changes_report.md):
echo ============================================================
type changes_report.md
echo.
echo ============================================================
echo  DONE: %date% %time%
echo  Next step: review report, then run translate
echo ============================================================
pause
