class plane:
    def __init__(self,result):
        #if result.get('名称'):
            self.name = result.get('名称')
        #if result.get('国家'):
            self.country = result.get('国家')
        #if result.get('简介'):
            self.simple_info = result.get('简介')
        #if result.get('结构特点'):
            self.structure = result.get('结构特点')
        #if result.get('使用情况'):
            self.use_info = result.get('使用情况')
        #if result.get('型号演变'):
            self.evolution = result.get('型号演变')
        #if result.get('首飞时间'):
            self.time_fly = result.get('首飞时间')
        #if result.get('研发单位'):
            self.RDgroup = result.get('研发单位')
        #if result.get('气动布局'):
            self.air_layout = result.get('气动布局')
        #if result.get('发动机数量'):
            self.engine_num = result.get('发动机数量')
        #if result.get('飞行速度'):
            self.speed = result.get('飞行速度')
        #if result.get('乘员'):
            self.passenger = result.get('乘员')
        #if result.get('机长'):
            self.length = result.get('机长')
        #if result.get('翼展'):
            self.width = result.get('翼展')
        #if result.get('机高'):
            self.height = result.get('机高')
        #if result.get('发动机'):
            self.engine = result.get('发动机')
        #if result.get('最大飞行速度'):
            self.max_speed = result.get('最大飞行速度')
        #if result.get('最大航程'):
            self.max_distance = result.get('最大航程')
        #if result.get('大类'):
            self.first_class = result.get('大类')
        #if result.get('类型'):
            self.second_class = result.get('类型')

class ship:
    def __init__(self,result):
        # if result.get('名称'):
        self.name = result.get('名称')
        # if result.get('国家'):
        self.country = result.get('国家')
        # if result.get('简介'):
        self.simple_info = result.get('简介')
        # if result.get('结构特点'):
        self.structure = result.get('结构特点')
        # if result.get('使用情况'):
        self.use_info = result.get('使用情况')
        self.history = result.get("研制历程")
        self.build_time = result.get("建造时间")
        self.attend_time = result.get("服役时间")
        self.status = result.get("现状")
        self.manufacturer = result.get("制造厂")
        self.ton = result.get("满排吨位")
        self.people = result.get("编制")
        self.length = result.get("舰长")
        self.width = result.get("型宽")
        self.water = result.get("满载排水量")
        self.distance = result.get("续航距离")
        self.speed = result.get("航速")
        self.first_class = result.get("大类")
        self.second_class = result.get("类型")




