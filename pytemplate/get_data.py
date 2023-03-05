import os
import zipfile
import requests
from urllib.parse import urlparse
from tqdm import tqdm
import logging


def get_data(folder=os.path.join(os.getcwd(),'downloaded_data'), link='https://github.com/JGCRI/pytemplate/raw/dev/examples.zip'):
    """Download and unpack example data supplement from Zenodo current installed distribution.
    :param folder:              Full path to the folder to save data to
    :type folder:               str
    :param link:                Full path to data download link
    :type link:                 str
    return                      save_path as a string
    """

    logging.info('Starting function get_data...')

    # Check if folder exists
    exists = os.path.exists(folder)
    if not exists:
        # Create a new directory because it does not exist
        os.makedirs(folder)
        logging.info(f'Created folder: {folder}.')

    try:
        r = requests.get(link, stream=True)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        logging.error(err)
    except requests.exceptions.HTTPError as errh:
        logging.error(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        logging.error(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        logging.error(f"Timeout Error: {errt}")

    file_name = os.path.basename((urlparse(link)).path)
    save_path = os.path.join(folder, file_name)

    # Progress bar and download
    logging.info(f'Downloading file to {save_path}...')
    total_size_in_bytes = int(r.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(save_path, 'wb') as file:
        for data in r.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
    logging.info(f'File downloaded to {save_path}.')

    if zipfile.is_zipfile(save_path):
        with zipfile.ZipFile(save_path,'r') as zipped:
            logging.info(f'Unzipping: {zipped} to folder: {os.path.abspath(folder)}...')
            zipped.extractall(path=folder)
            logging.info(f'Unzipping: {zipped} to folder: {os.path.abspath(folder)} complete.')

    logging.info('Function get_data complete.')

    return os.path.splitext(save_path)[0]
