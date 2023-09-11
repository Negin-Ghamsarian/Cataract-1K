

frame_rate = 59.94
frame_num = 6012
frame_sec = frame_num/frame_rate
minutes = frame_sec//60
seconds = frame_sec - (minutes*60)
time = '00:0' + str(int(minutes)) + ':' + str(seconds)
print(time)