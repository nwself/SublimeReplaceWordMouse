# -*- coding: utf-8 -*-


import sublime, sublime_plugin

class ReplaceWordCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sel = self.view.sel()

        copy_r  = sel[1] if (sel[0].begin() - sel[0].end() == 0) else sel[0]
        paste_r = sel[0] if (sel[0].begin() - sel[0].end() == 0) else sel[1]

        paste_r = self.view.word(paste_r)

        self.view.replace(edit, paste_r, self.view.substr(copy_r))

    def is_enabled(self):
        if self.view == None:
            return False
        sel = self.view.sel()
        enabled = len(sel) == 2 and ((sel[0].begin() - sel[0].end()) == 0) != ((sel[1].begin() - sel[1].end()) == 0)
        return enabled

    def is_visible(self):
        return True

    def description(self):
        return None