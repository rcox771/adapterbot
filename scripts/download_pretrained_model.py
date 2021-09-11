import gdown
import zipfile
import os


url = 'https://drive.google.com/uc?id=1JQZex-AD-sa5WUT5U4lIn1K2sPW-us8a/'
output = 'models.zip'
gdown.download(url, output, quiet=False)
with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall()
os.remove(output)
