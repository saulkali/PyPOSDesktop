from PySide6.QtCore import QObject,Signal,Property
import app.modules.moduleLogin.enums.loginResponse as LoginResponse
from app.modules.moduleLogin.model.loginRepository import LoginRepository

class LoginViewModel(QObject):

    __repository:LoginRepository

    username_changed = Signal()
    password_changed = Signal()
    login_response_changed = Signal()

    def __init__(self,login_repository:LoginRepository):
        super().__init__()
        self.__repository = login_repository

        self.login_response:LoginResponse = None
        self.username:str = ""
        self.password:str = ""

    @Property(str,notify=username_changed)
    def username_property(self):
        return self.username

    @username_property.setter
    def username_property(self,value):
        self.username = value
        self.username_changed.emit()

    @Property(str,notify=password_changed)
    def password_property(self):
        return self.password

    @password_property.setter
    def password_property(self,value):
        self.password = value
        self.password_changed.emit()

    @Property(str,notify=login_response_changed)
    def login_response_property(self):
        return self.login_response

    @login_response_property.setter
    def login_response_property(self,value):
        self.login_response = value
        self.login_response_changed.emit()


    def login(self):
        print("username: ", self.username, "password: ", self.password)
        if len(self.password) == 0 or len(self.username) == 0:
            self.login_response = LoginResponse.user_empty
            self.login_response_changed.emit()
        else:
            self.login_response = self.__repository.login_api(self.username, self.password)
            self.login_response_changed.emit()