'''
Module's main function:
+ Creating an RGB Bitmap image of 128*128 pixel
'''
import requests
import json

from PIL import Image

#Function to generate a 128*128 Bitmap image of a random color
def generate_image():
    http_url = "https://www.random.org/integers/?num=1&min=0&max=255&col=1&base=10&format=plain&rnd=new"
    random_num = requests.get(http_url)
    new_img = Image.new( 'RGB', (128,128)) # creating a new image
    pixels = new_img.load() # creating the pixel map
    for i in range(new_img.size[0]):    # for every pixel:
        for j in range(new_img.size[1]):
            pixels[i,j] = (i, j,random_num.json()) # set the colour accordingly
    new_img.show()


#Main Logic
quota_url = "https://www.random.org/quota/?format=plain"
validate_quota = requests.get(quota_url).json() 
if(validate_quota > -1):
    generate_image()
    

    
    
    
    
    

    
