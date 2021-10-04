import tensorflow as tf

def read_image_tf(file_name):
    image = tf.io.read_file(file_name)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    return image

def preproc_image_incv1(image):
    image = tf.image.resize_with_pad(image, target_height=224, target_width=224)
    image = tf.expand_dims(image, axis=0)
    return image