import time
import sys
import os
import cv2
from pygame import mixer

# KU SO CODE


def print_error(id_name, statement):
    print(id_name + ': ERROR:', statement)
    return


def print_system(id_name, command):
    print(id_name + ': SYSTEM:', command)
    return


class Video2Auto(object):
    """
    IGNIS
    video class
    """

    def __init__(self, filename, save_video_path, divide_file,
                 offset=0, video_id=0,
                 fourcc=cv2.VideoWriter_fourcc(*'XVID'), fps=60, save_extension='.avi'):
        if os.path.exists(save_video_path):
            self._SAVE_VIDEO_PATH = save_video_path
        else:
            print_error(str(self._VIDEO_ID), save_video_path + ' does not exist.')
            self.release_video()
            sys.exit()

        self.cap = cv2.VideoCapture(filename)
        self.ret, self.frame = self.cap.read()

        self._VIDEO_ID = video_id % 10
        self._SIZE = (self.frame.shape[1], self.frame.shape[0])
        self._FOURCC = fourcc
        self._SAVE_EXTENSION = save_extension
        self._FPS = fps
        self._VIDEO_NAME = (filename.split('/')[-1]).split('.')[0]

        self.offset = offset

        self.video_number = 0
        self.frame_number = 0
        self.flag_record = False
        self._READ_FRAME_NUMBER_FILE = open(divide_file, 'r')
        offset_str = self._READ_FRAME_NUMBER_FILE.readline()
        print_system(str(self._VIDEO_ID), 'original offset: ' + offset_str)
        self.start_frame = self._READ_FRAME_NUMBER_FILE.readline()
        self.end_frame = '<-1'

        self.out = cv2.VideoWriter('dummy.avi', self._FOURCC, self._FPS, self._SIZE)
        self.out.release()
        return

    def release_video(self):
        self.cap.release()
        self._READ_FRAME_NUMBER_FILE.close()
        cv2.destroyAllWindows()
        return

    def advance_offset(self):
        for i in range(0, self.offset):
            self.ret, self.frame = self.cap.read()
            self.frame_number += 1

            if i % 500 == 0:
                print_system(str(self._VIDEO_ID), 'advanced: ' + str(i))

        print_system(str(self._VIDEO_ID), 'advanced: ' + str(self.frame_number))
        return

    def show(self):
        cv2.imshow('frame:' + str(self._VIDEO_ID), self.frame)
        cv2.waitKey(1)
        return

    def control_video(self):
        self.ret, self.frame = self.cap.read()

        if self.flag_record:
            self.out.write(self.frame)

        if self.frame_number == (int(self.start_frame[1:]) + self.offset) and self.start_frame[0] == '>':
            self.flag_record = True
            print_system(str(self._VIDEO_ID), 'start saving video, ' +
                         'frame: ' + str(self.frame_number) + '; ' + str(self.frame_number - self.offset))

            self.out = cv2.VideoWriter(self._SAVE_VIDEO_PATH + 'div_' + str(self._VIDEO_ID) + '_' +
                                       self._VIDEO_NAME + '_' + ('%06d' % self.video_number) + self._SAVE_EXTENSION,
                                       self._FOURCC, self._FPS, self._SIZE)

            self.out.write(self.frame)
            self.end_frame = self._READ_FRAME_NUMBER_FILE.readline()
            if self.end_frame is '':
                print_error(str(self._VIDEO_ID), 'nowhere end frame number started with < ')
                return False

        if self.frame_number == (int(self.end_frame[1:]) + self.offset) and self.end_frame[0] == '<':
            self.flag_record = False
            self.video_number += 1
            print_system(str(self._VIDEO_ID), 'finish recording video, ' +
                         'frame: ' + str(self.frame_number) + '; ' + str(self.frame_number - self.offset))
            self.out.release()
            self.start_frame = self._READ_FRAME_NUMBER_FILE.readline()
            if self.start_frame is '':
                return False

        self.frame_number += 1

        return True


##################################################
DATE = '20161215/'
DIRECTION = 'side/'
NAME = 'sC0005.MP4'
DIVIDE_FILE_NAME = 'dt_fC0005.MP4.txt'
STATE = 'double/'
OFFSET = 411 + (0 * 60 + 20) * 60
##################################################

FILENAME = 'I:IIGNIS/' + 'data/' + DATE + DIRECTION + NAME
SAVE_VIDEO_PATH = 'dev/divideo/' + DATE + DIRECTION + STATE
DIVIDE_FILE_PATH = 'dev/divtext/' + DATE + 'front/'
DIVIDE_FILE = DIVIDE_FILE_PATH + DIVIDE_FILE_NAME


if __name__ == '__main__':
    print_system(str(-1), 'have you set the correct initialization? : y')
    key = input('>>> ')

    if key != 'y':
        sys.exit()

    video = Video2Auto(filename=FILENAME, save_video_path=SAVE_VIDEO_PATH, divide_file=DIVIDE_FILE,
                       offset=OFFSET, video_id=1)

    flag_loop = True

    video.advance_offset()

    while True:
        flag_loop = video.control_video()
        # video.show()

        if not flag_loop:
            break

    video.release_video()

    mixer.init()
    mixer.music.load('refresh.mp3')
    mixer.music.play(1)

    mixer.music.set_volume(0.8)

    time.sleep(8)
    mixer.music.stop()
