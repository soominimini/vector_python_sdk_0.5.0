

import threading

import anki_vector
from anki_vector.events import Events

wake_word_heard = False
cnt =0

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial, requires_behavior_control=False, cache_animation_list=False) as robot:
        evt = []
        for i in range(10):
            evt.append(threading.Event())

        global wake_word_heard
        global cnt

        async def on_wake_word(event_type, event):
            for a in range(10):
                print(evt[a].is_set())
            print("---------------------------------------------------------------------")

            # robot.conn.request_control()
            print("func")
            global wake_word_heard
            global cnt
            if not wake_word_heard:
                wake_word_heard = True
                await robot.conn.request_control(timeout=1.0)
                await robot.say_text("Hello")
                evt[cnt].set()
                cnt+=1



        print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')
        while(True):

            wake_word_heard = False
            try:
                robot.events.subscribe(on_wake_word, Events.wake_word)
                print("cnt"  , cnt)
                if not evt[cnt].wait(timeout=10):
                    print('------ Vector never heard "Hey Vector!" ------')
            except KeyboardInterrupt:
                pass


if __name__ == '__main__':
    main()