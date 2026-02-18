@echo off
echo Запуск Chrome с remote debugging...
echo После открытия - перейдите на notebooklm.google.com вручную
echo Потом запустите: python scripts/upload_to_notebooklm.py
echo.

start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" ^
  --remote-debugging-port=9222 ^
  --user-data-dir="%TEMP%\chrome_debug_profile" ^
  --no-first-run ^
  --start-maximized ^
  https://notebooklm.google.com

echo Chrome запущен на порту 9222
pause
