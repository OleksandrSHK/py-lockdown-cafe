import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("All friends should be vaccinated")
        expiration_date = visitor["vaccine"]["expiration_date"]
        today_date = datetime.date.today()
        if expiration_date < today_date:
            raise OutdatedVaccineError("All friends should be vaccinated")
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Friends should buy count masks")
        else:
            return f"Welcome to {self.name}"
