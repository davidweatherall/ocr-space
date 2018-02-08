import urllib.request, urllib.parse
import base64
import json

with open("/home/david/triv/testbw.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

data = {
'apikey' : '',
'base64Image' : 'data:image/png;base64,' + encoded_string.decode('utf-8')
}
data = bytes( urllib.parse.urlencode( data ).encode() )
handler = urllib.request.urlopen( 'https://api.ocr.space/parse/image', data );
result = handler.read().decode( 'utf-8' );

a = result

b = json.loads(a.replace('\r\n', '\\r\\n'))

c = b['ParsedResults'][0]['ParsedText']

print(c)