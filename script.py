import pynder
import urllib.request
import os
import re


def getNumOfDownloadedImages():
    list_of_index = []
    number_of_images = 0

    pattern = re.compile(r"[0-9]+")

    for file in os.listdir("./images"):
        match = re.search(pattern, file)

        if (match is not None):
            index = match.group(0)
            list_of_index.append(int(index))

    number_of_images = max(list_of_index) + 1

    return number_of_images


if __name__ == "__main__":

    # latitude and longtitude of the location
    LAT = 37.786430
    LON = -122.409561

    # your Facebook ID and token

    XAuthToken = 'a02245eb-690c-444d-855e-af3d6e7c02dd'

    # authentication
    session = pynder.Session(XAuthToken=XAuthToken)

    # updates latitude and longitude
    session.update_location(LAT, LON)

    # returns a iterable of users nearby
    users = session.nearby_users()

    working_directory = "./images"

    try:
        print("==================================================================")
        for user in users:
            print("Name: " + user.name)
            print("Age:  " + str(user.age))

            if user.instagram_username:
                print("IG:   " + user.instagram_username)

            user_photos = list(user.photos)

            number_of_photos = len(user_photos)
            number_of_downloaded_images = getNumOfDownloadedImages()

            # download images
            for i, j in zip(range(number_of_downloaded_images, (number_of_downloaded_images + number_of_photos + 1)),
                            range(0, number_of_photos)):
                filename = "image" + str(i) + ".jpg"
                urllib.request.urlretrieve(user_photos[j], "./images/" + filename)

            # show schools
            for school in user.schools:
                print(school)

            print(user.bio)
            print("Distance: " + str(user.distance_km) + "km")
            print("==============================================================")
    except KeyError:
        print("Complete")
