$dns =  ipconfig /displaydns 
$Path = "C:\Users\Jose\Escritorio\LPC\p9\resultadosDNS.txt"
$codificado = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($dns))
Set-Content -Value "$codificado" -Path $Path
