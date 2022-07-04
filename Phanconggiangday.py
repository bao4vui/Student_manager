import PySimpleGUI as sg
from Quanlyhocsinh import mydb

mycursor = mydb.cursor()
strat_headings = ['Môn','Giáo_viên_giảng dạy','Lớp_được_dạy']

mycursor.execute('select * from phanconggiangday')
strat =  mycursor.fetchall()
strat_list = []
for i in strat:
    strat_list.append(list(i))
    
strat_lo = [[sg.Text('\tPhân công giảng dạy',justification='center',font = 'Calibra 20')],
              [sg.Table(strat_list,
                        strat_headings,
                        background_color='LightBlue4',justification='center',
                        text_color='white',change_submits=True,
                        enable_click_events=True,
                        k='-STRATTABLE-'),sg.Column([[sg.Button('Nhập',key='-INSERT5-',expand_x=True)],[sg.Button('Sửa',expand_x=True,key='-FIX5-',disabled=True)],[sg.Button('Tìm kiếm',key='-FIND5-')],[sg.Button('Xóa',expand_x=True,disabled=True,key= '-DEL5-')]])],
              [sg.Input(key = '-INFOR5-')],
              [sg.Exit(visible=False,k='-EXIT6-')]]    

def Sửa(window,values,row,column):
    strat_list[row-1][column-1] = values['-INFOR5-']
    sg.popup('Chỉnh sửa thông tin thành công!')
    window['-STRATTABLE-'].update(strat_list)
    mycursor.execute(("update phanconggiangday set {} = %s where Họ_và_tên = %s".format(strat_headings[column-1])),(values['-INFOR5-'],strat_list[row-1][1]))   
    mydb.commit()
    window['-FIX5-'].update(disabled=True)