#!/usr/bin/env python3

from aws_cdk import core

from rootstream_twitch_streamlink.rootstream_twitch_streamlink_stack import RootstreamTwitchStreamlinkStack


app = core.App()
RootstreamTwitchStreamlinkStack(app, "rootstream-twitch-streamlink")

app.synth()
