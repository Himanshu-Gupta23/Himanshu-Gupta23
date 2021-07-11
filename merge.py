from moviepy.editor import VideoFileClip ,concatenate_videoclips
vid1=VideoFileClip('11.mp4')
vid2=VideoFileClip('22.mp4')

finalVideo=concatenate_videoclips([vid1,vid2])
finalVideo.write_videofile('FinalVideo.mkv')