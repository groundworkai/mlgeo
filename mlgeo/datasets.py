# -- Imports ------------------------------------------------------------------
import sys
import os
if sys.version_info.minor <= 7:
    import pickle5 as pickle
else:
    import pickle
import urllib.request
import mlgeo
import pandas as pd



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

def load_isfogpiledriving(kind="featurematrix"):
    """
    Loads the ISFOG2020 pile driving dataset from the module directory (if previously downloaded)
    or from the remote repository.

    :param kind: Kind of data to download. If equal to ``"featurematrix"`` the featurematrix with pile dimensions, hammer performance and CPT data is downloaded. If equal to ``"fullcpt"`` the full CPT data is downloaded.

    :returns: Pandas dataframe with the data loaded from csv
    """
    if kind == "featurematrix":
        filename = "all_data_withnormalised.csv"
    elif kind == "fullcpt":
        filename = "full_cpt_data_withnormalised.csv"
    else:
        raise IOError("Argument kind must be one of 'featurematrix' or 'fullcpt'")

    if not os.path.isfile(os.path.join(mlgeo.dataset_path, filename)):
        print('-- Downloading dataset... Do not forget to cite authors. --')

        url = 'https://mlgeo-datasets.s3.eu-central-1.amazonaws.com/isfog-piledriving/' + filename
        urllib.request.urlretrieve(
            url, os.path.join(mlgeo.dataset_path, filename))

        print('-- Done --')

        data = pd.read_csv(os.path.join(mlgeo.dataset_path, filename))

        return data