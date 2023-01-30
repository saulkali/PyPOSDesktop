class PatterDesignUtil:
    @staticmethod
    def singleton(cls):
        instances:dict = dict()
        def wrap(*args,**kwargs):
            if not cls in instances:
                instances[cls] = cls(*args,**kwargs)
            return instances[cls]
        return wrap