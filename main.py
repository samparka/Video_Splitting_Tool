import cv2
import os
from PIL import Image

def video_to_frames(videos_path, odd_frames_save_path, even_frames_save_path):
    vidclip = cv2.VideoCapture(videos_path) #import the video file
    total_frames = int(vidclip.get(cv2.CAP_PROP_FRAME_COUNT))  #count the total frames num
    success, image = vidclip.read()
    count = 0
    odd_count = 0
    even_count = 0
    while success:
        success, image = vidclip.read()
        count += 1
        if (count % 2)==0:# divide the odd and even num
            even_count += 1
            cv2.imencode('.jpg', image)[1].tofile(even_frames_save_path + "/%d.jpg" % even_count)
        else:
            odd_count += 1
            cv2.imencode('.jpg', image)[1].tofile(odd_frames_save_path + "/%d.jpg" % odd_count)
        if count == total_frames-1:
            break

def frames_to_video(odd_frames_save_path, even_frames_save_path, output_video_path_o, output_video_path_e, videos_path):
    vid = cv2.VideoCapture(videos_path)
    fps= int(vid.get(cv2.CAP_PROP_FPS))/2 # detect the original video frame rate, /2 for the output video
    im_list = os.listdir(odd_frames_save_path)
    file_num = len(im_list)
    img = Image.open(os.path.join(odd_frames_save_path,im_list[0]))
    img_size = img.size
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') #Four-Character Codes
    videoWriter_o = cv2.VideoWriter(output_video_path_o, fourcc, fps, img_size)
    videoWriter_e = cv2.VideoWriter(output_video_path_e, fourcc, fps, img_size)

    for i in range(1,file_num):
        im_name_o = odd_frames_save_path+"/"+str(i)+".jpg"
        frame_o = cv2.imread(im_name_o)
        videoWriter_o.write(frame_o)
        im_name_e = even_frames_save_path+"/"+str(i)+".jpg"
        frame_e = cv2.imread(im_name_e)
        videoWriter_e.write(frame_e)
        os.remove(odd_frames_save_path+"/"+str(i)+".jpg")
        os.remove(even_frames_save_path + "/" + str(i) + ".jpg")
    print('Finished')

if __name__ == '__main__':
    videos_path = 'Input_Video/test.mp4'#chose the path of the vid
    odd_frames_save_path = 'Odd_Output_Frames' # path of the odd frames
    even_frames_save_path = 'Even_Output_Frames' # path of the even frames
    output_video_path_o = 'Output_Video/odd.mp4'  # path of the odd frames merged video
    output_video_path_e = 'Output_Video/even.mp4'  # path of the even frames merged video
    video_to_frames(videos_path, odd_frames_save_path, even_frames_save_path)
    frames_to_video(odd_frames_save_path, even_frames_save_path, output_video_path_o, output_video_path_e, videos_path)
