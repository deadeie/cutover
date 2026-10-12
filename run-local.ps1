$ErrorActionPreference = 'Stop'
$python = Get-Command py -ErrorAction SilentlyContinue
if ($python) { & py -3 -m application }
else { & python -m application }
