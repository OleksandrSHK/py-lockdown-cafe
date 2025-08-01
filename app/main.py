from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    mask_count = 0
    not_vaccine = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccine = True
        except NotWearingMaskError:
            mask_count += 1
    if not_vaccine:
        return "All friends should be vaccinated"
    elif mask_count > 0:
        return f"Friends should buy {mask_count} masks"
    else:
        return "Friends can go to KFC"
