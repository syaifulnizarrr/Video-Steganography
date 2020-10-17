from moviepy.editor import *
import os
import sys


def convert_frames_to_video(frames_folder):
    """Converts all frames to a video"""
    frames = [frames_folder + '/' + img for img in os.listdir(frames_folder) if img.endswith('.png')]
    video_object = ImageSequenceClip(frames, fps=25)
    return video_object


def combine_audio_video(video_object, audio_object, base_filename):
    """Combines an audio and a video object together"""
    with_audio = video_object.set_audio(audio_object)
    with_audio.write_videofile(filename=f'{base_filename}_image+audio_combined.mp4')


def main():
    # try:
    frames_folder, audio_filename = sys.argv[1], sys.argv[2]
    # print(frames_folder, audio_filename)
    base_filename = os.path.splitext(os.path.basename(audio_filename))[0]
    video_object = convert_frames_to_video(frames_folder)
    audio_object = AudioFileClip(audio_filename)
    combine_audio_video(video_object, audio_object, base_filename)
    # except ValueError:
    #     print("Invalid filenames!")

if __name__ == '__main__':
    main()