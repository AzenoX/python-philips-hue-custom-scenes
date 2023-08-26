import _rooms as rooms

lamp_salon_canap = 1
lamp_salon_bureau = 2
lamp_salon_tv = 3
lamp_salon_alexis = 6
lamp_salon_clement = 5
lamp_chambre_alexis_plafonnier = 4
lamp_chambre_alexis_chevet = 7

all = {
    rooms.SALON: [
        lamp_salon_canap,
        lamp_salon_bureau,
        lamp_salon_tv,
        lamp_salon_clement,
        lamp_salon_alexis,
    ],
    rooms.CHAMBRE_ALEXIS: [
        lamp_chambre_alexis_plafonnier,
        lamp_chambre_alexis_chevet,
    ]
}

all_list = [
    lamp_salon_canap,
    lamp_salon_bureau,
    lamp_salon_tv,
    lamp_salon_clement,
    lamp_salon_alexis,
    lamp_chambre_alexis_plafonnier,
    lamp_chambre_alexis_chevet,
]

backups = {}
