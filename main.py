#
# This function showcases how to easily set and adjust regions of interest.
#
# Copyright (c) 2019 Žiga Pisar <pisar.ziga@gmail.com>
# Licensed under the MIT license.
#

import cv2


def dragRoi(path, num):
    """Crop out one or two regions of interest (denoted as ROI).

        path = array, src image
        num  = int, flag to specify number of ROIs
                1 = one ROI
                2 = two ROIs        
        Controls:         
            <LMB>     - click and drag to select.
            <ENTER>   - confirm
            <C>       - clear selection
            <ESC>     - continue execution (second time is for exit)

            *Note: for two ROIs, click and select with LMB + ENTER for
                   the first, then select and press enter again for the
                   second ROI. To finish the process of selecting, press ESC.
    """

    img = cv2.imread(path)
    ROIs = cv2.selectROIs('Win', img, fromCenter=True, showCrosshair=True)

    if num is None:
        print('Error: Missing argument.')
        return   
    elif num == 1:        
        roi_1 = img[
            ROIs[0][1]:ROIs[0][1]+ROIs[0][3],
            ROIs[0][0]:ROIs[0][0]+ROIs[0][2]
        ]
        cv2.destroyWindow('Win')
        cv2.imshow('Roi_1', roi_1)
        return roi_1  
    elif num == 2:
        roi_1 = img[
            ROIs[0][1]:ROIs[0][1]+ROIs[0][3],
            ROIs[0][0]:ROIs[0][0]+ROIs[0][2]
        ]
        roi_2 = img[
            ROIs[1][1]:ROIs[1][1]+ROIs[1][3],
            ROIs[1][0]:ROIs[1][0]+ROIs[1][2]
        ]
        roi_3 = img[
            ROIs[1][1]:ROIs[1][1]+ROIs[1][3],
            ROIs[1][0]:ROIs[1][0]+ROIs[1][2]
        ]
        cv2.imshow('Roi_1', roi_1)
        cv2.imshow('Roi_2', roi_2)
#        cv2.imshow('roi_3', roi_3)
        return roi_1, roi_2  
dragRoi('images/lena.jpg', 2)

# Exit
if cv2.waitKey(0) == 27:
    print('Exited.')
    cv2.destroyAllWindows()
