def construir_playlist(musicas, preferencias):
    playlist=[]
    for musica, info in musicas.items():
        artistas= info['artistas']
        estilo= info['estilo']

        for i in range(len(preferencias)):
            preferencia = preferencias[i]
            if preferencia in musicas:
                if preferencia not in playlist:
                    playlist.append(preferencia)
            elif preferencia== estilo:
                if musica not in playlist:
                    playlist.append(musica)
            elif preferencia in artistas:
                if musica not in playlist:
                    playlist.append(musica)
    return playlist

        
x=input('nome: ')
if x=='':
    print('deu certo')
