from PySide6.QtWidgets import QMainWindow,QMessageBox
from app.modules.moduleLogin.viewModel.loginViewModel import LoginViewModel
import app.modules.moduleLogin.enums.loginResponse as LoginResponse
from app.modules.moduleLogin.view.loginUI import Ui_MainWindow

import app.res.values.strings as Strings

class Login(QMainWindow,Ui_MainWindow):

    def __init__(self,viewModel:LoginViewModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.viewModel = viewModel
        self.__setup_view_model()
        self.__setup_buttons()
        self.__setup_edit_lines()
        self.show()

    def __setup_buttons(self):
        self.btn_login.clicked.connect(self.viewModel.login)

    def __setup_edit_lines(self):
        self.ld_username.textChanged.connect(lambda value: self.__update_username(value))
        self.ld_password.textChanged.connect(lambda value: self.__update_password(value))

    def login_response(self):
        message = QMessageBox(self)

        if self.viewModel.login_response == LoginResponse.user_empty:
            message.setWindowTitle(Strings.error_title_mb)
            message.setText(Strings.error_text_box_empty)
        elif self.viewModel.login_response == LoginResponse.unknow_response:
            message.setWindowTitle(Strings.error_title_mb)
            message.setText(Strings.error_unknow)
        elif self.viewModel.login_response == LoginResponse.user_not_exists:
            message.setWindowTitle(Strings.error_title_mb)
            message.setText(Strings.error_user_not_exists_mb)
        message.show()

    def __setup_view_model(self):
        self.viewModel.login_response_changed.connect(self.login_response)

    def __update_username(self,value:str):
        self.viewModel.username = value

    def __update_password(self,value):
        self.viewModel.password = value