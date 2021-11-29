#!/bin/python
from googleapiclient.discovery import build

#Crear un script que maneje una WEb API

api_key = 'AIzaSyDZhfzlTaMaQXd-PjcikGU5eXtao-OsyHU'

youtube = build('youtube', 'v3', developerKey=api_key)

#acción1: agregando el nombre del canal, te muestra información 
canal = youtube.channels().list(part='statistics',
        forUsername='#nombre de canal')

respuesta1 = canal.execute()
print(respuesta1)

#2: crea una lista de reproducción privada
playlists = youtube.playlists().insert(
  part="snippet,status",
  body=dict(
    snippet=dict(
      titulo = "Mi playlist privada",
      description = "Playlist privada creada con una API"
    ),
    status=dict(
      privacyStatus="private"
    )
  )
).execute()

print ("Nueva Id de playlist: %s" % playlists["id"])
