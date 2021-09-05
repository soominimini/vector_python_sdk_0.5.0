#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Play an animation on Vector
"""

import anki_vector


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        # anim_request = robot.anim.load_animation_list()
        # anim_names = robot.anim.anim_list
        # for anim_name in anim_names:
        #     print(anim_name)
        robot.anim.play_animation('anim_onboarding_reacttoface_happy_01_head_angle_40')



if __name__ == "__main__":
    main()
