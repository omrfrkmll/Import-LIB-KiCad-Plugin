###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.adv

###########################################################################
## Class impartGUI
###########################################################################


class impartGUI(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title="impartGUI",
            pos=wx.DefaultPosition,
            size=wx.Size(1200, 700),
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.BORDER_DEFAULT,
        )

        self.SetSizeHints(wx.Size(500, 500), wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        dialogSizer = wx.BoxSizer(wx.VERTICAL)

        # ----------------- Splitter Window (Resizable Panels) -----------------
        self.splitter = wx.SplitterWindow(
            self,
            style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH | wx.SP_NO_XP_THEME,
        )
        self.splitter.SetMinimumPaneSize(350)

        # ----------------- Left Panel (Main / Import) -----------------
        self.leftPanel = wx.Panel(self.splitter)
        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_button = wx.Button(self.leftPanel, wx.ID_ANY, "Start", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer.Add(self.m_button, 0, wx.ALL | wx.EXPAND, 5)

        self.m_text = wx.TextCtrl(
            self.leftPanel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_BESTWRAP | wx.TE_MULTILINE,
        )
        bSizer.Add(self.m_text, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticline11 = wx.StaticLine(
            self.leftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL
        )
        self.m_staticline11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_staticline11.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))
        self.m_staticline11.Hide()

        bSizer.Add(self.m_staticline11, 0, wx.EXPAND | wx.ALL, 5)

        fgSizer2 = wx.FlexGridSizer(0, 4, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        fgSizer2.AddGrowableCol(1)

        self.m_staticTextLCSC = wx.StaticText(
            self.leftPanel, wx.ID_ANY, "EasyEDA / LCSC Part#", wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer2.Add(self.m_staticTextLCSC, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl2 = wx.TextCtrl(
            self.leftPanel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_PROCESS_ENTER,
        )
        self.m_textCtrl2.SetMinSize(wx.Size(120, -1))
        fgSizer2.Add(self.m_textCtrl2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_buttonImportManual = wx.Button(
            self.leftPanel, wx.ID_ANY, "Import", wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer2.Add(self.m_buttonImportManual, 0, wx.ALL, 5)

        self.m_buttonToggleSearch = wx.Button(
            self.leftPanel, wx.ID_ANY, "🔍 Search ▶", wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer2.Add(self.m_buttonToggleSearch, 0, wx.ALL, 5)

        bSizer.Add(fgSizer2, 0, wx.EXPAND | wx.ALL, 0)

        self.m_staticline12 = wx.StaticLine(
            self.leftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL
        )
        self.m_staticline12.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_staticline12.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))

        bSizer.Add(self.m_staticline12, 0, wx.EXPAND | wx.ALL, 5)

        # Use WrapSizer for responsive auto-wrapping checkboxes
        fgSizer1 = wx.WrapSizer(wx.HORIZONTAL)

        self.m_autoImport = wx.CheckBox(
            self.leftPanel, wx.ID_ANY, "auto import", wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer1.Add(self.m_autoImport, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 4)

        self.m_check_autoLib = wx.CheckBox(
            self.leftPanel, wx.ID_ANY, "auto settings", wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer1.Add(self.m_check_autoLib, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 4)

        self.m_overwrite = wx.CheckBox(
            self.leftPanel, wx.ID_ANY, "overwrite lib", wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer1.Add(self.m_overwrite, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 4)

        self.m_checkBoxCompressModels = wx.CheckBox(
            self.leftPanel, wx.ID_ANY, "zip 3D", wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer1.Add(self.m_checkBoxCompressModels, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 4)

        # Single lib checkbox and text field grouped together so they wrap as a single unit
        single_lib_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.m_checkBoxSingleLib = wx.CheckBox(
            self.leftPanel, wx.ID_ANY, "single lib name", wx.DefaultPosition, wx.DefaultSize, 0
        )
        single_lib_sizer.Add(self.m_checkBoxSingleLib, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 4)

        self.m_textCtrl_libname = wx.TextCtrl(
            self.leftPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_textCtrl_libname.SetMinSize(wx.Size(130, -1))
        self.m_textCtrl_libname.SetHint("e.g. MyLibrary")
        self.m_textCtrl_libname.Show(False)
        single_lib_sizer.Add(self.m_textCtrl_libname, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 2)

        fgSizer1.Add(single_lib_sizer, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 4)

        bSizer.Add(fgSizer1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 4)

        self.m_staticText_sourcepath = wx.StaticText(
            self.leftPanel,
            wx.ID_ANY,
            "Folder of the library to import:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText_sourcepath.Wrap(-1)

        bSizer.Add(self.m_staticText_sourcepath, 0, wx.ALL, 5)

        self.m_dirPicker_sourcepath = wx.DirPickerCtrl(
            self.leftPanel,
            wx.ID_ANY,
            ".",
            "Select a folder",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.DIRP_DEFAULT_STYLE,
        )
        bSizer.Add(self.m_dirPicker_sourcepath, 0, wx.ALL | wx.EXPAND, 5)

        bSizer2 = wx.WrapSizer(wx.HORIZONTAL)

        self.m_staticText_librarypath = wx.StaticText(
            self.leftPanel,
            wx.ID_ANY,
            "Library save location:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText_librarypath.Wrap(-1)

        bSizer2.Add(self.m_staticText_librarypath, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_checkBoxLocalLib = wx.CheckBox(
            self.leftPanel,
            wx.ID_ANY,
            "Save local, in the project folder",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizer2.Add(self.m_checkBoxLocalLib, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer.Add(bSizer2, 0, wx.EXPAND, 0)

        self.m_dirPicker_librarypath = wx.DirPickerCtrl(
            self.leftPanel,
            wx.ID_ANY,
            ".",
            "Select a folder",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.DIRP_DEFAULT_STYLE,
        )
        bSizer.Add(self.m_dirPicker_librarypath, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(
            self.leftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL
        )
        self.m_staticline1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_staticline1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))
        self.m_staticline1.Hide()

        bSizer.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_hyperlink = wx.adv.HyperlinkCtrl(
            self.leftPanel,
            wx.ID_ANY,
            "github.com/Steffen-W/Import-LIB-KiCad-Plugin",
            "https://github.com/Steffen-W/Import-LIB-KiCad-Plugin",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.adv.HL_DEFAULT_STYLE,
        )
        bSizer.Add(self.m_hyperlink, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.leftPanel.SetSizer(bSizer)

        # ----------------- Right Panel (Component Search) -----------------
        self.rightPanel = wx.Panel(self.splitter)
        self.rightSizer = wx.BoxSizer(wx.VERTICAL)
        self.rightPanel.SetSizer(self.rightSizer)

        # Split left and right panels with a draggable sash (default position at 520px)
        self.splitter.SplitVertically(self.leftPanel, self.rightPanel, sashPosition=520)

        dialogSizer.Add(self.splitter, 1, wx.EXPAND | wx.ALL, 4)
        self.SetSizer(dialogSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.m_button.Bind(wx.EVT_BUTTON, self.BottonClick)
        self.m_buttonImportManual.Bind(wx.EVT_BUTTON, self.ButtomManualImport)
        self.m_textCtrl2.Bind(wx.EVT_TEXT_ENTER, self.ButtomManualImport)
        self.m_buttonToggleSearch.Bind(wx.EVT_BUTTON, self.OnToggleSearchPanel)
        self.m_dirPicker_sourcepath.Bind(wx.EVT_DIRPICKER_CHANGED, self.DirChange)
        self.m_checkBoxLocalLib.Bind(wx.EVT_CHECKBOX, self.m_checkBoxLocalLibOnCheckBox)
        self.m_checkBoxSingleLib.Bind(wx.EVT_CHECKBOX, self.m_checkBoxSingleLibOnCheckBox)
        self.m_dirPicker_librarypath.Bind(wx.EVT_DIRPICKER_CHANGED, self.DirChange)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_close(self, event):
        event.Skip()

    def BottonClick(self, event):
        event.Skip()

    def ButtomManualImport(self, event):
        event.Skip()

    def OnToggleSearchPanel(self, event):
        event.Skip()

    def DirChange(self, event):
        event.Skip()

    def m_checkBoxLocalLibOnCheckBox(self, event):
        event.Skip()

    def m_checkBoxSingleLibOnCheckBox(self, event):
        event.Skip()
