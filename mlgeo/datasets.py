# -- Imports ------------------------------------------------------------------
import sys
import os
if sys.version_info.minor <= 7:
    import pickle5 as pickle
else:
    import pickle
import urllib.request
import mlgeo



# -- Main Functions -----------------------------------------------------------
def load_slt():
    """Looks for the dataset in the module directory and if not found, it
    downloads the Driven Pile Static Load Test Dataset from the remote
    repository.

    :return: a dictionary with features, target and related information
    """
    filename = \
        'slt_data_' \
        + mlgeo.dataset_version['slt'][mlgeo.__version__] \
        + '.pickle'

    if not os.path.isfile(os.path.join(mlgeo.dataset_path, filename)):
        print('-- Downloading dataset... Do not forget to cite authors. --')

        url = 'https://storage.googleapis.com/mlgeo/slt/' + filename
        urllib.request.urlretrieve(
            url, os.path.join(mlgeo.dataset_path, filename))

        print('-- Done --')

    with open(os.path.join(mlgeo.dataset_path, filename), 'rb') as handle:
        data = pickle.load(handle)

    return data
