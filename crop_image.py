import cv2

def crop_image(image_path, save_path, x, y, width, height):

    img = cv2.imread(image_path)

    cropped_img = img[y: y+height, x: x+width]

    cv2.imwrite(save_path, cropped_img)

def contrast_image(image_path, save_path, alpha, beta):

    img = cv2.imread(image_path)

    contrast_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    cv2.imwrite(save_path, contrast_img)

def flip_image(image_path, save_path, flip_code):
   
    img = cv2.imread(image_path)

    flipped_img = cv2.flip(img, flip_code)

    cv2.imwrite(save_path, flipped_img)

crop_image("images_unflipped/jpeg.jpg", "K:\image_opencv\cropped_image\cropped_image.jpg", x=200, y=100, width=700, height=1500)
flip_image("K:\\image_opencv\\images_unflipped\\jpeg.jpg", "K:\\image_opencv\\images_flipped\\flipped_image.jpg", flip_code=1)
contrast_image("K:\image_opencv\images_unflipped\jpeg.jpg", "K:\image_opencv\contrasted_image\contrast_img.jpg", alpha=0.2, beta=8)
