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
        
        self.talkative = configo.settings[1]
        self.start_server()
        if sys.version_info < (3, 0):
            self.needs_encode = False
        else:
            self.needs_encode = True
        
    def start_server(self):
        if self.enabled:
            #prior to lang
            #voices = ["-s 190 -a 100 -p 75 -ven+m1 ", "-s 170 -a 100 -p 80 -ven+m2 ","-s 175 -a 100 -p 80 -ven+m3 ","-s 190 -a 100 -p 60 -ven+f1 ","-s 170 -a 100 -p 75 -ven+f2 ","-s 170 -a 100 -p 80 -ven+m2 "]
            #attr = voices[4]
            #attr = self.lang.voice
            cmd = ['espeak']
            cmd.extend(self.lang.voice)
            try:
                self.process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                self.enabled = False
                print("Failed to connect with espeak")
            #stdout and stderr only used to hide the messages from terminal
    
    def restart_server(self):
        self.stop_server()
        self.start_server()
        
    def run(self):
        pass
        
    def stop_server(self):
        if self.enabled:
            self.process.stdin.close()
            self.process.stdout.close()
            self.process.stderr.close()
            try:
                os.kill(self.process.pid, signal.SIGTERM)
            except OSError:
                print("Error killing the espeak process")
        
    def say(self,text,voice=1):
        if self.enabled and self.talkative:
            text = self.check_letter_name(text)
            text = text + "\n"
            if self.needs_encode:
                text = text.encode("utf-8")
            try:
                self.process.stdin.write(text)
                #self.process.stdin.write(text.encode())
                self.process.stdin.flush()
            except:
                pass
        else:
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
        