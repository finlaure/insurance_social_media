El archivo "semilla.csv" tiene las cuentas y hashtags que busqué para armar el integral de la conversación, centrando en canales de seguros de asistencia al viajero y blogs de viajes que recomendaban salir con asistencia al viajero. Las conexiones encontradas tienen mayor frecuencia en los últimos 30 días, por el funcionamiento de las API, pero hay edges que datan de más de 5 años. En total hay más de 50.000 edges.

Los archivos de edges tienen 5 columnas:
 - ssnn: La red social de la interacción
 - interaccion: El tipo de interaccion estudiada:
    1) comment: comentario en instagram
    2) auto: retweets o reply de la persona sobre su propio timeline
    3) mentions: Mención en otro tweet
    4) quote: Cita en otro tweet
    5) reply: Respuesta a otro tweet
    6) retweet: Duplicación del tweet en otro timeline
 - target: La persona que hizo el post/tweet original
 - source: La persona que comenta, twittea, etc. sobre el perfil del otro
 - weight: La cantidad de veces que esa interacción se genera

Los archivos originales de grafos se llaman "insurance _(_ssnn_) _grafos _(_interaccion_).csv" y están en la carpeta correspondiente a la red social. El archivo final se llama insurance_grafos.csv

Dentro de las carpetas de las redes sociales también se encuentra una copia de los detalles de cada una de las cuentas principales que postearon en la temática (weight es la cantidad de tweets/posts levantados). El archivo "insurance_influencers.csv" tiene esta información integrada para las dos redes sociales, además de la cantidad de followers de las cuentas (tengo otros datos que pueden llegar a ser útiles si necesitás también).


Por último, cleaning.py es el script que usé para limpiar los datos y unificarlos (largo y mal escrito, pero funciona).
