#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第四题
#变量和命名

#定义车辆的总数
cars=100
#每辆车的空间
space_in_a_space=4.0
#定义司机的数量
drivers=30.0
#乘客的数量
passengers=90
#空闲的车辆
cars_not_driven=cars-drivers
#可以开车的司机数
cars_drivern=drivers
#总的乘车人数:
carpool_capacity=cars_drivern*space_in_a_space
#每辆车的人数:
average_passengers_per_car=passengers/cars_drivern
print '定义车辆的总数:'
print 'there are ',cars,'cars available.'
print '可以开车的司机数 ',drivers
print '空闲的车辆 ',cars_not_driven
print '可以乘坐乘客的总数: ',carpool_capacity
print '每辆车的人数 ',average_passengers_per_car
