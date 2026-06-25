@echo off
REM Dynatrace Docs — Full local pipeline
REM Scrape fresh EN docs from docs.dynatrace.com -> detect -> translate via claude CLI -> PDF -> Obsidian sync
REM No git push (locally only). Run via:
REM   start "Dynatrace Docs Pipeline" cmd /k "scripts\full_pipeline.bat"

cd /d "C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"

echo.
echo ============================================================
echo  DYNATRACE DOCS — FULL LOCAL PIPELINE
echo  Started: %date% %time%
echo ============================================================
echo.

REM ---- Sync repo first ----
echo [git] pull --ff-only
git pull --ff-only 2>nul
echo.

REM ---- STAGE 0: Scrape ----
echo ============================================================
echo  STAGE 0: Scraping docs.dynatrace.com -> docs\en
echo  (~26 min for 1500 pages, 1 req/sec)
echo ============================================================
python scripts\scrape_docs.py --output docs\en --max-pages 1500
if errorlevel 1 (
    echo.
    echo [ERROR] Scraper failed. Aborting.
    pause
    exit /b 1
)
echo.

REM ---- STAGE 1-6: auto_pipeline (detect + translate + PDF + obsidian + telegram, NO push) ----
echo ============================================================
echo  STAGE 1-6: detect -> translate -> PDF -> obsidian -> telegram
echo  (translates via 'claude -p' CLI, no API keys needed)
echo ============================================================
python scripts\auto_pipeline.py --max-translate 50 --skip-push

echo.
echo ============================================================
echo  DONE: %date% %time%
echo  Translated files: docs\ru\
echo  PDFs: pdf-docs\
echo  To commit and push manually:
echo    git status
echo    git add docs/en/ docs/ru/ pdf-docs/ scripts/.change_tracking/
echo    git commit -m "docs: update from docs.dynatrace.com"
echo    git push
echo ============================================================
pause
