'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 1A of Pharma Bot (PB) Theme (eYRC 2022-23).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			PB_#3275
# Author List:		Mathew V. Kariath, Rajath Thomas Kurain, Abhishek S, Alen Rajesh C.
# Filename:			task_1a.py
# Functions:		detect_traffic_signals, detect_horizontal_roads_under_construction, detect_vertical_roads_under_construction,
#					detect_medicine_packages, detect_arena_parameters
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
import cv2
import numpy as np
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################





##############################################################

def detect_traffic_signals(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list of
	nodes in which traffic signals are present in the image

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`traffic_signals` : [ list ]
			list containing nodes in which traffic signals are present
	
	Example call:
	---
	traffic_signals = detect_traffic_signals(maze_image)
	"""    
	traffic_signals = []

	##############	ADD YOUR CODE HERE	##############
	
	for i in range(100,800,100):
		for j in range(100,800,100):
			if (maze_image[i,j]==[0,0,255]).all():
				traffic_signals.append(chr(64+j//100)+str(i//100))
	traffic_signals.sort()
	
	##################################################
	
	return traffic_signals
	

def detect_horizontal_roads_under_construction(maze_image):
	
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing horizontal links

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`horizontal_roads_under_construction` : [ list ]
			list containing missing horizontal links
	
	Example call:
	---
	horizontal_roads_under_construction = detect_horizontal_roads_under_construction(maze_image)
	"""    
	horizontal_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	for i in range(100,800,100):
		for j in range(150,750,100):
		
			if (maze_image[i,j]==[255,255,255]).all():
				horizontal_roads_under_construction.append(chr(64+j//100)+str(i//100)+"-"+chr(65+j//100)+str(i//100))
					
        ##################################################
	
	return horizontal_roads_under_construction	

def detect_vertical_roads_under_construction(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing vertical links

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`vertical_roads_under_construction` : [ list ]
			list containing missing vertical links
	
	Example call:
	---
	vertical_roads_under_construction = detect_vertical_roads_under_construction(maze_image)
	"""    
	vertical_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	for i in range(150,750,100):
		for j in range(100,800,100):
			if (maze_image[i,j]==[255,255,255]).all():
				vertical_roads_under_construction.append(chr(64+j//100)+str(i//100)+"-"+chr(64+j//100)+str(i//100+1))

	##################################################
	
	return vertical_roads_under_construction


def detect_medicine_packages(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list of
	details of the medicine packages placed in different shops

	** Please note that the shop packages should be sorted in the ASCENDING order of shop numbers 
	   as well as in the alphabetical order of colors.
	   For example, the list should first have the packages of shop_1 listed. 
	   For the shop_1 packages, the packages should be sorted in the alphabetical order of color ie Green, Orange, Pink and Skyblue.

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`medicine_packages` : [ list ]
			nested list containing details of the medicine packages present.
			Each element of this list will contain 
			- Shop number as Shop_n
			- Color of the package as a string
			- Shape of the package as a string
			- Centroid co-ordinates of the package
	Example call:
	---
	medicine_packages = detect_medicine_packages(maze_image)
	"""    
	medicine_packages = []
	
	##############	ADD YOUR CODE HERE	##############
	
	x=[130,130,170,170]
	y=[130,170,130,170]
	c=0
	for i in range(1,7):
		shopno='Shop_'+str(i)
		d=0
		shape=''
		dt={"Green":[0,0],"Orange":[0,0],"Pink":[0,0],"Skyblue":[0,0]}
		for j in range(0,4):
			color=''
			if (maze_image[x[j],y[j]]==[0,255,0]).all():
				color="Green"
				
			elif (maze_image[x[j],y[j]]==[0,127,255]).all():
				color="Orange"
				
			elif (maze_image[x[j],y[j]]==[180,0,255]).all():
				color="Pink"
				
			elif (maze_image[x[j],y[j]]==[255,255,0]).all():
				color="Skyblue"
			dt[color]=[y[j],x[j]]
			if color=="Green"or color=="Orange"or color=="Pink"or color=="Skyblue":
				d+=1
				if d==1:
					if j==0 or j==1:
						cropped_image =maze_image[110:150,110+(i-1)*100+j*40:150+(i-1)*100+j*40]
					else:
						cropped_image =maze_image[150:190,110+(i-1)*100+(j-2)*40:150+(i-1)*100+(j-2)*40]
					imgGrey = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
					_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY_INV)
					contour,_ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
					for cnt in contour:
						approx = cv2.approxPolyDP(cnt, 0.01* cv2.arcLength(cnt, True), True)
						if len(approx)==3:
							shape="Triangle"
						elif len(approx)==4:
							shape="Square"
						else:
							shape="Circle"
			y[j]+=100
		for k in dt:
			if dt[k]!=[0,0]:
				medicine_packages.append([shopno,k,shape,dt[k]])     
		if d>0:
			c+=1
			if c>3:
				break  
			
	return medicine_packages

	##################################################

def detect_arena_parameters(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a dictionary
	containing the details of the different arena parameters in that image

	The arena parameters are of four categories:
	i) traffic_signals : list of nodes having a traffic signal
	ii) horizontal_roads_under_construction : list of missing horizontal links
	iii) vertical_roads_under_construction : list of missing vertical links
	iv) medicine_packages : list containing details of medicine packages

	These four categories constitute the four keys of the dictionary

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`arena_parameters` : { dictionary }
			dictionary containing details of the arena parameters
	
	Example call:
	---
	arena_parameters = detect_arena_parameters(maze_image)
	"""    
	arena_parameters = {}
	
	##############	ADD YOUR CODE HERE	##############
	
	arena_parameters['traffic_signals']=detect_traffic_signals(maze_image)
	arena_parameters['horizontal_roads_under_construction']=detect_horizontal_roads_under_construction(maze_image)
	arena_parameters['vertical_roads_under_construction']=detect_vertical_roads_under_construction(maze_image)
	arena_parameters['medicine_packages']=detect_medicine_packages(maze_image)
	
	##################################################
	
	return arena_parameters

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########	

if __name__ == "__main__":

    # path directory of images in test_images folder
	img_dir_path = "public_test_images/"

    # path to 'maze_0.png' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
	
	# read image using opencv
	maze_image = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor maze_' + str(file_num) + '.png')

	# detect and print the arena parameters from the image
	arena_parameters = detect_arena_parameters(maze_image)

	print("Arena Prameters: " , arena_parameters)

	# display the maze image
	cv2.imshow("image", maze_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 15):
			
			# path to maze image file
			img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
			
			# read image using opencv
			maze_image = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor maze_' + str(file_num) + '.png')
			
			# detect and print the arena parameters from the image
			arena_parameters = detect_arena_parameters(maze_image)

			print("Arena Parameter: ", arena_parameters)
				
			# display the test image
			cv2.imshow("image", maze_image)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()
