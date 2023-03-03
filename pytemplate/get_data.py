import os
import zipfile
import requests

from pkg_resources import get_distribution
from io import BytesIO as BytesIO


class InstallSupplement:
    """Download and unpack example data supplement from Zenodo that matches the current installed distribution.
    :param example_data_directory:              Full path to the directory you wish to install
                                                example data to.  Must be write-enabled
                                                for the user.
    """

    # URL for download link for zipped data on zenodo or github
    DATA_VERSION_URLS = {'2.4.0': 'https://zenodo.org/record/2578287/files/example.zip?download=1'}

    def __init__(self, example_data_directory):

        # full path to the Xanthos root directory where the example dir will be stored
        self.example_data_directory = example_data_directory

    def fetch_data(self):
        """Download and unpack the example data supplement for the
        current distribution."""

        # get the current version that is installed
        current_version = get_distribution('xanthos').version

        try:
            data_link = InstallSupplement.DATA_VERSION_URLS[current_version]

        except KeyError:
            msg = "Link to data missing for current version:  {}.  Please contact admin."
            raise(msg.format(current_version))

        # retrieve content from URL
        print("Downloading example data for current package version {}...".format(current_version))
        r = requests.get(data_link)

        with zipfile.ZipFile(BytesIO(r.content)) as zipped:

            # extract each file in the zipped dir to the project
            for f in zipped.namelist():
                print("Unzipped: {}".format(os.path.join(self.example_data_directory, f)))
                zipped.extract(f, self.example_data_directory)


def get_package_data(folder=os.getcwd(), link = 'https://zenodo.org/record/2578287/files/example.zip?download=1'):
    """Download and unpack example data supplement from Zenodo current installed distribution.
    :param folder:              Full path to the folder to save data to
    :type folder:               str
    :param link:                Full path to data download link
    :type link:                 str
    """

    # retrieve content from URL
        print("Downloading example data for current package version {}...".format(current_version))
        r = requests.get(data_link)