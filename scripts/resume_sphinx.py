#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Follow me, 音声認識

import rospy
from std_msgs.msg import String, Bool
import os
from pocketsphinx import LiveSpeech, get_model_path

class Recognition:
    def recognition(self):
        while 1:
	    if self.speech_recognition == True:
		self.resume()
		self.speech_recognition = False
	    elif self.speech_recognition == False:
		self.pause()
		while self.speech_recognition != True:
		    pass

	# 音声認識
    def resume(self):
	print('== START RECOGNITION ==')
	speech = LiveSpeech(
	    verbose=False, sampling_rate=8000, buffer_size=2048, no_search=False, full_utt=False,
	    hmm=os.path.join(self.model_path, 'en-us'),
	    lm=False,
	    dic=os.path.join(self.dictionary_path, 'take_sphinx.dict'),
	    jsgf=(os.path.join(self.dictionary_path, "take_sphinx.gram"))
	)
	for text in speech:
	    score = text.confidence()
	    if score > 0.1:
		text = str(text)
		self.pub.publish(text) # 音声認識の結果をpublish
		break
	    else:
		print("**noise**")

# 音声認識ストップ
    def pause(self):
	print('== STOP RECOGNITION ==')
	speech = LiveSpeech(no_search=True)

	# 音声認識再開のメッセージを受け取る
    def control(self, data):
	self.speech_recognition = data.data
        
    def __init__(self):
	rospy.init_node('follow_me_nlp_recognition', anonymous=True)
	self.model_path = get_model_path() # 音響モデルのディレクトリの絶対パス
	self.dictionary_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dictionary') # 辞書のディレクトリの絶対パス
	rospy.Subscriber('txt_start', Bool, self.control)
	self.pub = rospy.Publisher('recognition_txt', String, queue_size=10)
	self.speech_recognition = False # ノードを立ち上げた時から音声認識が始まる # 最初は音声認識を停止する場合はFalse
	self.recognition()
        
if __name__ == '__main__':
    Recognition()
