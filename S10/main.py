
#init program

import menu
import data
import actions

def init_main():
    current_list=0
    while True:
        action= menu.show_menu()
        if action==1:
            new_users=actions.input_details()
            if current_list==0:
                current_list=new_users
            else:
                for i in range(len(new_users)):
                    current_list.append(new_users[i])
        if action==2:
            actions.see_students(current_list)
        if action==3:
            actions.top_3(current_list)
        if action==4:
            current_list= data.import_list(list)
        if action==5:
            data.export_list(current_list)
        if action==6:
            actions.global_average(current_list)
        if action==7:
            break

init_main()