# posts/imagespecs.py

from imagekit.specs import ImageSpec 
from imagekit import processors 

# First we define our "processors". ImageKit ships with four configurable
# processors: Adjustment, Resize, Reflection and Transpose. You can also
# create your own processors. Processors are configured by subclassing and
# overriding specific class variables.

class ResizeAdminThumbnail(processors.Resize):
    width = 120
    height = 67
    crop = True
    
class ResizeMedium(processors.Resize):
    width = 340
    
class ResizeLarge(processors.Resize):
    width = 620
    
class EnhanceSmall(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1
    
# Next we define our specifications or "specs". Image specs are where we define
# the individual "classes" of images we want to have access to. Like processors
# image specs are configured by subclasses the ImageSpec superclass.
    
class AdminThumbnail(ImageSpec):
    access_as = 'admin_thumbnail'
    pre_cache = True
    processors = [ResizeAdminThumbnail, EnhanceSmall]

class Medium(ImageSpec):
    pre_cache = True
    processors = [ResizeMedium]

class Large(ImageSpec):
    pre_cache = True
    processors = [ResizeLarge]