# HermesYTExtractor
Programa para descargar vídeos de YT, principalmente se descargará el vídeo y el códec de audio con mayor calidad, ambos por separado, luego los unirá en un único archivo conservando las 3 pistas (archivo de video, audio, video y audio).

## Como se instala
Antes que nada, hay dos métodos de instalación, una manual y otra automática utilizando Docker.

### Automático - Válido para Windows/Linux/Mac (Preferido)
Lo primero es instalar Docker en tu sistema operativo (hay miles de tutoriales en youtube para todos los sistemas operativos), una vez lo tengas, independientemente de tu sistema, te vas a cualquier carpeta, abres una terminal allí y escribes:

<pre><code>docker run -v $PWD/videos:/app/youtube -it torbol/hermesytextractor:latest</code></pre>

#### Ejemplo de instalación/uso:


https://github.com/user-attachments/assets/f6bbdb36-687d-4c05-8814-bdf60c48a5f2



### Manual
Necesitamos satisfacer tres dependencias además de tener instalado Python 3:
<ul>
  <li>ffmpeg</li>
  <li>pathvalidate</li>
  <li>Última versión de <b>pytubefix</b></li>
</ul>

#### Windows
Abrimos powershell como administrador y ejecutamos:

<pre><code>pip3 install pytubefix ffmpeg pathvalidate</pre></code>
Luego debemos descargar la última versión de ffmpeg para Windows, podéis descargarlo desde <a href="https://github.com/BtbN/FFmpeg-Builds/releases">esta página</a>. Si no sabeis cómo instalarlo, en este <a href="https://www.youtube.com/watch?app=desktop&v=JR36oH35Fgg&ab_channel=Koolac">vídeo</a> lo explican bastante bien.

Por último ejecutamos nuestro programa como cualquier script en python, abriendo una powershell en la carpeta y escribiendo:
<pre><code>python ./main.py</code></pre>

#### Ubuntu
La instalación es sencilla, solo teneis que ejecutar los siguientes comandos:

<pre><code>sudo apt update && sudo apt upgrade
sudo apt install python3 ffmpeg
pip install pytubefix pathvalidate</code></pre>

Y listo, nos vamos a la carpeta de nuestro script y lo ejecutamos como cualquier programa de python :)
