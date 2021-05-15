from typing import Sequence
from genre_codes import genre_codes

ids_list = []

genre_select = genre_codes['genres']
for genre in genre_select:
    if genre['name'] == "Western":
        genre_id = genre['id']
        numbas.append(genre_id)
        break
if not ids_list:
    genre_id = None

print(genre_id)


#for numba in numbas:
#    if numba != None:
#        print(numba)
#
#        break

