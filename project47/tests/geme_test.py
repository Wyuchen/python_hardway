#!/usr/bin/python
from nose.tools import *
from project47.game import Room
def test_room():
    gold=Room('Goldroom',
              '''
              this room has gold in it you can grab.
              there is a door to the north
              ''')
    assert_equal(gold.name,'Goldroom')
    assert_equal(gold.paths,{})

def test_room_paths():
    center=Room('center','test room in the center')
    north=Room('North','test room in the north')
    south=Room('south','test room in the south')
    center.add_paths({'north':north,'south':south})
    assert_equal(center.go('north'),north)
    assert_equal(center.go('south'),south)

def test_map():
    start=Room('start','you can go west and down a hole')
    west=Room('Trees','there are tree here,you can go east')
    down=Room('dungeon','it is dark here,you can go up')
    start.add_paths({'west':west,'down':down})
    west.add_paths({'east':start})
    down.add_paths({'up':start})
    assert_equal(start.go('west'),west)
    assert_equal(start.go('west').go('east'),start)
    assert_equal(start.go('down').go('up'),start)

