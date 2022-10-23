import os
from shutil import copyfile


class get_cookie:
    def __init__(self) -> None:
        path = self.path()
        cookie_path = str(path) + "/modules/clients/music163.pkl"
        try:
            if os.path.isfile(cookie_path):
                copyfile(cookie_path, "music163.pkl")
                print("cookie信息复制成功")
            else:
                print("没有cookie信息，请重新运行run.bat")
        except:
            print("复制cookie信息出错")

    def path(self):
        import DecryptLogin

        model_path = DecryptLogin.__file__
        path = os.path.split(model_path)[0]
        path = path.replace("\\", "/")
        print("库路径为：" + path)
        return path


get_cookie()  # 回调函数
