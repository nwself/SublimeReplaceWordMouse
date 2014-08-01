# -*- coding: utf-8 -*-


import sublime, sublime_plugin

class ReplaceWordCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sel = self.view.sel()

        paste_r = []
        for region in sel:
            if region.begin() - region.end() == 0:
                paste_r.append(region)
            else:
                copy_r = region

        for region in paste_r:
            if self.view.word(region) != self.view.substr(copy_r):
                self.view.replace(edit, self.view.word(region), self.view.substr(copy_r))


    def is_enabled(self):
        if self.view == None:
            return False
        sel = self.view.sel()

        one_full  = False
        one_empty = False

        for region in sel:
            one_full  = one_full or (region.begin() - region.end() != 0)
            one_empty = one_empty or (region.begin() - region.end() == 0)
            print(region, one_full, one_empty)

        return one_full and one_empty

    def is_visible(self):
        return True

    def description(self):
        return None