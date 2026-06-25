Get-Process | Where-Object { $_.ProcessName -eq 'cmd' -or $_.ProcessName -eq 'python' } | Sort-Object Id | Format-Table Id, ProcessName, MainWindowTitle, StartTime -AutoSize
