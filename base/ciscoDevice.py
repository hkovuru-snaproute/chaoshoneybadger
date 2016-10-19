#!/usr/bin/python
import unittest
import paramiko
import time 
import sys 
import logging

logging.basicConfig( stream=sys.stderr )
log = logging.getLogger( " Monkey.TestCisco" )                                                              
log.setLevel( logging.DEBUG )

class CiscoSwitch(object):
    """Test case testing link failures while BGP is running"""

    def __init__ (self, ip, username, passwd):
        self.ip = ip
        self.username = username
        self.passwd = passwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
    def connect (self) :
        self.ssh.connect(self.ip, username=self.username, password=self.passwd)
     
    def executeCommand(self, cmd):
        """Execute command """
        inpt, outpt, err = self.ssh.exec_command('show interface brief') 
        inpt, outpt, err = self.ssh.exec_command(cmd)
        for line in outpt.readlines():
            print line
