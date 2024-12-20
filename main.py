from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathvalidate import sanitize_filename
import ffmpeg
import os

#Descargamos el video
def descarga_video_audio(enlacevideo):
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title) #Mostramos el título del vídeo

    #Obtenemos las pistas de video que tiene youtube y cogemos la primera, la de más alta resolución
    try:
        yv = yt.streams.get_highest_resolution(progressive=False)
    except:
        print("Ha ocurrido un error descargando por método tradicional, probando método alternativo...")
        yt.streaming_data #Con esto refrescamos los datos de streaming y aparecerán ya los streams que hay (sin error por checkavailability). Esta línea soluciona problema con algunos enlaces.
        yv = yt.streams.get_highest_resolution(progressive=False)

    if yv == None:
        print("No se ha encontrado ninguna pista de video con máxima calidad, se descargará por defecto una que ya incluya el audio, normalmente en 360p")
        yv = yt.streams.get_highest_resolution()
    print(yv) #Nos muestra la resolución del video descargado
    nombrevideoconextension = "video." + yv.subtype #Obtenemos el nombre completo del archivo de video (con su extensión)
    yv.download(filename="video." + yv.subtype) #Descargamos el video

    #Obtenemos las pistas de audio que tiene el video en youtube y descargamos la mejor en formato webm si existe, o en caso contrario se la descargará por defecto en mp4
    ya = yt.streams.get_audio_only("webm")
    if ya == None:
        print("No se ha encontrado ninguna pista de audio con formato webm, se descargará por defecto en mp4 u otro formato en su mayor bitrate (kbps)")
        ya = yt.streams.get_audio_only()

    print(ya) #Vemos el codec descargado
    nombreaudioconextension = "audio." + ya.subtype #Obtenemos el nombre completo del archivo de audio (con su extensión)
    ya.download(filename="audio." + ya.subtype) #Descargamos el audio

    #Obtenemos el nombre resultante para cuando juntemos audio y video
    nombrecompletooutputfinal = yv.title + "." + yv.subtype

    return nombrevideoconextension, nombreaudioconextension, nombrecompletooutputfinal

#Unimos el video y el audio
def video_audio_mux(path_audiosource, path_imagesource, out_video_path):
    video = ffmpeg.input(path_imagesource).video
    audio = ffmpeg.input(path_audiosource).audio
    ffmpeg.output(audio, video, out_video_path, vcodec='copy', acodec='copy').run() #En lugar de acodec='copy' usamos aac para que pueda leerlo sin instalar paquetes de codecs el reproductor de windows

#Cambiamos a directorio descarga youtube
def cambio_directorio():
    carpeta_necesaria = "youtube"
    ruta = os.getcwd()
    if carpeta_necesaria not in os.listdir() or not os.path.isdir(carpeta_necesaria): #Comprobamos si existe la carpeta "youtube"
        print("No existe carpeta: " + carpeta_necesaria + ". Creando...")
        os.mkdir(carpeta_necesaria)
    nuevaruta = os.path.join(ruta, carpeta_necesaria)
    os.chdir(nuevaruta)

#Sanitizamos nombre archivo final
def sanitize_ending_filename(archivo_final_f):
    archivo_final_sanitized_f = sanitize_filename(archivo_final_f)
    print(archivo_final_sanitized_f)
    return archivo_final_sanitized_f #Devolvemos el nombre del archivo formateado para poder guardarse en un archivo en sistemas Windows


#main
cambio_directorio() #Cambiamos a la carpeta youtube para hacer las descargas
url = input("Introduce la url del video >") #Solicitamos la URL al usuario

nombre_video, nombre_audio, archivo_final = descarga_video_audio(url) #Descargamos audio y video
archivo_final_formateado = sanitize_ending_filename(archivo_final) #Damos un formato aceptable por explorador de Windows al archivo
video_audio_mux(os.path.join(os.getcwd(), nombre_audio), os.path.join(os.getcwd(), nombre_video), os.path.join(os.getcwd(), "output_" + archivo_final_formateado)) #Lo juntamos en un único archivo de video (.mp4, webm...)
