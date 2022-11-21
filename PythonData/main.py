# first all imports

print("Start importing...")

import tensorflow as tf
from tensorflow import keras
from pathlib import Path

print("Import complete")

# stepp 1: load the data


movielens_data_file_url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

movielens_zipped_file = keras.utils.get_file("ml-latest-small.zip", movielens_data_file_url, extract=False)

keras_datasets_path = Path(movielens_zipped_file).parents[0]

movielens_dir = keras_datasets_path / "ml-latest-small"
