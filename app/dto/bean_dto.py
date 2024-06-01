from pydantic import BaseModel
from decimal import Decimal

class BeanDto(BaseModel):
    major_axis_length: Decimal
    minor_axis_length: Decimal
    aspect_ration: Decimal
    eccentricity: Decimal
    convex_area: int
    equiv_diameter: Decimal
    extent: Decimal
    solidity: Decimal
    roundness: Decimal
    shape_factor_1: Decimal
    shape_factor_2: Decimal
    shape_factor_4: Decimal