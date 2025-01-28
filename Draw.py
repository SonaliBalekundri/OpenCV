import cv2 as cv
import numpy as np
from numpy.lib.function_base import bartlett  # Not used in the script but imported

# Create a blank image (750x750) with 3 color channels (RGB), initialized to black
blank = np.zeros((750, 750, 3), dtype='uint8')
cv.imshow('Blank', blank)  # Show the blank image

'''
1. Paint the image in a yellow color
   - This section updates a region of the blank image with a yellow color (BGR: 0, 255, 255).
   - The region painted is from row 200 to 300 and column 300 to 400.
'''
blank[200:300, 300:400] = (0, 255, 255)  # Paint a region yellow (BGR color)
cv.imshow('Yellow', blank)  # Display the updated image

'''
2. Draw a rectangle
   - This section draws a green rectangle on the image using cv.rectangle().
   - The top-left corner of the rectangle is at (0, 0) and the bottom-right corner is at (250, 250).
   - The color of the rectangle is green (BGR: 0, 255, 0), and the thickness of the rectangle's border is 3 pixels.
'''
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=3)  # Draw a green rectangle
# Alternative: A rectangle filling half the image with green (uncomment to use).
# cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)  # Display the image with the rectangle

'''
3. Draw a Circle
   - This section draws a red circle at the center of the image using cv.circle().
   - The center of the circle is at the center of the image (half of width and height).
   - The radius of the circle is 40 pixels, and the color is red (BGR: 0, 0, 255).
   - The thickness of the circle's border is 3 pixels.
'''
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=3)  # Draw a red circle
cv.imshow('Circle', blank)  # Display the image with the circle

'''
4. Draw a Line
   - This section draws a red line on the image using cv.line().
   - The line starts from the top-left corner (0, 0) and ends at the center of the image.
   - The color of the line is red (BGR: 0, 0, 255), and the thickness is 3 pixels.
'''
cv.line(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 0, 255), thickness=3)  # Draw a red line
# Alternative: A line from (100, 250) to (300, 400) (uncomment to use).
# cv.line(blank, (100, 250),(300, 400), (0, 0, 255), thickness=3)
cv.imshow('Line', blank)  # Display the image with the line

'''
5. Add Text to the Image
   - This section adds the text 'Welcome Coder_13' to the image using cv.putText().
   - The text is placed at position (255, 255) on the image.
   - The font used is cv.FONT_HERSHEY_TRIPLEX with a font scale of 1.0 and a thickness of 2.
   - The color of the text is green (BGR: 0, 255, 0).
'''
cv.putText(blank, 'Welcome Coder_13', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)  # Add text to the image
cv.imshow('Text', blank)  # Display the image with the text

# Wait until a key is pressed and then close all OpenCV windows
cv.waitKey(0)
