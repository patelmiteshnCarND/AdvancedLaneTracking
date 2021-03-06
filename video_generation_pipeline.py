
# Import everything needed to edit/save/watch video clips
from moviepy.editor import VideoFileClip
from IPython.display import HTML
from image_processing_pipeline import *

output = 'project_output_colour.mp4'
clip1 = VideoFileClip("project_video.mp4")#.subclip(31,43)
# output = 'harder_challenge_video_op.mp4'
# clip1 = VideoFileClip("harder_challenge_video.mp4")
output_clip = clip1.fl_image(image_processing_pipeline) #NOTE: this function expects color images!!
output_clip.write_videofile(output, audio=False)
# print('fitcount: ', fitcount)
