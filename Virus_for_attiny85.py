import os
import webbrowser as hackedWeb
from random import randrange, choice

hackweb = ["https://geekprank.com/hacker/","https://www.youtube.com/watch?v=dQw4w9WgXcQ",
           "https://youtu.be/y3Jc2kxaqdw?si=OHzHH30Em-6yXWQU","https://geekprank.com/jurassic-park/",
           "https://vms.drweb.com/online/?lng=en","https://www.malwarebytes.com/",
           "https://hackprank.com/","https://hackedscreen.com/",
           "https://livethreatmap.radware.com/","https://threatmap.checkpoint.com/",
           "https://www.facebook.com/ellentv/videos/1588579742269085/"]


# os.system('for /l %i in (1,1,3) do start cmd /k echo |-|4ck3r 15 |-|3r3 ( > _ < )/ ')       #17
# os.system('for /l %i in (1,1,4) do start cmd /k echo Hacker is Here (*_*)/')                #20
# for i in range(2):     # 25
#     web = choice(hackweb)
#     os.system("for %i in (1 2 3 4 5) do pause>nul & echo Hacked! ")
#     os.system(f'for /l %i in (1,1,2) do start msedge --new-window {web}')
os.system('for /l %i in (1,1,3) do start cmd /k pause>nul')       #17
os.system(f'for /l %i in (1,1,2) do start msedge --new-window {choice(hackweb)}')

# for i in range(0,randrange(15,20)):
#     os.system('start cmd /k "prompt HACKED~^(^.^)by-anu~ & color 4)"')