import os

class check:
    def __init__(self) -> None:
        path = self.path()
        try:
            cookie_path = str(path) + "/modules/clients/music163.pkl"
            command = "cp music163.pkl " + str(cookie_path)
            os.system(command)
            print("cookie信息复制成功")
        except:
            print("没有cookie信息，将自动使用扫码登录")

            try:
                lib_path = str(path) + "/modules/core/music163.py"
                command = "cp music163.py " + str(lib_path)
                os.system(command)
            except:
                raise RuntimeError("没有找到组件music163.py")

    def path(self):
        import DecryptLogin

        model_path = DecryptLogin.__file__
        path = os.path.split(model_path)[0]
        path = path.replace("\\", "/")
        print(path)
        return path

check()  # 调用检查函数，检查是否符合运行条件