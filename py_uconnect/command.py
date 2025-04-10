from dataclasses import dataclass


@dataclass
class Command:
    name: str
    url: str = "remote"

    def __repr__(self):
        return self.name


COMMAND_ENGINE_ON = Command(name="REON")
COMMAND_ENGINE_OFF = Command(name="REOFF")
COMMAND_COMFORT_ON = Command(name="ROCOMFORTON")
COMMAND_COMFORT_OFF = Command(name="ROCOMFORTOFF")
COMMAND_HVAC_ON = Command(name="ROHVACON")
COMMAND_HVAC_OFF = Command(name="ROHVACOFF")
COMMAND_PRECOND_ON = Command(name="ROPRECOND")
COMMAND_PRECOND_OFF = Command(name="ROPRECOND_OFF")
COMMAND_LIGHTS_HORN = Command(name="HBLF")
COMMAND_LIGHTS = Command(name="ROLIGHTS")
COMMAND_DOORS_UNLOCK = Command(name="RDU")
COMMAND_DOORS_LOCK = Command(name="RDL")
COMMAND_TRUNK_UNLOCK = Command(name="ROTRUNKUNLOCK")
COMMAND_TRUNK_LOCK = Command(name="ROTRUNKLOCK")
COMMAND_LIFTGATE_UNLOCK = Command(name="ROLIFTGATEUNLOCK")
COMMAND_LIFTGATE_LOCK = Command(name="ROLIFTGATELOCK")
COMMAND_CHARGE = Command(name="CNOW", url="ev/chargenow")
COMMAND_DEEP_REFRESH = Command(name="DEEPREFRESH", url="ev")
COMMAND_REFRESH_LOCATION = Command(name="VF", url="location")

COMMANDS = [
    COMMAND_ENGINE_ON,
    COMMAND_ENGINE_OFF,
    COMMAND_COMFORT_ON,
    COMMAND_COMFORT_OFF,
    COMMAND_HVAC_ON,
    COMMAND_HVAC_OFF,
    COMMAND_PRECOND_ON,
    COMMAND_PRECOND_OFF,
    COMMAND_LIGHTS_HORN,
    COMMAND_LIGHTS,
    COMMAND_DOORS_UNLOCK,
    COMMAND_DOORS_LOCK,
    COMMAND_TRUNK_UNLOCK,
    COMMAND_TRUNK_LOCK,
    COMMAND_LIFTGATE_UNLOCK,
    COMMAND_LIFTGATE_LOCK,
    COMMAND_CHARGE,
    COMMAND_DEEP_REFRESH,
    COMMAND_REFRESH_LOCATION,
]

COMMANDS_BY_NAME = {x.name: x for x in COMMANDS}
