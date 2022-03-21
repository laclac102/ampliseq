import os
from datetime import datetime

from multiqc.utils import config

template_dir = os.path.dirname(__file__)
base_fn = 'base.html'

template_parent = 'default'

# the default 'creation_date' is too granular
config.creation_time = datetime.now().strftime("%m-%d-%Y")
