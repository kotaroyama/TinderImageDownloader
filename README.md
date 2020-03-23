# TinderImageDownloader
A simple script that can download profile pictures based on the location that you provide.

# NOTE
This script no longer runs on the current version of [Pynder](https://github.com/charliewolf/pynder). Instead, please use [this one](https://github.com/charliewolf/pynder/pull/211).

# Context
I started learning Python and became interested in web scraping. I found a very cool Tinder API called [Pynder](https://github.com/charliewolf/pynder) on Github. While playing around with it, I decided to create a simple image downloader.

# Authentication and Preparations
1. To run this script, you need to get a Facebook Authentication Token. I got mine by running [this script](https://gist.github.com/juliojgarciaperez/31ccb391cb1fbcb04dc86a16038fca24). All you need is your Facebook email and password. You can also refer to [this page](https://gist.github.com/taseppa/66fc7239c66ef285ecb28b400b556938).
2. Please get your XAuthToken by referring to [this page](https://github.com/cjekel/tindetheus/issues/7#issuecomment-48887853).
3. Also, you need your Facebook ID. You can get it from [this website](https://findmyfbid.in/).If this website doesn't work, you can go to your Facebook profile page, click on the profile picture, and the "fbid" should be included in the URL. [Example](https://www.quora.com/How-do-I-find-my-Facebook-user-ID)
4. You have to [get the latitude and longitude of the location](https://www.latlong.net/). Times Square is the default location.

# Usage
You can simply run the script after you provide the necessary information. It will download profile pictures of the girls from Tinder based on the location. All the images are in images folder.

# Other
I'm open to suggestions. Thank you!
