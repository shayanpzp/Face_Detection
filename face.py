import cv2
import numpy as np




def stack_images(scale,image_list):
    
    rows = len(image_list)
    cols = len(image_list[0])

    rows_is_instance = isinstance(image_list[0], list)

    width = image_list[0][0].shape[1]
    height = image_list[0][0].shape[0]

    if rows_is_instance:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if image_list[x][y].shape[:2] == image_list[0][0].shape[:2]:
                    image_list[x][y] = cv2.resize(image_list[x][y], (0, 0), None, scale, scale)

                else:
                    image_list[x][y] = cv2.resize(image_list[x][y], (image_list[0][0].shape[1], image_list[0][0].shape[0]), None, scale, scale)
                
                if len(image_list[x][y].shape) == 2: image_list[x][y]= cv2.cvtColor( image_list[x][y], cv2.COLOR_BAYER_BG2BGR)

        empty_image = np.zeros((height, width, 3), np.uint8)
        horizontal = [empty_image]*rows

        for x in range(0, rows):
            horizontal[x] = np.hstack(image_list[x])

        vertical = np.vstack(horizontal)

    else:
        for x in range(0, rows):
            if image_list[x].shape[:2] == image_list[0].shape[:2]:
                image_list[x] = cv2.resize(image_list[x], (0, 0), None, scale, scale)

            else:
                image_list[x] = cv2.resize(image_list[x], (image_list[0].shape[1], image_list[0].shape[0]), None,scale, scale)
            
            if len(image_list[x].shape) == 2: image_list[x] = cv2.cvtColor(image_list[x], cv2.COLOR_BAYER_BG2BGR)

        horizontal= np.hstack(image_list)
        vertical = horizontal

    return vertical
