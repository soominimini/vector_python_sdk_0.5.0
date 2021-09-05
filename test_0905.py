
import functools
import threading
import time

import anki_vector
from anki_vector.events import Events
from anki_vector import util

wake_word_heard = False
wake_word_heardw = False


def main():
    evt = threading.Event()

    def on_wake_word(robot, event_type, event):
        robot.conn.request_control()
        print("//1")
        global wake_word_heard
        if not wake_word_heard:
            wake_word_heard = True
            robot.say_text("hi! i am vector")
            evt.set()

    def ff(robot, event_type, event):
        robot.conn.request_control()
        print("//2")
        global wake_word_heardw
        if not wake_word_heardw:
            wake_word_heardw = True
            robot.say_text("Hello")
            aa.set()

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial, requires_behavior_control=False, cache_animation_list=False) as robot:
        on_wake_word = functools.partial(on_wake_word, robot)
        robot.events.subscribe(on_wake_word, Events.wake_word)

        print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')
        print(evt.is_set())
        try:
            if not evt.wait(timeout=10):
                print('------ Vector never heard "Hey Vector!" ------')
        except KeyboardInterrupt:
            pass
        print(evt.is_set())
        aa = threading.Event()
        with anki_vector.Robot(args.serial, requires_behavior_control=False, cache_animation_list=False) as robot2:
            ff = functools.partial(ff, robot2)
            robot2.events.subscribe(ff, Events.wake_word)
            print("ffff")
            print(aa.is_set())
            try:
                if aa.is_set()==False:
                    aa.wait(timeout=10)
                    print('------ Vector never heard "Hey Vector!" ------')
                else:
                    print(aa.is_set())
            except KeyboardInterrupt:
                pass
            print(aa.is_set())


if __name__ == '__main__':
    main()