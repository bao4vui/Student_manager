import PySimpleGUI as sg
from Quanlyhocsinh import mydb

mycursor4 = mydb.cursor()
study_list = []
attitude_list = []
title = ''
layout = [[sg.Button('Xếp loại học tập',k='-STUDY-',use_ttk_buttons=True),
           sg.Button('Xếp loại hạnh kiểm',k='-ATTITUDE-',use_ttk_buttons=True),
           sg.Button('Khen thưởng,kỷ luật',k='-REWARD-',use_ttk_buttons=True)]]

study_heading = ['Lớp','Tốt','Tốt_%','Khá','Khá_%','Yếu','Yếu_%','Kém','Kém_%','Ghi chú']
attitude_heading = ['Lớp','Tốt','Tốt_%','Khá','Khá_%','Yếu','Yếu_%','Kém','Kém_%','Ghi chú']
report_lo = [[sg.Frame('Các tác vụ',layout)],
             [sg.Text('',font = 'Calibra 20',k='-TITLE-')],
             [sg.Table(study_list,study_heading,
                       
                       background_color='LightBlue4',
                        text_color='white',change_submits=True,visible=False,k='-STUDYTB-')],
             [sg.Exit(k='-EXIT5-',visible=False)]
             ]

def Thống_kê_xếp_loại_học_tập(window):
    study_list.clear()
    mycursor4.execute('select * from xeploaihocluc')
    study = mycursor4.fetchall()
    for i in study:
        study_list.append(list(i))
    window['-TITLE-'].update('\tXếp loại học tập')    
    window['-STUDYTB-'].update(study_list,visible=True)    
    
def Thống_kê_xếp_loại_hạnh_kiểm(window):
    attitude_list.clear()
    mycursor4.execute('select * from xeploaihanhkiem')
    attitude = mycursor4.fetchall()
    for i in attitude:
        attitude_list.append(list(i))
    window['-TITLE-'].update('\tXếp loại hạnh kiểm')
    window['-STUDYTB-'].update(attitude_list,visible=True)    
    
    
    