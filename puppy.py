
# # Module 2 - Critical Thinking - Option 1
# ## David Edwards
# ## November 28, 2021
#

import numpy as np
import cv2
import urllib.request
import matplotlib.pyplot as plt

# Donwload the image from the web
url = "https://frostlor-cdn-prod.courses.csuglobal.edu/lor/resources/src/89f79919-379b-3a8f-997a-98f3dd1d3a8a/shutterstock215592034--250.jpg"
urllib.request.urlretrieve(url, "puppy.jpg")

img = cv2.imread('puppy.jpg')
img.shape

# Display inline with matplotlib
plt.imshow(img)


# That doesn't look right.  That's right, OpenCV is BGR instead of RGB.  Let's reverse that and display it
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)


# Ok, let's break this out into red, green and blue channels.  My brain thinks in RGB, so even though these are in reverse numerical order, they make more sense to me.
r = img[:, :, 2]
g = img[:, :, 1]
b = img[:, :, 0]

r.shape
plt.imshow(r, cmap='gray')
cv2.imwrite('red.jpg', r)
plt.imshow(g, cmap='gray')
cv2.imwrite('green.jpg', g)
plt.imshow(b, cmap='gray')
cv2.imwrite('blue.jpg', b)


# Just out of curiosity, let's display the red channel as red.
#
# This image is counterintuitive to me, because I think that the nose, being black, should be the brightest.  However, because white is 255, that means that the closer the image is to white, the more red will show up.

red_img = np.zeros(img.shape, dtype=np.uint8)
red_img[:, :, 2] = r
plt.imshow(cv2.cvtColor(red_img, cv2.COLOR_BGR2RGB))


# Now, let's take the R, G and B channels and put them back together into a new image.  First we'll make a new image of the same shape with all blacks, then make sure it looks right.
new_img = np.zeros(img.shape, dtype=np.uint8)
plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))

# Now lets put them together.
new_img[:, :, 2] = r
new_img[:, :, 1] = g
new_img[:, :, 0] = b
plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))
cv2.imwrite('new_image.jpg', new_img)

# There's our new image!  Now let's swap the red and green channels.
red_green_swap = np.zeros(img.shape, dtype=np.uint8)
red_green_swap[:, :, 1] = r
red_green_swap[:, :, 2] = g
red_green_swap[:, :, 0] = b
plt.imshow(cv2.cvtColor(red_green_swap, cv2.COLOR_BGR2RGB))
cv2.imwrite('red_green_swap.jpg', red_green_swap)

# Because the puppy fur was warm brown colored, with a lot of red, it now shows as largely green.
