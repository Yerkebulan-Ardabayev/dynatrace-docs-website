# 🚀 Автоматическое исправление проекта
# Запусти: powershell -ExecutionPolicy Bypass -File fix_project.ps1

Write-Host "================================================================================================" -ForegroundColor Cyan
Write-Host "🔧 АВТОМАТИЧЕСКОЕ ИСПРАВЛЕНИЕ DYNATRACE DOCS WEBSITE" -ForegroundColor Cyan
Write-Host "================================================================================================" -ForegroundColor Cyan
Write-Host ""

$PROJECT_DIR = "C:\Users\yerke\Desktop\my_develop_code\dynatrace-docs-website"

# Проверка существования проекта
if (-not (Test-Path $PROJECT_DIR)) {
    Write-Host "❌ Проект не найден: $PROJECT_DIR" -ForegroundColor Red
    Write-Host "Измени переменную PROJECT_DIR в скрипте на правильный путь!" -ForegroundColor Yellow
    exit 1
}

Set-Location $PROJECT_DIR
Write-Host "✅ Проект найден: $PROJECT_DIR" -ForegroundColor Green
Write-Host ""

# Проверка Git
Write-Host "🔍 Проверка Git репозитория..." -ForegroundColor Yellow
$gitStatus = git status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Это не Git репозиторий!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Git репозиторий OK" -ForegroundColor Green
Write-Host ""

# Создание папки .github/workflows если не существует
$workflowDir = ".github\workflows"
if (-not (Test-Path $workflowDir)) {
    Write-Host "📁 Создаю папку $workflowDir..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $workflowDir -Force | Out-Null
}

# Резервная копия старого workflow (если есть)
$oldWorkflow = "$workflowDir\update-docs.yml"
if (Test-Path $oldWorkflow) {
    Write-Host "💾 Создаю резервную копию старого workflow..." -ForegroundColor Yellow
    Copy-Item $oldWorkflow "$oldWorkflow.backup" -Force
    Write-Host "✅ Резервная копия: $oldWorkflow.backup" -ForegroundColor Green
}

# Создание нового workflow
Write-Host "📝 Создаю исправленный workflow..." -ForegroundColor Yellow

$workflowContent = @"
name: Update Documentation

on:
  schedule:
    - cron: '0 21 * * *'
  workflow_dispatch:

jobs:
  update-docs:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Scrape documentation
        id: scrape
        continue-on-error: true
        run: |
          cd scripts
          python scrape_docs.py --max-pages 1000 --output ../temp_docs
          echo "scrape_status=`$?" >> `$GITHUB_OUTPUT
      
      - name: Organize docs
        if: steps.scrape.outcome == 'success'
        continue-on-error: true
        run: |
          cd scripts
          python organize_docs.py --source ../temp_docs --target ../docs/en
      
      - name: Translate to Russian (Groq)
        if: steps.scrape.outcome == 'success'
        continue-on-error: true
        env:
          GROQ_API_KEY: `${{ secrets.GROQ_API_KEY }}
        run: |
          cd scripts
          python translate_docs_groq.py --source ../docs/en --target ../docs/ru
      
      - name: Commit and push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add docs/
          
          CHANGED=`$(git diff --cached --numstat | wc -l)
          
          if [ "`$CHANGED" -eq "0" ]; then
            echo "No changes"
            echo "changes=false" >> `$GITHUB_ENV
          else
            echo "Files changed: `$CHANGED"
            git commit -m "Auto-update: `$(date +'%Y-%m-%d %H:%M') (`$CHANGED files)"
            git push
            echo "changes=true" >> `$GITHUB_ENV
          fi
      
      - name: Summary
        if: always()
        run: |
          echo "## Update Summary" >> `$GITHUB_STEP_SUMMARY
          echo "" >> `$GITHUB_STEP_SUMMARY
          
          if [ "`${{ steps.scrape.outcome }}" == "success" ]; then
            echo "Scraping: Success (1000 pages)" >> `$GITHUB_STEP_SUMMARY
          else
            echo "Scraping: Failed" >> `$GITHUB_STEP_SUMMARY
          fi
          
          if [ "`${{ env.changes }}" == "true" ]; then
            echo "Changes: Committed" >> `$GITHUB_STEP_SUMMARY
          else
            echo "Changes: None" >> `$GITHUB_STEP_SUMMARY
          fi
"@

Set-Content -Path $oldWorkflow -Value $workflowContent -Encoding UTF8
Write-Host "✅ Workflow создан: $oldWorkflow" -ForegroundColor Green
Write-Host ""

# Git add и commit
Write-Host "📤 Коммит изменений..." -ForegroundColor Yellow
git add .github/workflows/update-docs.yml
git commit -m "🔧 Fix: увеличен лимит до 1000 страниц + Groq перевод"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Коммит создан" -ForegroundColor Green
} else {
    Write-Host "⚠️  Нет изменений для коммита (возможно уже закоммичено)" -ForegroundColor Yellow
}
Write-Host ""

# Push
Write-Host "🚀 Push в GitHub..." -ForegroundColor Yellow
Write-Host "Хочешь запушить изменения в GitHub? (Y/N): " -NoNewline -ForegroundColor Cyan
$push = Read-Host

if ($push -eq "Y" -or $push -eq "y") {
    git push origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Push успешно!" -ForegroundColor Green
        Write-Host ""
        Write-Host "================================================================================================" -ForegroundColor Cyan
        Write-Host "🎉 ГОТОВО!" -ForegroundColor Green
        Write-Host "================================================================================================" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Следующие шаги:" -ForegroundColor Yellow
        Write-Host "1. Добавь GROQ_API_KEY в GitHub Secrets:" -ForegroundColor White
        Write-Host "   https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/settings/secrets/actions" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "2. Запусти workflow вручную:" -ForegroundColor White
        Write-Host "   https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website/actions" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "3. Подожди 35-40 минут пока скачается 1000 страниц" -ForegroundColor White
        Write-Host ""
        Write-Host "4. Проверь сайт:" -ForegroundColor White
        Write-Host "   https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/" -ForegroundColor Cyan
        Write-Host ""
    } else {
        Write-Host "❌ Ошибка push!" -ForegroundColor Red
        Write-Host "Попробуй вручную: git push origin main" -ForegroundColor Yellow
    }
} else {
    Write-Host "⏭️  Push пропущен. Запусти вручную: git push origin main" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Нажми Enter для выхода..." -ForegroundColor Gray
Read-Host
