#!/bin/sh

v4l2-ctl --set-ctrl power_line_frequency=2
v4l2-ctl --set-ctrl repeat_sequence_header=1
v4l2-ctl --set-ctrl video_bitrate_mode=1
v4l2-ctl --set-ctrl video_bitrate=2000000
v4l2-ctl --set-ctrl h264_i_frame_period=30

/home/pi/work/v4l2rtspserver/v4l2rtspserver -S -W 1280 -H 720 -F 60 -u h264 -A 48000 -C 1 /dev/video0,hw:1,0
