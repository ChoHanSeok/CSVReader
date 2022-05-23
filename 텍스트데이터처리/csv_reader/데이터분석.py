# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"텍스트데이터분석", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
        
        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"파일명:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.filename = wx.TextCtrl( self, wx.ID_ANY, u"파일명을 입력하시오", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer2.Add( self.filename, 1, wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"분석하기", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
        
        self.resultArea = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,170 ), wx.HSCROLL|wx.TE_MULTILINE )
        bSizer1.Add( self.resultArea, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button3.Bind( wx.EVT_BUTTON, self.analysys )
        self.m_button2.Bind( wx.EVT_BUTTON, self.clear )
    

    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def analysys( self, event ):
        ret=[]
        fn = str(self.filename.GetValue())
        with open(fn,'r') as f:
            data = f.readlines()
            cnt = -1
            colNames = []
            for x in data:
                cnt += 1
                if x[-1] == '\n':
                    x = x[:-1]
                if cnt == 0:
                    colNames = x.split(',')
                else:
                    tempDic = {}
                    tempList = x.split(',')
                    couples = zip(colNames,tempList)
                    print(dict(couples))
                    
                    couples = zip(colNames,tempList)
                    self.resultArea.AppendText(str(dict(couples)))
                    self.resultArea.AppendText('\n')
    
    def clear( self, event ):
        self.resultArea.SetValue('')
        
        
        
if __name__=='__main__':
    ex = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    ex.MainLoop()       
    

