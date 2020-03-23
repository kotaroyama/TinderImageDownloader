import pynder
import urllib
import os
import re


def getNumOfDownloadedImages():
    list_of_index = []
    number_of_images = 0

    pattern = re.compile(r"[0-9]+")

    # Look for images in the Images directory
    for file in os.listdir("./images"):
        match = re.search(pattern, file)

        # If the filename is "imageX.jpg", add the X to the list of all index
        if (match is not None):
            index = match.group(0)
            list_of_index.append(int(index))

    # Assign the number of images IF the directory is not empty
    if list_of_index != []:
        number_of_images = max(list_of_index) + 1

    return number_of_images


def main():
    # Latitude and longtitude of the location
    #   The default location is Times Square:
    #       LAT = 40.759010
    #       LON = -73.984474

    LAT = 40.759010
    LON = -73.984474

    # Your XAuthToken
    #   To get your XAuthToken, please refer to:
    #      "https://github.com/cjekel/tindetheus/issues/7#issuecomment-488878534"
    XAuthToken = ''

    # Authentication
    session = pynder.Session(XAuthToken=XAuthToken)

    # Update latitude and longitude
    session.update_location(LAT, LON)

    # Return the iterable of users nearby
    users = session.nearby_users()

    try:
        print("=============================================================")

        for user in users:
            # Optional: you can choose to swipe like the user
            # user.like()

            # Print the name and age of the user
            print("Name: " + user.name)
            print("Age:  " + str(user.age))

            # Print the Instagram username
            if user.instagram_username:
                print("IG:   " + user.instagram_username)

            # List of the Images uploaded by the user
            user_photos = list(user.photos)

            # The number of the images of the user
            number_of_photos = len(user_photos)

            # The number of the images already downloaded
            number_of_downloaded_images = getNumOfDownloadedImages()

            # Ranges to be used in the for loop to download all the images
            range_for_i = range(
                number_of_downloaded_images,
                (number_of_downloaded_images + (number_of_photos + 1))
            )

            range_for_j = range(0, number_of_photos)

            # Download images
            for i, j in zip(range_for_i, range_for_j):
                filename = "image" + str(i) + ".jpg"
                urllib.request.urlretrieve(
                    user_photos[j],
                    "./images/" + filename
                )

            # Print the schools
            for school in user.schools:
                print(school)

            # Print the bio
            print(user.bio)

            # Print the distance between the set locaiton and the user
            print("Distance: " + str(user.distance_km) + "km")
            print(
                "============================================================="
            )
    except KeyError:
        print("Complete")


if __name__ == "__main__":
    main()
