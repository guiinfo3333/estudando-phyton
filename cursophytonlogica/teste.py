from math import radians, sin, cos, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2):
    # Raio médio da Terra em quilômetros
    raio_terra = 6371.0

    # Converte graus de latitude e longitude para radianos
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Calcula as diferenças absolutas das latitudes e longitudes
    delta_lat = abs(lat2 - lat1)
    delta_lon = abs(lon2 - lon1)

    # Calcula a distância haversine entre as coordenadas
    a = sin(delta_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia_km = raio_terra * c

    # Calcula a distância Manhattan
    distancia_manhattan = delta_lat + delta_lon + distancia_km

    return distancia_manhattan

# Exemplo de uso
lat1 = -3.7598139   #Latitude do ponto 1
lon1 = -38.6378107  #Longitude do ponto 1
lat2 = -3.7604675   #Latitude do ponto 2
lon2 = -38.6351776  #Longitude do ponto 2

dist_manhattan = haversine(lat1, lon1, lat2, lon2)
print(f'Distância Manhattan entre os pontos: {dist_manhattan:.2f} quilômetros')