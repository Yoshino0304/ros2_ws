import rclpy
from rclpy.node import Node
from person_msgs.msg import Int 16

class Talker():
    def __init__(self):
    

def cb(request, response):
    if request.name == "吉野泰生":
        response.age = 19
    else:
        response.age = 225

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)

