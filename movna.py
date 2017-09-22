import time
import os
i = 1
while i < 9:
    j = 0
    while j < i:
        j += 1
        print"     "
    i += 1
    print"  王裕民  " 
    print"  #  #  #                         #     #                          " 
    print"  # ### #                          #   #                 #         " 
    print"  # # # #                           # #                            " 
    print"  # # # #   ###   # ##   ####       ###    #   #  ####   #  # ##   " 
    print"  ### ###  #   #  ##  #  #  #        #     #   #  # # #  #  ##  #  " 
    print"  ### ###      #  #   #  ###         #     #   #  # # #  #  #   #  " 
    print"   #   #    ####  #   #  #           #     #   #  # # #  #  #   #  " 
    print"   #   #   #   #  #   #  ####        #     #  ##  # # #  #  #   #  " 
    print"   #   #    ####  #   #  #   #       #      ## #  # # #  #  #   #  " 
    print"                          ###                                      " 
    time.sleep(0.5)
    os.system("cls")