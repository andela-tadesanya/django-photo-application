from PIL import Image, ImageFilter
import os


# set the directory to the flags
FILE_DIR = os.path.dirname(__file__)


def double(source):
    '''creates the double effect on an image'''

    original_image = Image.open(source)

    # get heigth and width of original image
    original_width, original_height = original_image.size

    # create new image to paste on
    editted_image = Image.new('RGB', original_image.size)

    # paste original image on new image
    editted_image.paste(original_image, (0, 0))

    # blur editted_image
    # editted_image.filter(ImageFilter.GaussianBlur(radius=2))

    # editted_image.save('blur_lenna.png')
    blurred_original_image = original_image.filter(ImageFilter.GaussianBlur(radius=8))

    # resize original image to 80% of its original size
    resized_original_image = original_image.resize((int(original_width*0.8), int(original_height*0.8)), Image.ANTIALIAS)

    # coordinates for resized image in blurred image
    left = original_width * 0.1
    upper = original_height * 0.1

    # place resize image on blurred image
    blurred_original_image.paste(resized_original_image, (int(left), int(upper)))

    blurred_original_image.save(source)


def france(source):
    '''creates the france effect on an image'''

    flag = os.path.join(FILE_DIR, 'static', 'photo', 'img', 'flag', 'flag_france.png')

    original_image = Image.open(source)
    flag_image = Image.open(flag)

    # get heigth and width of original image
    original_width, original_height = original_image.size

    # resize the flag image to fit the size of the original image
    resized_flag_image = flag_image.resize((original_width, original_height), Image.ANTIALIAS)

    # paste flag image over original image
    original_image.paste(resized_flag_image, (0, 0), resized_flag_image)

    original_image.save(source)


def kenya(source):
    '''creates the kenya effect on an image'''

    flag = os.path.join(FILE_DIR, 'static', 'photo', 'img', 'flag', 'flag_kenya.png')

    original_image = Image.open(source)
    flag_image = Image.open(flag)

    # get heigth and width of original image
    original_width, original_height = original_image.size

    # resize the flag image to fit the size of the original image
    resized_flag_image = flag_image.resize((original_width, original_height), Image.ANTIALIAS)

    # paste flag image over original image
    original_image.paste(resized_flag_image, (0, 0), resized_flag_image)

    original_image.save(source)


def nigeria(source):
    '''creates the nigeria effect on an image'''

    flag = os.path.join(FILE_DIR, 'static', 'photo', 'img', 'flag', 'flag_nigeria.png')

    original_image = Image.open(source)
    flag_image = Image.open(flag)

    # get heigth and width of original image
    original_width, original_height = original_image.size

    # resize the flag image to fit the size of the original image
    resized_flag_image = flag_image.resize((original_width, original_height), Image.ANTIALIAS)

    # paste flag image over original image
    original_image.paste(resized_flag_image, (0, 0), resized_flag_image)

    original_image.save(source)


def russia(source):
    '''creates the russia effect on an image'''

    flag = os.path.join(FILE_DIR, 'static', 'photo', 'img', 'flag', 'flag_russia.png')

    original_image = Image.open(source)
    flag_image = Image.open(flag)

    # get heigth and width of original image
    original_width, original_height = original_image.size

    # resize the flag image to fit the size of the original image
    resized_flag_image = flag_image.resize((original_width, original_height), Image.ANTIALIAS)

    # paste flag image over original image
    original_image.paste(resized_flag_image, (0, 0), resized_flag_image)

    original_image.save(source)


def usa(source):
    '''creates the usa effect on an image'''
    flag = os.path.join(FILE_DIR, 'static', 'photo', 'img', 'flag', 'flag_usa.png')

    original_image = Image.open(source)
    flag_image = Image.open(flag)

    # get heigth and width of original image
    original_width, original_height = original_image.size

    # resize the flag image to fit the size of the original image
    resized_flag_image = flag_image.resize((original_width, original_height), Image.ANTIALIAS)

    # paste flag image over original image
    original_image.paste(resized_flag_image, (0, 0), resized_flag_image)

    original_image.save(source)
