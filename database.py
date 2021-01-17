import os
from typing import Dict, List, Tuple

import sqlite3

conn = sqlite3.connect(os.path.join("database"  , "plans.db"))