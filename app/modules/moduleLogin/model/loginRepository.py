import requests
import app.modules.moduleLogin.enums.loginResponse as LoginResponse


class LoginRepository:
    def __init__(self):
        super(LoginRepository, self).__init__()

    def login_api(self, username: str, password: str) -> LoginResponse:
        login_response: LoginResponse = LoginResponse.unknow_response
        try:
            payload = {
                "username":username,
                "password":password
            }
            request = requests.get("http://localhost:8000/login", verify=False, params=payload)
            if request.status_code == 200:
                json_response = request.json()
                login_response = int(json_response["response"])
            else:
                raise Exception(f"error de api: {request.status_code}")
        except Exception as error:
            print(error)
        return login_response
