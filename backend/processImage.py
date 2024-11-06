import cv2
from PIL import Image


def get_corners(image_path: str)->list[tuple]:

    # 1) load image
    # ===========================================================================================
    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # 2) apply edge detection to find contours
    # =========================================================================================
    edges = cv2.Canny(image_gray, 50, 150, apertureSize=3)


    # 3) find contours
    # =========================================================================================
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # 4) initialize variables for storing corners
    # =========================================================================================
    box_corners = None


    # 5) filter contours to find the rectangular box
    # =========================================================================================
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Look for a rectangle (4 vertices)
        if len(approx) == 4:
            box_corners = approx
            break

    # 6) append corners to image
    # =========================================================================================
    res = []
    if box_corners is not None:
        for corner in box_corners:
            temp_tup = (corner[0][0], corner[0][1])
            res.append(temp_tup)
            #print(corner)


    # 7) return res (we will use idx 0 & 2)
    # =========================================================================================
    return res


def crop_image(x1:int, y1:int, x2:int, y2:int, src_path:str, dest_path:str)->None:
    # 1) crop & save result
    # =========================================================================================
    image = Image.open(src_path)
    cropped_image = image.crop((x1, y1, x2, y2))
    cropped_image.save(dest_path)  # Save the cropped image

    # 2) return
    # =========================================================================================
    return None