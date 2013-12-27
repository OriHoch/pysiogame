# -*- coding: utf-8 -*-
import sys
import threading
import os
import subprocess
import signal

class Speaker(threading.Thread):
    def __init__(self, lang, configo):
        threading.Thread.__init__(self)
        self.lang = lang
        self.enabled = True
        self.started = False
        
        self.started_en = False
        self.process = None
        self.process_en = None
        self.spk = None
        self.talkative = False
        #self.start_server()
        if sys.version_info < (3, 0):
            self.needs_encode = False
        else:
            self.needs_encode = True
        
    def start_server(self):
        if self.enabled and self.lang.voice != None:
            #prior to lang
            #voices = ["-s 190 -a 100 -p 75 -ven+m1 ", "-s 170 -a 100 -p 80 -ven+m2 ","-s 175 -a 100 -p 80 -ven+m3 ","-s 190 -a 100 -p 60 -ven+f1 ","-s 170 -a 100 -p 75 -ven+f2 ","-s 170 -a 100 -p 80 -ven+m2 "]
            #attr = voices[4]
            #attr = self.lang.voice
            cmd = ['espeak']
            cmd.extend(self.lang.voice)
            try:
                self.process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.started = True
                #self.contactable = True
                self.spk = self.process
            except:
                self.enabled = False
                self.started = False
                print("pySioGame: You may like to install espeak to get some extra functionality, however this is not required to successfully use the game.")
            #stdout and stderr only used to hide the messages from terminal
        else:
            self.process = None
            
    def start_server_en(self):
        if self.enabled:
            cmd = ['espeak']
            cmd.extend(["-ven+m1"])
            try:
                self.process_en = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.started_en = True
            except:
                self.started_en = False
            
    def switch_spk(self, spk):
        if spk == 1:
            self.spk = self.process
        elif spk == 2:
            self.spk = self.process_en
            
    def restart_server(self):
        if self.started:
            self.stop_server()
        self.start_server()
        
    def run(self):
        pass
        
    def stop_server(self):
        if self.enabled and self.started and self.process != None:
            self.process.stdin.close()
            self.process.stdout.close()
            self.process.stderr.close()
            try:
                os.kill(self.process.pid, signal.SIGTERM)
            except OSError:
                print("Error killing the espeak process")
                
    def stop_server_en(self):
        if self.enabled and self.started_en and self.process_en != None:
            self.process_en.stdin.close()
            self.process_en.stdout.close()
            self.process_en.stderr.close()
            try:
                os.kill(self.process_en.pid, signal.SIGTERM)
            except OSError:
                print("Error killing the espeak process")
                
    def say(self,text,voice=1):
        if self.enabled and self.talkative and (self.lang.voice != None or self.spk == self.process_en):
            if self.spk == self.process:
                text = self.check_letter_name(text)
            text = text + "\n"
            #if self.needs_encode:
            try:
                text = text.encode("utf-8")
            except:
                pass
                
            try:
                #print(text)
                self.spk.stdin.write(text)
                #self.process.stdin.write(text.encode())
                self.spk.stdin.flush()
            except:
                pass
            
    def check_letter_name(self,text):
        if sys.version_info < (3, 0):
            try:
                val = unicode(text, "utf-8")
            except:
                val = text
                
            if len(val) == 1 and len(self.lang.letter_names)>0:
                t = val.lower()
                for i in range(len(self.lang.alphabet_lc)):
                    if t == unicode(self.lang.alphabet_lc[i],"utf-8"):
                        text = self.lang.letter_names[i]
                        break
        else:
            if len(text) == 1 and len(self.lang.letter_names)>0:
                t = text.lower()
                for i in range(len(self.lang.alphabet_lc)):
                    if t == self.lang.alphabet_lc[i]:
                        text = self.lang.letter_names[i]
                        break
        return text
        