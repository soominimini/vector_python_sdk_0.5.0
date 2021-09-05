
import threading

import anki_vector
from anki_vector.events import Events
from anki_vector import util
from anki_vector import behavior
from anki_vector.util import *
from anki_vector.behavior import *
from anki_vector import connection

import asyncio

wake_word_heard = False
wake_word_heard2 = False
wake_word_heard3 = False


def first():
    with anki_vector.Robot(requires_behavior_control=False, cache_animation_list=False) as robot:
        evt = threading.Event()

        async def first_wake(event_type, event):
            await robot.conn.request_control()

            global wake_word_heard
            if not wake_word_heard:
                print(robot.conn.requires_behavior_control)
                wake_word_heard = True
                await robot.say_text("hi i'm vector")
                await robot.anim.play_animation('anim_eyepose_happy')
                # await asyncio.wrap_future(robot.anim.play_animation('anim_onboarding_reacttoface_happy_01_head_angle_40'))
                await robot.say_text("nice to meet you!")
                evt.set()


        robot.events.subscribe(first_wake, Events.wake_word)

        print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')

        try:
            if not evt.wait(timeout=30):
                print('------ Vector never heard "Hey Vector!" ------')
        except:
            pass
        robot.conn.release_control()
        second()


def second():
    with anki_vector.Robot(requires_behavior_control=False, cache_animation_list=False) as robot2:
        evt2 = threading.Event()

        async def second_wake(event_type, event):
            await robot2.conn.request_control()
            print("//")
            global wake_word_heard2
            if not wake_word_heard2:
                wake_word_heard2 = True
                await robot2.say_text("of course! i will try!")
                await robot2.behavior.turn_in_place(degrees(90))  # or this can be placed with remote control
                await robot2.behavior.drive_straight(distance_mm(200), speed_mmps(100)) # arrive on the spot
                evt2.set()

        robot2.events.subscribe(second_wake, anki_vector.events.Events.wake_word)


        print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')

        try:
            if not evt2.wait(timeout=30):
                print('------ Vector never heard "Hey Vector!" ------')
        except:
            pass
        robot2.conn.release_control()
        third()

def third():
    with anki_vector.Robot(requires_behavior_control=False, cache_animation_list=False) as robot3:
        evt3 = threading.Event()

        async def test2(event_type, event):
            await robot3.conn.request_control()
            print("//")
            global wake_word_heard3
            if not wake_word_heard3:
                wake_word_heard3 = True
                await robot3.behavior.turn_in_place(degrees(-90))
                await robot3.behavior.set_head_angle(MAX_HEAD_ANGLE)
                await robot3.anim.play_animation('anim_eyepose_sad_instronspect')
                await robot3.say_text("it seems scary..")
                evt3.set()

        robot3.events.subscribe(test2, anki_vector.events.Events.wake_word)


        print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')

        try:
            if not evt3.wait(timeout=30):
                print('------ Vector never heard "Hey Vector!" ------')
        except:
            pass
        robot3.conn.release_control()


if __name__ == '__main__':
    first()