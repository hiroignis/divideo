import os
import sys
import cv2
# KU SO CODE


def print_error(id_name, statement):
    print(id_name + ': ERROR:', statement)
    return


def print_system(id_name, command):
    print(id_name + ': SYSTEM:', command)
    return


class Video(object):
    """
    IGNIS
    video class
    """

    def __init__(self, filename, video_id, offset=0, show_size=3):
        if os.path.exists(filename):
            self.cap = cv2.VideoCapture(filename)
            self.ret, self.frame = self.cap.read()
        else:
            print_error(str(self._VIDEO_ID), filename + ' does not exist.')
            sys.exit()

        self._VIDEO_ID = video_id % 10
        self._SIZE = (self.frame.shape[1], self.frame.shape[0])
        self._SHOW_SIZE = show_size

        self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                  int(self.frame.shape[0] / self._SHOW_SIZE)))
        self.offset = offset

        self.video_number = 0
        self.frame_number = 0
        return

    def release_video(self):
        self.cap.release()
        cv2.destroyAllWindows()
        return

    def advance_offset(self):
        for i in range(0, self.offset):
            self.ret, self.frame = self.cap.read()
            self.frame_number += 1

            if i % 500 == 0:
                print_system(str(self._VIDEO_ID), 'advanced: ' + str(i))

        print_system(str(self._VIDEO_ID), str(self.frame_number))
        return

    def show(self):
        cv2.imshow('frame:' + str(self._VIDEO_ID), self.frame_show)
        return

    def control_video(self, command_key):

        if command_key & 0xff == ord('q'):
            print_system(str(-1), 'quit? : y')
            temp_key = cv2.waitKey(0)
            if temp_key & 0xff == ord('y'):
                return True
            else:
                print_system(str(-1), 'quit quitting')

        if command_key & 0xff == ord(str(self._VIDEO_ID)):
            self.ret, self.frame = self.cap.read()
            self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                      int(self.frame.shape[0] / self._SHOW_SIZE)))
            self.frame_number += 1
            print_system(str(self._VIDEO_ID), 'progress: ' + str(self.frame_number))

        elif command_key & 0xff == ord('o'):
            self.offset = self.frame_number
            print_system(str(self._VIDEO_ID), 'offset20161208: ' + str(self.offset))

        elif command_key & 0xff == ord('w'):
            self.ret, self.frame = self.cap.read()
            self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                      int(self.frame.shape[0] / self._SHOW_SIZE)))
            self.frame_number += 1
            print_system(str(self._VIDEO_ID), 'w progress: ' + str(self.frame_number))

        elif command_key & 0xff == ord('v'):
            for _ in range(0, 5):
                self.ret, self.frame = self.cap.read()
                self.frame_number += 1
            self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                      int(self.frame.shape[0] / self._SHOW_SIZE)))
            print_system(str(self._VIDEO_ID), 'v progress: ' + str(self.frame_number))

        elif command_key & 0xff == ord('x'):
            for _ in range(0, 10):
                self.ret, self.frame = self.cap.read()
                self.frame_number += 1
            self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                      int(self.frame.shape[0] / self._SHOW_SIZE)))
            print_system(str(self._VIDEO_ID), 'x progress: ' + str(self.frame_number))

        elif command_key & 0xff == ord('z'):
            for _ in range(0, 100):
                self.ret, self.frame = self.cap.read()
                self.frame_number += 1
            self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                      int(self.frame.shape[0] / self._SHOW_SIZE)))
            print_system(str(self._VIDEO_ID), 'z progress: ' + str(self.frame_number))

        return True


##################################################
DATE = '20161215/'
NAME_F = 'fC0005.MP4'
NAME_S = 'sC0005.MP4'
OFFSET_F = 500 + (0 * 60 + 20) * 60
OFFSET_S = 411 + (0 * 60 + 20) * 60
##################################################


FRONT = 'front/'
SIDE = 'side/'
FILENAME_F = 'I:IIGNIS/' + 'data/' + DATE + FRONT + NAME_F
FILENAME_S = 'I:IIGNIS/' + 'data/' + DATE + SIDE + NAME_S
VIDEO_ID_F = 0
VIDEO_ID_S = 1


if __name__ == '__main__':
    print_system(str(-1), 'have you set the correct initialization? : y')
    key = input('>>> ')

    if key != 'y':
        sys.exit()

    videos = [Video(filename=FILENAME_F, offset=OFFSET_F, video_id=VIDEO_ID_F),
              Video(filename=FILENAME_S, offset=OFFSET_S, video_id=VIDEO_ID_S)]

    flag_loop = True

    for video in videos:
        video.advance_offset()

    print_system(str(-1), ('progress offset20161208: 0: %d, 1: %d' % (videos[0].frame_number, videos[1].frame_number)))

    while True:
        key = cv2.waitKey(0)

        if key & 0xff == ord('q'):
            print_system(str(-1), 'quit? : y')
            key = cv2.waitKey(0)
            if key & 0xff == ord('y'):
                break
            else:
                print_system(str(-1), 'continue')

        for video in videos:
            flag_loop = video.control_video(key)
            video.show()
            if not flag_loop:
                break

        if not flag_loop:
            break

    for video in videos:
        video.release_video()
