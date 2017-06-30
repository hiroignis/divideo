import sys
import os
import cv2
# KU SO CODE


def print_error(id_name, statement):
    print(id_name + ': ERROR:', statement)
    return


def print_system(id_name, command):
    print(id_name + ': SYSTEM:', command)
    return


class Video2(object):
    """
    IGNIS
    video class
    """

    def __init__(self, filename, save_video_path, save_text_path,
                 offset=0, video_id=0, show_size=3,
                 fourcc=cv2.VideoWriter_fourcc(*'XVID'), fps=60, save_extension='.avi'):
        self._VIDEO_ID = video_id % 10
        self._SHOW_SIZE = show_size
        self._FOURCC = fourcc
        self._SAVE_EXTENSION = save_extension
        self._FPS = fps
        self.offset = offset
        self.video_number = 0
        self.frame_number = 0
        self.flag_record = False
        self._VIDEO_NAME = (filename.split('/')[-1]).split('.')[0]

        if os.path.exists(save_video_path):
            self._SAVE_VIDEO_PATH = save_video_path
        else:
            print_error(str(self._VIDEO_ID), save_video_path + ' does not exist.')
            sys.exit()

        if os.path.exists(filename):
            self.cap = cv2.VideoCapture(filename)
            self.ret, self.frame = self.cap.read()
        else:
            print_error(str(self._VIDEO_ID), filename + ' does not exist.')
            sys.exit()

        self._SIZE = (self.frame.shape[1], self.frame.shape[0])

        self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                  int(self.frame.shape[0] / self._SHOW_SIZE)))

        if os.path.exists(save_text_path) and \
                not os.path.exists(save_text_path + 'dt_' + filename.split('/')[-1] + '.txt'):
            self._SAVE_TEXT_PATH = save_text_path
            self._SAVE_FRAME_NUMBER_FILE = open(self._SAVE_TEXT_PATH + 'dt_' + filename.split('/')[-1] + '.txt', 'w')
            self._SAVE_FRAME_NUMBER_FILE.write('# ' + str(offset) + '\n')
        else:
            print_error(str(self._VIDEO_ID), save_text_path + 'dt_' + filename.split('/')[-1] + '.txt'
                        + ' has already existed or no such directory.')
            sys.exit()

        self.out = cv2.VideoWriter('dummy.avi', self._FOURCC, self._FPS, self._SIZE)
        self.out.release()
        return

    def release_video(self):
        self._SAVE_FRAME_NUMBER_FILE.close()
        self.cap.release()
        cv2.destroyAllWindows()
        return

    def advance_offset(self):
        for i in range(0, self.offset):
            self.ret, self.frame = self.cap.read()
            self.frame_number += 1

            if i % 500 == 0:
                print_system(str(self._VIDEO_ID), 'advanced: ' + str(i))

        print_system(str(self._VIDEO_ID), 'offset: ' + str(self.frame_number))
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
            print_system(str(self._VIDEO_ID), 'id progress: ' + str(self.frame_number) +
                         '; video: ' + str(self.video_number))

            if self.flag_record:
                self.out.write(self.frame)

        elif command_key & 0xff == ord('o'):
            self.offset = self.frame_number
            print_system(str(self._VIDEO_ID), 'offset20161208: ' + str(self.offset))

        elif command_key & 0xff == ord('w'):
            self.ret, self.frame = self.cap.read()
            self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                      int(self.frame.shape[0] / self._SHOW_SIZE)))
            self.frame_number += 1
            if self.flag_record:
                self.out.write(self.frame)
            print_system(str(self._VIDEO_ID), 'w progress: ' + str(self.frame_number) +
                         '; video: ' + str(self.video_number))

        elif command_key & 0xff == ord('v'):
            for _ in range(0, 5):
                self.ret, self.frame = self.cap.read()
                self.frame_number += 1
                if self.flag_record:
                    self.out.write(self.frame)
            self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                      int(self.frame.shape[0] / self._SHOW_SIZE)))
            print_system(str(self._VIDEO_ID), 'v progress: ' + str(self.frame_number) +
                         '; video: ' + str(self.video_number))

        elif command_key & 0xff == ord('x'):
            for _ in range(0, 10):
                self.ret, self.frame = self.cap.read()
                self.frame_number += 1
                if self.flag_record:
                    self.out.write(self.frame)
            self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                      int(self.frame.shape[0] / self._SHOW_SIZE)))
            print_system(str(self._VIDEO_ID), 'x progress: ' + str(self.frame_number) +
                         '; video: ' + str(self.video_number))

        elif command_key & 0xff == ord('z'):
            for _ in range(0, 100):
                self.ret, self.frame = self.cap.read()
                self.frame_number += 1
                if self.flag_record:
                    self.out.write(self.frame)
            self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                      int(self.frame.shape[0] / self._SHOW_SIZE)))
            print_system(str(self._VIDEO_ID), 'z progress: ' + str(self.frame_number) +
                         '; video: ' + str(self.video_number))

        elif command_key & 0xff == ord('s'):
            if self.flag_record:
                print_error(str(self._VIDEO_ID), 'cannot start to save new videos. type e and finish recoding video.')
            else:
                self.flag_record = True
                print_system(str(self._VIDEO_ID), 'start saving video')
                self.out = cv2.VideoWriter(self._SAVE_VIDEO_PATH + 'div_' + str(self._VIDEO_ID) + '_' +
                                           self._VIDEO_NAME + '_' + ('%06d' % self.video_number) + self._SAVE_EXTENSION,
                                           self._FOURCC, self._FPS, self._SIZE)
                self.out.write(self.frame)
                self._SAVE_FRAME_NUMBER_FILE.write('>' + str(self.frame_number - self.offset) + '\n')

        elif command_key & 0xff == ord('e'):
            if not self.flag_record:
                print_error(str(self._VIDEO_ID), 'cannot finish saving videos. type s and start to record video')
            else:
                self.flag_record = False
                self.video_number += 1
                print_system(str(self._VIDEO_ID), 'finish recording video.')
                self.out.release()
                self._SAVE_FRAME_NUMBER_FILE.write('<' + str(self.frame_number - self.offset) + '\n')

        elif command_key & 0xff == ord('p'):
            if self.flag_record:
                self.video_number += 1
                print_system(str(self._VIDEO_ID), 'finish recording video.')
                self.out.release()
                self._SAVE_FRAME_NUMBER_FILE.write('<' + str(self.frame_number - self.offset) + '\n')

                self.ret, self.frame = self.cap.read()
                self.frame_show = cv2.resize(self.frame, (int(self.frame.shape[1] / self._SHOW_SIZE),
                                                          int(self.frame.shape[0] / self._SHOW_SIZE)))
                self.frame_number += 1
                print_system(str(self._VIDEO_ID), 'progress: ' + str(self.frame_number))

                print_system(str(self._VIDEO_ID), 'start saving video')
                self.out = cv2.VideoWriter(self._SAVE_VIDEO_PATH + 'div_' + str(self._VIDEO_ID) + '_' +
                                           self._VIDEO_NAME + '_' + ('%06d' % self.video_number) + self._SAVE_EXTENSION,
                                           self._FOURCC, self._FPS, self._SIZE)
                self.out.write(self.frame)
                self._SAVE_FRAME_NUMBER_FILE.write('>' + str(self.frame_number - self.offset) + '\n')
            else:
                print_error(str(self._VIDEO_ID), 'cannot process fin&start new video.')

        return True


#######################################################
DATE = '20161215/'
DIRECTION = 'front/'
NAME = 'fC0005.MP4'
STATE = 'double/'
OFFSET = 500 + (0 * 60 + 20) * 60
#######################################################

FILENAME = 'I:IIGNIS/' + 'data/' + DATE + DIRECTION + NAME
SAVE_VIDEO_PATH = 'dev/divideo/' + DATE + DIRECTION + STATE
SAVE_TEXT_PATH = 'dev/divtext/' + DATE + DIRECTION


if __name__ == '__main__':
    print_system(str(-1), 'have you set the correct initialization? : y')
    key = input('>>> ')

    if key != 'y':
        sys.exit()

    video = Video2(filename=FILENAME, save_video_path=SAVE_VIDEO_PATH, save_text_path=SAVE_TEXT_PATH,
                   offset=OFFSET, video_id=0, show_size=2)

    flag_loop = True

    video.advance_offset()

    while True:
        key = cv2.waitKey(0)

        if key & 0xff == ord('q'):
            print_system(str(-1), 'quit? : y')
            key = cv2.waitKey(0)
            if key & 0xff == ord('y'):
                break
            else:
                print_system(str(-1), 'continue')

        flag_loop = video.control_video(key)
        video.show()
        if not flag_loop:
            break

    video.release_video()
