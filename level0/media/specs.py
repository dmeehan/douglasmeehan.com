# media/specs.py

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

class ResizeThumbnail(processors.Resize):
    width = 160
    height = 90
    crop = True
    quality = 100

class ResizeSmall(processors.Resize):
    width = 300
    quality = 100

class ResizeMedium(processors.Resize):
    width = 460
    quality = 100
    
class ResizeLarge(processors.Resize):
    width = 670
    height = 379
    crop = True
    quality = 100

class ResizeMax(processors.Resize):
    width = 1080
    quality = 100

class ResizeTile(processors.Resize):
    width = 300
    height = 300
    crop = True
    quality = 100

class ResizeTileLarge(processors.Resize):
    width = 480
    height = 270
    crop = True
    quality = 100
    
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

class Small(ImageSpec):
    processors = [ResizeSmall]

class Large(ImageSpec):
    increment_count = True
    processors = [ResizeLarge]
    
class Max(ImageSpec):
    increment_count = True
    processors = [ResizeMax]

class Tile(ImageSpec):
    processors = [ResizeTile, EnhanceSmall]

class TileLarge(ImageSpec):
    processors = [ResizeTileLarge]
        
class Thumbnail(ImageSpec):
    processors = [ResizeThumbnail, EnhanceSmall]
    pre_cache = True
