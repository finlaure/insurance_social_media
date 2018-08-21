El archivo "semilla.csv" tiene las cuentas y hashtags que busqu� para armar el integral de la conversaci�n, centrando en canales de seguros de asistencia al viajero y blogs de viajes que recomendaban salir con asistencia al viajero. Las conexiones encontradas tienen mayor frecuencia en los �ltimos 30 d�as, por el funcionamiento de las API, pero hay edges que datan de m�s de 5 a�os. En total hay m�s de 50.000 edges.

Los archivos de edges tienen 5 columnas:
 - ssnn: La red social de la interacci�n
 - interaccion: El tipo de interaccion estudiada:
		1) comment: comentario en instagram
		2) auto: retweets o reply de la persona sobre su propio timeline
		3) mentions: Menci�n en otro tweet
		4) quote: Cita en otro tweet
		5) reply: Respuesta a otro tweet
		6) retweet: Duplicaci�n del tweet en otro timeline
 - target: La persona que hizo el post/tweet original
 - source: La persona que comenta, twittea, etc. sobre el perfil del otro
 - weight: La cantidad de veces que esa interacci�n se genera

Los archivos originales de grafos se llaman "insurance_*ssnn*_grafos_*interaccion*.csv" y est�n en la carpeta correspondiente a la red social. El archivo final se llama insurance_grafos.csv

Dentro de las carpetas de las redes sociales tambi�n se encuentra una copia de los detalles de cada una de las cuentas principales que postearon en la tem�tica (weight es la cantidad de tweets/posts levantados). El archivo "insurance_influencers.csv" tiene esta informaci�n integrada para las dos redes sociales, adem�s de la cantidad de followers de las cuentas (tengo otros datos que pueden llegar a ser �tiles si necesit�s tambi�n).


Por �ltimo, cleaning.py es el script que us� para limpiar los datos y unificarlos (largo y mal escrito, pero funciona).