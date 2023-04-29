import tkinter.messagebox
import customtkinter
import os
import webbrowser
import subprocess

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("my hub")
        self.geometry(f"{1300}x{800}")

        #кнопки скриптовч
        def pipetka_hex():
            os.startfile(r"C:\Users\Admin\Desktop\sv_bogdanov_tools\pipetka_hex.py")
        def pipetka_rgb():
            os.startfile(r"C:\Users\Admin\Desktop\sv_bogdanov_tools\pipetka_rgb.py")
        
        #команды сайтов
        def b_github():
            webbrowser.open("https://github.com/")
        def yandex_mail():
            webbrowser.open("https://mail.yandex.ru/?uid=674902034#inbox")
        def datalens():
            webbrowser.open("https://datalens.yandex.ru/5dy0ijb6sw0mx-byudzhet")
            

        #кнопки папки
        def project_folder():
            subprocess.Popen('explorer "%s"'%(r'C:\Users\Admin\Desktop\Project foler'))

        #кнопки файлов
        def needed():
            subprocess.Popen('explorer "%s"'%(r"C:\Users\Admin\Desktop\Файлы Excel\Нужное.xlsm"))
        def budget():
            subprocess.Popen('explorer "%s"'%(r"C:\Users\Admin\Desktop\Программы\1Статистика\Ананлиз затрат\Бюджет 2.0.xlsm"))
        



        #параметры кнопок
        button_width = 200
        button_height = 25
        button_font = ('Boulder',15,'bold')
        
        # располагаем контейнеры 
        self.grid_columnconfigure(list(range(7)), weight=1)
        self.grid_rowconfigure(list(range(60)), weight=1)

        # заголовки
        self.button_l1 = customtkinter.CTkButton(self, text='Сайты',fg_color='#242424')
        self.button_l1.grid(row=0, column=0, padx=0, pady=0)
        self.button_l1.configure(width=button_width, height=button_height,font=('Boulder',20,'bold'))

        self.button_l2 = customtkinter.CTkButton(self, text='Папки',fg_color='#242424')
        self.button_l2.grid(row=0, column=1, padx=0, pady=0)
        self.button_l2.configure(width=button_width, height=button_height,font=('Boulder',20,'bold'))

        self.button_l3 = customtkinter.CTkButton(self, text='Файлы',fg_color='#242424')
        self.button_l3.grid(row=0, column=2, padx=0, pady=0)
        self.button_l3.configure(width=button_width, height=button_height,font=('Boulder',20,'bold'))

        self.button_l4 = customtkinter.CTkButton(self, text='Скрипты',fg_color='#242424')
        self.button_l4.grid(row=0, column=3, padx=0, pady=0)
        self.button_l4.configure(width=button_width, height=button_height,font=('Boulder',20,'bold'))

        self.button_l4 = customtkinter.CTkButton(self, text='Приложения',fg_color='#242424')
        self.button_l4.grid(row=0, column=4, padx=0, pady=0)
        self.button_l4.configure(width=button_width, height=button_height,font=('Boulder',20,'bold'))

        self.button_l4 = customtkinter.CTkButton(self, text='Сайт бюджета',fg_color='#242424')
        self.button_l4.grid(row=3, column=0, padx=0, pady=0)
        self.button_l4.configure(width=button_width, height=button_height,font=('Boulder',20,'bold'))

        #кнопки сайтов 
        col=0 

        self.b_github = customtkinter.CTkButton(self, command=b_github, text='GitHub')
        self.b_github.grid(row=1, column=col, padx=0, pady=0)
        self.b_github.configure(width=button_width, height=button_height,font=button_font)

        self.yandex_mail = customtkinter.CTkButton(self, command=yandex_mail, text='Почта')
        self.yandex_mail.grid(row=2, column=col, padx=0, pady=0)
        self.yandex_mail.configure(width=button_width, height=button_height,font=button_font)

        self.datalens = customtkinter.CTkButton(self, command=datalens, text='DataLens')
        self.datalens.grid(row=4, column=col, padx=0, pady=0)
        self.datalens.configure(width=button_width, height=button_height,font=button_font)

        #кнопки папок
        col=1
        self.button_2 = customtkinter.CTkButton(self, command=project_folder, text='Папка с проектами')
        self.button_2.grid(row=1, column=col, padx=0, pady=0)
        self.button_2.configure(width=button_width, height=button_height,font=button_font)

        #кнопки файлов
        col=2
        self.needed = customtkinter.CTkButton(self, command=needed, text='Нужное')
        self.needed.grid(row=1, column=col, padx=0, pady=0)
        self.needed.configure(width=button_width, height=button_height,font=button_font)
        self.budget = customtkinter.CTkButton(self, command=budget, text='Бюджет')
        self.budget.grid(row=2, column=col, padx=0, pady=0)
        self.budget.configure(width=button_width, height=button_height,font=button_font)

        #кнопки скриптов
        col=3
        self.pipetka_hex = customtkinter.CTkButton(self, command=pipetka_hex, text='Пипетка (hex)')
        self.pipetka_hex.grid(row=1, column=col, padx=0, pady=0)
        self.pipetka_hex.configure(width=button_width, height=button_height,font=button_font)

        self.pipetka_grb = customtkinter.CTkButton(self, command=pipetka_hex, text='Пипетка (rgb)')
        self.pipetka_grb.grid(row=2, column=col, padx=0, pady=0)
        self.pipetka_grb.configure(width=button_width, height=button_height,font=button_font)

        #кнопки приложений
        col=4
        self.button_4 = customtkinter.CTkButton(self, command='', text='default')
        self.button_4.grid(row=1, column=col, padx=0, pady=0)
        self.button_4.configure(width=button_width, height=button_height,font=button_font)

    
if __name__ == "__main__":
    app = App()
    app.mainloop()