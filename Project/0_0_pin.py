from PIL import Image
from pylab import *

im = array(Image.open('matlab/000000.jpg'))
imshow(im)
print 'Please click 20 points'
x = ginput(100)
print x
show()

# first time pick 5 points
# however the first point appears in the pedestrains
# (727,230)
# (313,466)
# (909,578)
# (100,860)
# (1788,799)
# (1540,296)

# second time picks
# [[894,586],[1652,481],[1799,780],[1540,269],[1420,125],[905,176],[247,447],[89,791],[69,466]]
