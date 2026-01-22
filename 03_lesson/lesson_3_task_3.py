from address import Address
from mailing import Mailing

to_address_mailing = Address("58738", "City-2", "West Orion-st", "32", "3")
from_address_mailing = Address("56732", "City-1", "1-st", "3/2", "53")
cost_mailing = 100
track_mailing = "735"

mailing = Mailing(to_address_mailing, from_address_mailing, cost_mailing, track_mailing)

print(f"Отправление {track_mailing} из {from_address_mailing} в {to_address_mailing}. Стоимость {cost_mailing} рублей.")
