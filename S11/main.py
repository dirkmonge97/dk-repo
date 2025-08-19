
import menu
import actions
import data

def init_main():
    current_list=[]
    while True:
        action= menu.show_menu()
        if action==1:
            new_users=actions.input_details()
            current_list.extend(new_users)
        if action==2:
            actions.show_student(current_list)
        if action==3:
            actions.top_3(current_list)
        if action==4:
            current_list= data.import_list()
        if action==5:
            data.export_list(current_list)
        if action==6:
            actions.global_average(current_list)
        if action==7:
            break

init_main()