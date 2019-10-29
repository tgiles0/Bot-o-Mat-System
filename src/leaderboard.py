import tkinter as tk
from src.vertical_scrollable_frame import VSF

leaderboard_w = 400
leaderboard_h = 500


def show_leaderboard(robot_list):
    """ Displays the leaderboard for the robots which have been created """
    print('Opening the Bot-o-Mat leaderboard. This will open in a separate window.')
    print('When you are done viewing the Bot-o-Mat leaderboard close the window '
          'to continue interacting with the Bot-o-Mat System.')
    robot_index = 0
    score_index = 1
    robot_ldrs = []
    for robot in robot_list:
        rbt_tuple = (robot, robot.get_robot_score())
        robot_ldrs.append(rbt_tuple)
    """ Sort the robot leaders from largest to smallest """
    robot_ldrs = sorted(robot_ldrs, key=lambda x: x[1], reverse=True)

    window = tk.Tk()
    title_txt = 'Bot-O-Mat Leaderboard'
    window.title(title_txt)

    data_row = 0
    plc_col = 0
    name_col = 1
    type_col = 2
    time_col = 3

    frame = VSF(window, leaderboard_w, leaderboard_h)
    plc_lbl = tk.Label(frame.scrollable_frame, text='Place', borderwidth=2)
    plc_lbl.grid(row=data_row, column=plc_col)
    name_lbl = tk.Label(frame.scrollable_frame, text='Robot Name', borderwidth=2)
    name_lbl.grid(row=data_row, column=name_col)
    type_lbl = tk.Label(frame.scrollable_frame, text='Robot Type', borderwidth=2)
    type_lbl.grid(row=data_row, column=type_col)
    time_lbl = tk.Label(frame.scrollable_frame, text='Time worked on Chores', borderwidth=2)
    time_lbl.grid(row=data_row, column=time_col)

    robot_num = 1
    for robot_pair in robot_ldrs:
        robot_id = robot_pair[robot_index]
        robot_score = robot_pair[score_index]
        lbl_1 = tk.Label(frame.scrollable_frame, text=robot_num, borderwidth=2)
        lbl_1.grid(row=robot_num, column=plc_col)

        lbl_2 = tk.Label(frame.scrollable_frame, text=robot_id.get_name(), borderwidth=2)
        lbl_2.grid(row=robot_num, column=name_col)

        lbl_3 = tk.Label(frame.scrollable_frame, text=robot_id.get_type(), borderwidth=2)
        lbl_3.grid(row=robot_num, column=type_col)

        lbl_4 = tk.Label(frame.scrollable_frame, text=str(robot_score) + ' seconds', borderwidth=2)
        lbl_4.grid(row=robot_num, column=time_col)
        robot_num += 1

    frame.pack(expand=True, fill='both')
    window.mainloop()
