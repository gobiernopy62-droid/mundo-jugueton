xml = """<?xml version='1.0' encoding='utf-8'?>
<widget id="com.tujuego.mundojugueton" version="1.0.0" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">
<n>Mundo Jugueton</n>
<description>Juego educativo interactivo</description>
<author>Las Cabezas de Ignacio</author>
<content src="index.html" />
<preference name="Orientation" value="landscape" />
<preference name="Fullscreen" value="true" />
<preference name="AllowInlineMediaPlayback" value="true" />
<preference name="android-minSdkVersion" value="22" />
<preference name="android-targetSdkVersion" value="33" />
<allow-navigation href="*" />
<allow-intent href="http://*/*" />
<allow-intent href="https://*/*" />
<access origin="*" />
</widget>"""

with open('MundoJugueton/config.xml', 'w') as f:
    f.write(xml)

print("config.xml escrito correctamente!")
