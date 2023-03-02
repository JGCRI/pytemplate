import logging
import numpy

# Calculate building energy demand
#   dh energy demand per unit floorspace (GJ/m2) heating
#   dh energy demand per unit floorspace (GJ/m2) heating

# Inputs needed:
#   k unitless calibration coefficient
#   HDH heating degree hours
#   CDH cooling degree hours
#   n = thermal conductance (GJ/m2 hour C)
#   R = unitless average surface-to-floor area ratio
#   IG internal gain [GJ/m2]
#   uh = region and sector-specific demand satition for heating
#   uc = region and sector-specific demand satition for cooling
#   i = per-capita income
#   Ph = total price of service (weighted average of technologies used) heating
#   Pc = total price of service (weighted average of technologies used) cooling

# heating energy demand
# dh = kh (HDH.n.R - IG)[ 1 - exp( - (ln2/uh) . (i/Ph) ) ]

# cooling energy demand
# dc = kc (CDH.n.R - IG)[ 1 - exp( - (ln2/uc) . (i/Pc) )]

def demand(calibration_coefficient =1, degree_hours=1, thermal_conductance=1, surface_to_floor_ratio=1, internal_gain=1, satiation=1,
           income_per_capita=1, service_price=1):
    """
    :param calibration_coefficient:             Float for calibration coefficient (Unitless)
    :param degree_hours:                        Array for degree hours (Hours)
    :param thermal_conductance:                 Float for thermal conductance (GJ/m2 hour C)
    :param surface_to_floor_ratio:              Float for surface to floor ratio (Unitless)
    :param internal_gain:                       Float for Internal Gain (GJ/m2)
    :param satiation:                           Array for region and sector-specific demand satiation (unitless)
    :param income_per_capita:                   Array for per-capita income (2010 USD)
    :param service_price:                       Array for weighted average of technologies used (2010 USD)
    :return:                                    Array for demand
    """

    logging.info('Starting function demand.')

    technical_component = degree_hours * thermal_conductance * surface_to_floor_ratio - internal_gain
    economic_component = 1 - numpy.exp(- (numpy.log(2) / satiation) * (income_per_capita / service_price))
    demand = calibration_coefficient * technical_component * economic_component

    logging.info('Function demand completed.')

    return demand