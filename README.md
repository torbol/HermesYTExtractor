# HermesYTExtractor
Programa para descargar vídeos de YT, principalmente se descargará el vídeo y el códec de audio con mayor calidad, ambos por separado, luego los unirá en un único archivo conservando las 3 pistas (archivo de video, audio, video y audio).

## Como se instala
Antes que nada, hay dos métodos de instalación, una manual y otra automática utilizando Docker.

### Automático (Preferido)
Lo primero es instalar Docker en tu sistema operativo (hay miles de tutoriales en youtube para todos los sistemas operativos), una vez lo tengas, independientemente de tu sistema, te vas a cualquier carpeta, abres una terminal allí y escribes:

<pre><code>docker run -v $PWD/videos:/app/youtube -it torbol/hermesytextractor:latest</code></pre>

#### Ejemplo de instalación/uso:


https://github.com/user-attachments/assets/f6bbdb36-687d-4c05-8814-bdf60c48a5f2



### Manual
Ya sea en Windows o Linux, necesitamos satisfacer dos dependencias además de tener instalado Python 3:
<ul>
  <li>ffmpeg</li>
  <li>Última versión de <b>pytubefix</b></li>
</ul>

#### Windows
Abrimos powershell como administrador y ejecutamos:

<pre style="color: red;"><code>pip.exe install pytubefix</code></pre>

Luego debemos descargar la última versión de ffmpeg para Windows, podeis descargarlo desde <a href="https://github.com/BtbN/FFmpeg-Builds/releases">esta página</a>. Igualmente dejaré todo lo necesario empaquetado en la <a href="https://github.com/torbol/HermesYTExtractor/releases">sección de lanzamientos</a>.

#### Ubuntu
Aquí la instalación es mucho más sencilla, solo teneis que ejecutar los siguientes comandos:

<pre><code>sudo apt update && sudo apt upgrade
sudo apt install python3 ffmpeg
pip install pytubefix</code></pre>

Y listo, nos vamos a la carpeta de nuestro script y lo ejecutamos como cualquier programa de python :)
