#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
    abstract class interface
'''
class WeaponBehavior(object):

    def __init__(self):
        pass

    def useWeapon(self):
        pass


class Character(object):

    def __init__(self):
        pass

    def fight(self):
        pass

    def setWeapon(self, w):
        self.weapon = w

'''
    Character Implement
'''
class King(Character):

    def fight(self):
        self.weapon.useWeapon()


class Knight(Character):

    def fight(self):
        self.weapon.useWeapon()


class Queen(Character):

    def fight(self):
        self.weapon.useWeapon()


class Troll(Character):

    def fight(self):
        self.weapon.useWeapon()

'''
    WeaponBehavior implement
'''
class SwordBehavior(WeaponBehavior):

    def useWeapon(self):
        print ('Using sword to fight!!')


class BowAndArrowBehavior(WeaponBehavior):

    def useWeapon(self):
        print ('Using bow and arrow to fight!!')


class KnifeBehavior(WeaponBehavior):

    def useWeapon(self):
        print ('Using knife to fight!!')


class AxeBehavior(WeaponBehavior):

    def useWeapon(self):
        print ('Using axe to fight!!')

if __name__ == '__main__':

    print '===== A king appears ====='
    k = King()
    k.setWeapon(SwordBehavior())
    k.fight()

    print '===== King choose his weapon to Bow and Arrow====='
    k.setWeapon(BowAndArrowBehavior())
    k.fight()

    print '===== A Troll appears====='
    t = Troll()
    t.setWeapon(AxeBehavior())
    t.fight()
