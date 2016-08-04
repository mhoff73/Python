from PIL import Image

#RGB values for the colors described
dark_blue = (0, 51, 76)
red = (217, 26, 33)
light_blue = (112, 150, 158)
yellow = (252, 227, 166)

im = Image.open("cat.jpeg")

data = im.getdata()	#gets the image data from im
data_list = list(data)	#puts the data into a list

# creates new color data based on the data of the original image
def create_new_image_data(image_data):
	
	new_pic = []
	
	#goes through the RGB values of each pixel in the image
	for pixel in image_data:
		red_val = pixel[0]
		green_val = pixel[1]
		blue_val = pixel[2]
		
		intensity = red_val + green_val + blue_val
		
		if intensity < 182:
			new_pic.append(dark_blue)
		elif intensity < 364:
			new_pic.append(red)
		elif intensity < 546:
			new_pic.append(light_blue)
		else:
			new_pic.append(yellow)
			
	return new_pic

new_data = create_new_image_data(data_list)	#calls the function and stores the new data
new_image = Image.new(im.mode, im.size)	#creates a new image
new_image.putdata(new_data)	#puts the new data in as pixel colors in the new image
new_image.show()	#shows the new image

new_im.save("output.jpg", "jpeg")	#saves the new image