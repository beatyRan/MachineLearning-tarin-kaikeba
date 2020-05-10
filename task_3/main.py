# -*- coding: utf-8 -*-
#新冠肺炎隔离检测
from task_3 import handler
from task_3 import person


if __name__ == '__main__':
    handler = handler.Handler()
    while True:
        handler.person = person.Person()
        handler.input_temperature()
        handler.input_id_number()



