from PySide6.QtWidgets import QApplication
from app.modules.moduleLogin.view.login import Login
from app.modules.moduleLogin.viewModel.loginViewModel import LoginViewModel
from app.modules.moduleLogin.model.loginRepository import LoginRepository
import sys

def run():
    app = QApplication(sys.argv)
    login = Login(
                LoginViewModel(
                    LoginRepository()
                )
            )
    sys.exit(app.exec())
