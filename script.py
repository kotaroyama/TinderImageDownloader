import pynder
import urllib.request

# latitude and longtitude of the location
LAT = 38.897676
LON = -77.036530

# your Facebook ID and token
facebook_id = ''
facebook_token = ''

# authentication
session = pynder.Session(facebook_id, facebook_token)

# updates latitude and longitude
session.update_location(LAT, LON)

# returns a iterable of users nearby
users = session.nearby_users()

working_directory = "./images"

# open and read last_index.txt
with open(working_directory + '/last_index.txt', 'r') as f:
    x = int(f.read())

try:
    print("==================================================================")
    for user in users:
        print("Name: " + user.name)
        print("Age:  " + str(user.age))

        if user.instagram_username:
            print("IG:   " + user.instagram_username)

        number_of_photos = len(user.photos)

        # download images
        for i, j in zip(range(x, (x + number_of_photos + 1)),
                        range(0, number_of_photos)):
            filename = "image" + str(i) + ".jpg"
            urllib.request.urlretrieve(user.photos[j], "./images/" + filename)

            if j == number_of_photos - 1:
                with open('./images/last_index.txt', 'w') as f:
                    f.write(str(i + 1))

        # show schools
        for school in user.schools:
            print(school)

        print(user.bio)
        print("Distance: " + str(user.distance_km) + "km")
        print("==============================================================")
except KeyError:
    print("Complete")
