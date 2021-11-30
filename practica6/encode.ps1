$archivo = Get-Content .\transcripcion.txt

$ste = [System.Text.Encoding]::UTF8.GetBytes($archivo)
[System.Convert]::ToBase64String($ste) > .\transcripcion.txt
