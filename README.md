# TinderImageDownloader
A simple script that can download profile pictures based on the location that you provide. It can also log profiles.

# NOTE
This script no longer runs on the current version of [Pynder](https://github.com/charliewolf/pynder) because it gives a 401 error even with the right access token. Instead, please follow [this instruction](https://github.com/charliewolf/pynder/pull/211#issuecomment-491353236) to install an older version.

Also, before the initial run, create a directory named "images" if it doesn't already exist.

# Context
I started learning Python and became interested in web scraping. I found a very cool Tinder API called [Pynder](https://github.com/charliewolf/pynder) on Github. While playing around with it, I decided to create a simple image downloader.

# Authentication and Preparations
1. To run this script, you need to get a Tinder account using your Facebook profile and the access token (XAuthToken).
2. Using [the script I wrote](https://github.com/kotaroyama/Get-Tinder-XAuthToken) with Selenium to get the XAuthToken. You need to enter your Facebook email and password.
3. In line 63 of script.py, paste the XAuthToken obtained via the aforementioned script.
4. Run script.py. To stop, press Ctrl + C.
5. Images are saved in "images" folder and profiles are logged in "log.txt".

# Usage
You can simply run the script after you provide the necessary information. It will download profile pictures of the girls from Tinder based on the location. All the images are in images folder.
