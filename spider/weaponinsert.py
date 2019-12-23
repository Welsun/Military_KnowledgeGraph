import pymongo
from army_tree_crawler import neo_models
from py2neo import Graph,Node,Relationship,NodeMatcher
from WeaponItems import plane,ship
neo =neo_models.Neo4j()
neo.connectDB()
conn = pymongo.MongoClient(host="10.6.213.55",port=27017)
db =conn['military']['knowledge_base']
big_classes = ["舰船舰艇","枪械与单兵","坦克装甲车辆","火炮","导弹武器","太空装备","爆炸物"]

big_node = Node("武器第一类",name = big_classes[6])
#neo.graph.create(big_node)
data = {"大类":big_classes[6]}
results = db.find(data)
for result in results:
    matcher = NodeMatcher(neo.graph)
    main_node = matcher.match("武器第二类", name=result.get("类型")).first()
    if not main_node:
        main_node = Node("武器第二类", name=result.get("类型"))
    node = Node(result.get("类型"),
                name=result.get("名称"),
                country=result.get('国家'),
                # if result.get('简介'):
                simple_info=result.get('简介'),
                # if result.get('结构特点'):
                # structure = result.get('结构特点'),
                #  # if result.get('使用情况'):
                #  use_info = result.get('使用情况'),

                #  history = result.get("研制历程"),
                build_time=result.get("研制时间"),
                # attend_time=result.get("服役时间"),
                # status=result.get("现状"),
                # manufacturer=result.get("制造厂"),
                # ton=result.get("满排吨位"),
                # people=result.get("编制"),
                # length=result.get("舰长"),
                # width=result.get("型宽"),
                # water=result.get("满载排水量"),
                # distance=result.get("续航距离"),
                # speed=result.get("航速"),

                maker = result.get("研制单位"),
                # lanuch_time=result.get("发射日期"),
                # lanuch_place = result.get("发射地点"),
                caliber = result.get("弹径"),
                # shoot_module = result.get("发射性能"),
                bullet_length = result.get("弹长"),
                weight = result.get("全重"),
                powder_type = result.get("装药类型"),
                empennage=result.get("尾翼类型"),
                fuze = result.get("引信类型"),
                # width = result.get("宽度"),
                # height = result.get("高度"),
                #max_speed = result.get("炮口初速"),
                # max_distance = result.get("最大射程"),
                # chassis_type = result.get("底盘类型"),
                # people_num = result.get("乘员与载员"),
                # capacity = result.get("弹匣容弹量"),
                # war_info = result.get("参战情况"),
                # system = result.get("制导系统"),
                # shoot_distance=result.get("射程"),
                # pathway = result.get("轨道"),
                # lanucher = result.get("运载火箭"),
                # latitude = result.get("纬度"),
                # longtitude = result.get("经度"),
                first_class=result.get("大类"),
                second_class=result.get("类型"),
                )
    neo.graph.create(node)
    print("建造节点")
    relation = Relationship(node, "belongs_to", main_node)
    neo.graph.create(relation)

