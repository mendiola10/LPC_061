#Este script permite hacer acciones con carpetas
function salir
{ exit }

function pregunta 
{ $direct = Read-Host "Por favor introduce el nombre de la carpeta" } 

Write-Output "MENU DE ACCIONES
[1] Crear carpeta
[2] Borrar carpeta
[3] Mostrar carpeta
[4] Salir"
$numero = Read-Host "Por favor introduce una opcion"

while ($numero -ne 1 -and $numero -ne 2 -and $numero -ne 3 -and $numero -ne 4)
{
cls
Write-Output "Lo siento has introducido $numero y debes introducir un número del 1 al 4
[1] Crear carpeta
[2] Borrar carpeta
[3] Mostrar carpeta
[4] Salir"
$numero = Read-Host "Por favor introduce un numero"
$numero2 = $numero
}

switch ($numero) {
1 { pregunta
    New-Item $direct -ItemType directory }
2 { pregunta
    Remove-Item $direct }
3 { pregunta
    Get-ChildItem $direct }
default { salir }
}