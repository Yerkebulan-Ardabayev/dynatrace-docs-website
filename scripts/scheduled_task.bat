@echo off
REM Dynatrace Docs Auto-Pipeline — runs daily via Task Scheduler
REM Switches to project dir and runs the pipeline

cd /d "C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"

REM Pull latest from GitHub first
git pull --ff-only 2>nul

REM Run the full pipeline
python scripts\auto_pipeline.py --max-translate 20 >> scripts\pipeline.log 2>&1
