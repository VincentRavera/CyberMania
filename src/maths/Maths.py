'''
Created on 17 janv. 2017

@author: vince
'''


def updatePositionOfObject(myObject):
    '''
    Update the position of an object
    '''
    speed = myObject.speed
    currentPosi = myObject.position
    newPosition = currentPosi + speed
    myObject.position = newPosition