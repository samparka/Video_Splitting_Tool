import tensorflow as tf
# Read images from file.
def PSNR(im1, im2):
    psnr1 = tf.image.psnr(im1, im2, max_val=255)

    # Compute PSNR over tf.float32 Tensors.
    im1 = tf.image.convert_image_dtype(im1, tf.float32)
    im2 = tf.image.convert_image_dtype(im2, tf.float32)
    psnr2 = tf.image.psnr(im1, im2, max_val=1.0)
    print(psnr1)
    print(psnr2)


if __name__ == '__main__':
    im1 = tf.decode_png('Odd_Output_Frames/1.jpg')
    im2 = tf.decode_png('Even_Output_Frames/1.jpg')
    PSNR(im1, im2)
