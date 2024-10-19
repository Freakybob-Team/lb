@echo off
setlocal

set "imageUrl=https://f.feridinha.com/LqRkS.jpg"
set "desktopPath=%USERPROFILE%\Desktop\greg.jpg"

powershell -command "Invoke-WebRequest -Uri '%imageUrl%' -OutFile '%desktopPath%'"

if exist "%desktopPath%" (
    for /L %%i in (1,1,0) do (
        copy "%desktopPath%" "%USERPROFILE%\Desktop\rowley_%%%%i.jpg"
    )
) else (
    echo greg wasen't feeling well today :(.
)

echo greg in a box
pause