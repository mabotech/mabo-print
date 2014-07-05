# -*- coding: utf-8 -*-

import os


from mako.template import Template

from time import time, strftime, localtime

import  subprocess

class Gen(object):

    def __init__(self):
        
        pass
        
        
    def _render(self, template_file, rows):
        """
        template file render
        """
        now = strftime('%Y-%m-%d %H:%M:%S', localtime())
        return Template(filename=template_file, input_encoding='utf-8',output_encoding='utf-8').render(rows = rows, now = now)

    def rst_pdf(self, seqno):
        
        
        try:
            
            cmd = "rst2pdf c:/maboss/output/%s.rst -s c:/maboss/chinese.style -o c:/maboss/output/%s.pdf --font-path c:/WinNT/fonts" %(seqno, seqno)
            
            print('rst2pdf')
            
            rtn = subprocess.Popen(cmd, shell=True)
            
            gs = 'c:\\maboss\\Tools\\gs9.04\\bin\\gswin32c'
            
            output = '''\\spool\\Adobe PDF'''
            
            cmd = '''%s  -dPrinted -dBATCH -dNOPAUSE -dNOSAFER -dNOCANCEL -sPAPERSIZE=a4 -dBitsPerPixel=1 -sDEVICE=mswinpr2 -sOutputFile="%s" "c:/maboss/output/%s.pdf"''' %(gs, output, seqno)
            
            #cmd = '''%s -dBitsPerPixel=1 -sDEVICE=display "c:/maboss/output/%s.pdf" ''' %(gs,  seqno)            
            
            print cmd
            
            rtn = subprocess.Popen(cmd, shell=True)            
            
            
        except:
            print('Exception')
            pass
        
        
    def rst_gen(self, seqno,  rows):
        
        template_file = "c:/maboss/temp/rest.mako"       
        
        if rows != None:
        
            routes = self._render(template_file, rows)
            
            fn = "c:/maboss/output/%s.rst" %(seqno)
            
            fh = open(fn, 'w')
            
            fh.write(routes)
            
            fh.close()
            
            self.rst_pdf(seqno)
            
        else:
            raise Exception('error')