#!/usr/bin/env python
#coding=utf-8

import json
import base64
import time


from roboyun_robot_sample.srv import SAMPLE_CMD
from roboyun_asr.srv import ASR
from roboyun_tts.srv import TTS
from roboyun_afr.srv import AFR
from roboyun_nlu.srv import NLU
from roboyun_chat.srv import CHAT

import rospy

'''
def led():

    rospy.wait_for_service('led')
    try:
        led_s = rospy.ServiceProxy('led',LED)
        res = led_s('')
    except rospy.ServiceException,e:
        print 'led call failed:%s'%e

'''


def tts(content):
    rospy.wait_for_service('tts_online')
    try:
        tts_s = rospy.ServiceProxy('tts_online',TTS)
        res = tts_s(content)
    except rospy.ServiceException,e:
        print 'tts call failed:%s'%e

def afr():

    rospy.wait_for_service('afr_online')
    try:
        afr_s = rospy.ServiceProxy('afr_online',AFR)
        res = afr_s('')
        tts('你是%s'%res.processing_result_json)
    except rospy.ServiceException,e:
        print 'afr call failed:%s'%e
    
def asr():
    
    rospy.wait_for_service('asr_online')
    try:
        asr_s = rospy.ServiceProxy('asr_online',ASR)
        res = asr_s('')
        chat(res.processing_result_json)
    except rospy.ServiceException,e:
        print 'asr call failed:%s'%e

def nlu():
    pass

def chat(content):
    
    rospy.wait_for_service('chat_online')
    try:
        chat_s = rospy.ServiceProxy('chat_online',CHAT)
        res = chat_s(content)
        tts(res.processing_result_json)
    except rospy.ServiceException,e:
        print 'chat call failed:%s'%e


def sample_switch(msg):
    
    if msg == 'afr':
        tts('请将您的脸对准摄像头')
        afr()    
    elif msg == 'chat':
        tts('我们开始聊天吧')
        asr()
    elif msg == 'nlu':
        print msg    
    #elif msg == 'led':
    #    tts('下面进行10秒钟的灯光演示')
    #    led()    


    return msg
    
def handle_sample(req):

    return SAMPLEResponse(sample_switch(req.cmd))

def sample_server():
    rospy.init_node('roboyun_robot_sample')
    s = rospy.Service('robot_sample',SAMPLE_CMD,handle_sample)
    rospy.spin()

if __name__ == '__main__':
    sample_server()
