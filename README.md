# TinderImageDownloader
A simple script that can download profile pictures based on the location that you provide.

# Context
I started learning Python and became interested in web scraping. I found a very cool Tinder API called [Pynder](https://github.com/charliewolf/pynder) on Github. While playing around with it, I decided to create a simple image downloader.

# Authentication and Preparations
1. To run this script, you need to get a Facebook Authentication Token. I got mine by running [this script](https://gist.github.com/juliojgarciaperez/31ccb391cb1fbcb04dc86a16038fca24). All you need is your Facebook email and password.
2. Also, you need your Facebook ID. You can get it from [this website](https://findmyfbid.in/).
3. You have to [get the latitude and longtitude of the location](https://mynasadata.larc.nasa.gov/latitudelongitude-finder/). The White House is the default location. 

# Usage
You can simply run the script after you provide the necessary information. It will download profile pictures of the girls from Tinder based on the location. All the images are in images folder.

## *I realized you simply don't need to do any of the following:*
~~The only way you can make changes to the image folder is deleting or moving all the images to somewhere else. After doing so, please follow these steps:~~

~~1. Open 'last_index.txt.'~~
~~2. Erase all the content.~~
~~3. Enter 0.~~
~~4. Save it.~~

# Other
Since I'm a beginner, I know my code sucks, so I'm open to suggestions. Thank you!
