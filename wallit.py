import sublime, sublime_plugin

class WallCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        comment = "\n/*\n" \
                  "TTTTTTTTTTTTTTTTTTTTTTT     RRRRRRRRRRRRRRRRR        UUUUUUUU     UUUUUUUU     MMMMMMMM               MMMMMMMM     PPPPPPPPPPPPPPPPP   \n" \
                  "T:::::::::::::::::::::T     R::::::::::::::::R       U::::::U     U::::::U     M:::::::M             M:::::::M     P::::::::::::::::P  \n" \
                  "T:::::::::::::::::::::T     R::::::RRRRRR:::::R      U::::::U     U::::::U     M::::::::M           M::::::::M     P::::::PPPPPP:::::P \n" \
                  "T:::::TT:::::::TT:::::T     RR:::::R     R:::::R     UU:::::U     U:::::UU     M:::::::::M         M:::::::::M     PP:::::P     P:::::P\n" \
                  "TTTTTT  T:::::T  TTTTTT       R::::R     R:::::R      U:::::U     U:::::U      M::::::::::M       M::::::::::M       P::::P     P:::::P\n" \
                  "        T:::::T               R::::R     R:::::R      U:::::D     D:::::U      M:::::::::::M     M:::::::::::M       P::::P     P:::::P\n" \
                  "        T:::::T               R::::RRRRRR:::::R       U:::::D     D:::::U      M:::::::M::::M   M::::M:::::::M       P::::PPPPPP:::::P \n" \
                  "        T:::::T               R:::::::::::::RR        U:::::D     D:::::U      M::::::M M::::M M::::M M::::::M       P:::::::::::::PP  \n" \
                  "        T:::::T               R::::RRRRRR:::::R       U:::::D     D:::::U      M::::::M  M::::M::::M  M::::::M       P::::PPPPPPPPP    \n" \
                  "        T:::::T               R::::R     R:::::R      U:::::D     D:::::U      M::::::M   M:::::::M   M::::::M       P::::P            \n" \
                  "        T:::::T               R::::R     R:::::R      U:::::D     D:::::U      M::::::M    M:::::M    M::::::M       P::::P            \n" \
                  "        T:::::T               R::::R     R:::::R      U::::::U   U::::::U      M::::::M     MMMMM     M::::::M       P::::P            \n" \
                  "      TT:::::::TT           RR:::::R     R:::::R      U:::::::UUU:::::::U      M::::::M               M::::::M     PP::::::PP          \n" \
                  "      T:::::::::T           R::::::R     R:::::R       UU:::::::::::::UU       M::::::M               M::::::M     P::::::::P          \n" \
                  "      T:::::::::T           R::::::R     R:::::R         UU:::::::::UU         M::::::M               M::::::M     P::::::::P          \n" \
                  "      TTTTTTTTTTT           RRRRRRRR     RRRRRRR           UUUUUUUUU           MMMMMMMM               MMMMMMMM     PPPPPPPPPP          \n" \
                  "*/\n"
        view = self.view
        for region in self.view.sel():
            if not region.empty():
                syntax = view.settings().get('syntax')
                if str(syntax).lower() == "python":
                    comment = "\n\"\"\"\n" \
                              "TTTTTTTTTTTTTTTTTTTTTTT     RRRRRRRRRRRRRRRRR        UUUUUUUU     UUUUUUUU     MMMMMMMM               MMMMMMMM     PPPPPPPPPPPPPPPPP   \n" \
                              "T:::::::::::::::::::::T     R::::::::::::::::R       U::::::U     U::::::U     M:::::::M             M:::::::M     P::::::::::::::::P  \n" \
                              "T:::::::::::::::::::::T     R::::::RRRRRR:::::R      U::::::U     U::::::U     M::::::::M           M::::::::M     P::::::PPPPPP:::::P \n" \
                              "T:::::TT:::::::TT:::::T     RR:::::R     R:::::R     UU:::::U     U:::::UU     M:::::::::M         M:::::::::M     PP:::::P     P:::::P\n" \
                              "TTTTTT  T:::::T  TTTTTT       R::::R     R:::::R      U:::::U     U:::::U      M::::::::::M       M::::::::::M       P::::P     P:::::P\n" \
                              "        T:::::T               R::::R     R:::::R      U:::::D     D:::::U      M:::::::::::M     M:::::::::::M       P::::P     P:::::P\n" \
                              "        T:::::T               R::::RRRRRR:::::R       U:::::D     D:::::U      M:::::::M::::M   M::::M:::::::M       P::::PPPPPP:::::P \n" \
                              "        T:::::T               R:::::::::::::RR        U:::::D     D:::::U      M::::::M M::::M M::::M M::::::M       P:::::::::::::PP  \n" \
                              "        T:::::T               R::::RRRRRR:::::R       U:::::D     D:::::U      M::::::M  M::::M::::M  M::::::M       P::::PPPPPPPPP    \n" \
                              "        T:::::T               R::::R     R:::::R      U:::::D     D:::::U      M::::::M   M:::::::M   M::::::M       P::::P            \n" \
                              "        T:::::T               R::::R     R:::::R      U:::::D     D:::::U      M::::::M    M:::::M    M::::::M       P::::P            \n" \
                              "        T:::::T               R::::R     R:::::R      U::::::U   U::::::U      M::::::M     MMMMM     M::::::M       P::::P            \n" \
                              "      TT:::::::TT           RR:::::R     R:::::R      U:::::::UUU:::::::U      M::::::M               M::::::M     PP::::::PP          \n" \
                              "      T:::::::::T           R::::::R     R:::::R       UU:::::::::::::UU       M::::::M               M::::::M     P::::::::P          \n" \
                              "      T:::::::::T           R::::::R     R:::::R         UU:::::::::UU         M::::::M               M::::::M     P::::::::P          \n" \
                              "      TTTTTTTTTTT           RRRRRRRR     RRRRRRR           UUUUUUUUU           MMMMMMMM               MMMMMMMM     PPPPPPPPPP          \n" \
                              "\"\"\n"
                view.insert(edit, region.begin(), comment)
                view.insert(edit, len(comment)+region.end(), comment)
