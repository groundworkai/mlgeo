"""
Repository for Machine Learning in Geotechnics
==============================================

MLgeo is the beginning of an exciting effort in lowering the
barrier of entry to Machine Learning for Geoprofessionals by:

  - Distributing relevant and interesting toy datasets
    to practice with (now)
  - Offering tools that can make applying ML easier,
    especially for beginners (soon)

For more, visit https://github.com/groundworkai/mlgeo
"""

__version__ = '0.0.2'

import os


# -- Create a directory to store data -----------------------------------------
module_path = os.path.dirname(__file__)
dataset_path = os.path.join(module_path, '_datasets')

if not os.path.isdir(dataset_path):
    os.mkdir(dataset_path)


# -- Keeping track of library and dataset versions
dataset_version = {
    'slt': {
        '0.0.2': '0.0.2'
    }
}
