@echo off
SETLOCAL
set "dir=%userprofile%\Documents\Soulseek Downloads\complete"
set "dl=%userprofile%\Documents\Soulseek Downloads\downloading"
set "ext=%userprofile%\Documents\Soulseek Downloads\extracted"

cd %dir%

echo Extracting all tracks from: %dir%

Rem check for /extracted folder. create one if there isn't
If not exist "%ext%" (
  echo extracted folder not detected. Creating...
  mkdir "%ext%"
) else (
  echo extracted folder already exists...skipping directory creation
)

echo Moving extracted tracks to:  %ext%

REM extract out all individual tracks
for /r %%j in (*) do (
  move "%%j" "%ext%"
)

REM Delete all empty folders in complete and downloading directories
robocopy "%dir%" "%dir%" /s /move /NFL /NDL /NJH /NJS /nc /ns /np
robocopy "%dl%" "%dl%" /s /move  /NFL /NDL /NJH /NJS /nc /ns /np

exit /B 0