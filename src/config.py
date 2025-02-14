# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "batch_python_tutorial_ffmpeg.py"

# Update the Batch and Storage account credential strings below with the values
# unique to your accounts. These are used when constructing connection strings
# for the Batch and Storage client objects.

_BATCH_ACCOUNT_NAME = 'byc'
_BATCH_ACCOUNT_KEY = 'cK37SzKrxCu24jRidvfCULRsrYp3OQu9AhClHCqKmi0bkemimooCy+snwtrckPoEVKJfBDDGGJSHrprvGgPBDQ=='
_BATCH_ACCOUNT_URL = 'https://byc.westus.batch.azure.com'
_STORAGE_ACCOUNT_NAME = 'videoprocessing'
_STORAGE_ACCOUNT_KEY = '/s7+i6U356P6c06+Ed20sw0vw13i+tRE3qZ+Z0vc4P2N9P2YqpW3MbdKlIow0L6a3ShY737hBJ0mcjFBqigGZQ=='
_POOL_ID = 'LinuxFfmpegPool'
_DEDICATED_POOL_NODE_COUNT = 0
_LOW_PRIORITY_POOL_NODE_COUNT = 5
_POOL_VM_SIZE = 'STANDARD_A1_v2'
_JOB_ID = 'LinuxFfmpegJob'
