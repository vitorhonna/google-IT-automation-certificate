#!C:\Python310\python.exe

import math


def triangle(base, height):
    return base*height/2


def rectangle(base, height):
    return base*height


def circle(radius):
    return math.pi*(radius**2)


def donut(out_radius, in_radius):
    return circle(out_radius) - circle(in_radius)
