from shutil import copyfile
import os


class check:
    def __init__(self) -> None:
        path = self.path()
        cookie_path = str(path) + "/modules/clients/music163.pkl"
        try:
            if os.path.isfile("music163.pkl"):
                copyfile("music163.pkl", cookie_path)
                print("cookie信息复制成功")
            else:
                if os.path.isfile(cookie_path):
                    copyfile(cookie_path, "music163.pkl")
                    print("cookie信息复制成功")
                else:
                    print("没有cookie信息，将自动使用扫码登录")
        except:
            print("复制cookie信息出错")

        try:
            lib_path = str(path) + "/modules/core/music163.py"
            if os.path.isfile("music163.py"):
                copyfile("music163.py", lib_path)
                print("复制组件库")
            else:
                print("不存在必要组件")
                raise RuntimeError("没有找到必要组件music163.py")
        except:
            raise RuntimeError("复制组件错误")

    def path(self):
        import DecryptLogin

        model_path = DecryptLogin.__file__
        path = os.path.split(model_path)[0]
        path = path.replace("\\", "/")
        print("库路径为：" + path)
        return path


check()  # 调用检查函数，检查是否符合运行条件
