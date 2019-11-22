# First we load the configuration files, in the main Solcore4 folder and in the user
# folder, if present.
import os
from configparser import ConfigParser
from pathlib import Path

SOLCORE_ROOT = os.path.split(__file__)[0]
DATA = Path(__file__).parent / "data"
default_config = os.path.join(SOLCORE_ROOT, "solcore_config.cfg")
user_config = os.path.join(os.path.expanduser("~"), ".solcore_config.cfg")

config = ConfigParser()
config.read([default_config, user_config])

version = config.get("Configuration", "version")
welcome_message = bool(int(config.get("Configuration", "welcome_message")))
verbose = bool(int(config.get("Configuration", "verbose_loading")))

if welcome_message:
    print(
        """\n\tWelcome to Solcore - version {}
\tCopyright (c) 2019, Imperial College London. All rights reserved.
\tSoftware released under the GNU Lesser General Public License.\n""".format(
            version
        )
    )


# Now we load the Units system, making available in the solcore scope some functions
# internal to the system
from .units_system import UnitsSystem  # isort:skip

# First we populate the Units system:
UnitsSystem(config["Units"])

# And now we load some functions form it.
si = UnitsSystem().si
asUnit = UnitsSystem().asUnit
siUnits = UnitsSystem().siUnits
sensibleUnits = UnitsSystem().sensibleUnits
siUnitFromString = UnitsSystem().siUnitFromString
convert = UnitsSystem().convert
guess_dimension = UnitsSystem().guess_dimension
nmJ = UnitsSystem().nmJ
mJ = UnitsSystem().mJ
eVnm = UnitsSystem().eVnm
nmHz = UnitsSystem().nmHz
spectral_conversion_nm_ev = UnitsSystem().spectral_conversion_nm_ev
spectral_conversion_nm_hz = UnitsSystem().spectral_conversion_nm_hz
eV = UnitsSystem().eV

# And the same with the Parameter system
from .materials import ParameterSystem  # isort:skip

ParameterSystem(config["Parameters"])
get_parameter = ParameterSystem().get_parameter

# And the same with the Materials system
from .materials import MaterialSystem  # isort:skip

MaterialSystem(config["Materials"])
material = MaterialSystem().material
