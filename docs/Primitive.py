from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT  import *
from math import *

class Box:

    size = [2.0, 2.0, 2.0]

    def __init__(self):
        self.size = [2.0, 2.0, 2.0]

    def setValue(self, x, y, z):
        if float(x) <= 1.0:
            self.size[0] = 2.0
        else:
            self.size[0] = float(x) * 2

        if float(y) <= 1.0:
            self.size[1] = 2.0
        else:
            self.size[1] = float(y) * 2

        if float(z) <= 1.0:
            self.size[2] = 2.0
        else:
            self.size[2] = float(z) * 2

    def Draw(self):
        point1 = [self.size[0] / 2.0, self.size[1] / 2.0, self.size[2] / -2.0]
        point2 = [self.size[0] / 2.0, self.size[1] / 2.0, self.size[2] / 2.0]
        point3 = [self.size[0] / 2.0, self.size[1] / -2.0, self.size[2] / 2.0]
        point4 = [self.size[0] / 2.0, self.size[1] / -2.0, self.size[2] / -2.0]
        point5 = [self.size[0] / -2.0, self.size[1] / -2.0, self.size[2] / 2.0]
        point6 = [self.size[0] / -2.0, self.size[1] / 2.0, self.size[2] / 2.0]
        point7 = [self.size[0] / -2.0, self.size[1] / 2.0, self.size[2] / -2.0]
        point8 = [self.size[0] / -2.0, self.size[1] / -2.0, self.size[2] / -2.0]

        glBegin(GL_QUADS)

        glVertex3fv(point1)  # TOP
        glVertex3fv(point2)
        glVertex3fv(point6)
        glVertex3fv(point7)

        glVertex3fv(point3)  # Bottom
        glVertex3fv(point4)
        glVertex3fv(point8)
        glVertex3fv(point5)

        glVertex3fv(point2)  # Front
        glVertex3fv(point3)
        glVertex3fv(point5)
        glVertex3fv(point6)

        glVertex3fv(point7)  # Back
        glVertex3fv(point8)
        glVertex3fv(point4)
        glVertex3fv(point1)

        glVertex3fv(point6)  # Left
        glVertex3fv(point5)
        glVertex3fv(point8)
        glVertex3fv(point7)

        glVertex3fv(point1)  # Right
        glVertex3fv(point4)
        glVertex3fv(point3)
        glVertex3fv(point2)

        glEnd()

class Cone:
    height = 2.0
    bottomRadius = 2.0

    def __init__(self):
        self.height = 2.0
        self.bottomRadius = 2.0

    def setValue(self, r, h):
        if float(r) <= 2.0:
            self.bottomRadius = 2.0
        else:
            self.bottomRadius = float(r)

        if float(h) <= 2.0:
            self.height = 2.0
        else:
            self.height = float(h)

    def Draw(self):
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, self.height)
        angle = 0.0

        for angle in range(0, 360):
            glVertex3f(sin(angle) * self.bottomRadius / 2, cos(angle) * self.bottomRadius / 2, 0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, 0)
        angle = 0.0
        for angle in range(0, 360):
            glNormal3f(0, -1, 0)
            glVertex3f(sin(angle) * self.bottomRadius / 2, cos(angle) * self.bottomRadius / 2, 0)
        glEnd()


class Cylinder:
    height = 2.0
    radius = 2.0

    def __init__(self):
        self.height = 2.0
        self.radius = 2.0

    def setValue(self, r, h):
        if float(r) <= 2.0:
            self.radius = 2.0
        else:
            self.radius = float(r)

        if float(h) <= 2.0:
            self.height = 2.0
        else:
            self.height = float(h)

    def Draw(self):
        x = 0.0
        y = 0.0
        angle = 0.0
        angle_stepsize = 0.01
        CONST_PI = 3.14159265

        glBegin(GL_QUAD_STRIP)
        for angle in self.myrange(0.0, 2 * CONST_PI, angle_stepsize):
            x = self.radius * cos(angle)
            y = self.radius * sin(angle)
            glVertex3f(x, y, self.height)
            glVertex3f(x, y, 0.0)

        glVertex3f(self.radius, 0.0, self.height)
        glVertex3f(self.radius, 0.0, 0.0)
        glEnd()

        glBegin(GL_POLYGON)
        angle = 0.0
        for angle in self.myrange(0.0, 2 * CONST_PI, angle_stepsize):
            x = self.radius * cos(angle)
            y = self.radius * sin(angle)
            glVertex3f(x, y, self.height)

        glVertex3f(self.radius, 0.0, self.height)
        glEnd()

        glBegin(GL_POLYGON)
        angle = 0.0
        for angle in self.myrange(0.0, 2 * CONST_PI, angle_stepsize):
            x = self.radius * cos(angle)
            y = self.radius * sin(angle)
            glVertex3f(x, y, 0)

        glVertex3f(self.radius, 0.0, 0)
        glEnd()

    def myrange(self, start, end, step):
        r = start
        while (r < end):
            yield r
            r += step

class Sphere:
    raidus = 1.0

    def __init__(self):
        self.radius = 1.0

    def setValue(self, r):
        if float(r) <= 1.0:
            self.radius = 1.0
        else:
            self.radius = float(r)

    def Draw(self):
        CONST_PI = 3.14159265
        lats = 50
        longs = 50

        for i in range (0, lats) :
            lat0 = float( CONST_PI * ( -0.5 + float (i - 1 ) / lats ) )
            z0 = float( sin(lat0) )
            zr0 = float( cos(lat0) )

            lat1 = float ( CONST_PI * ( -0.5 + float (i) / lats ) )
            z1 = float( sin(lat1) )
            zr1 = float( cos(lat1) )

            glBegin(GL_QUAD_STRIP)

            for j in range (0, longs) :
                lng = 2 * CONST_PI * float( j - 1 ) / longs
                x = float ( cos(lng) )
                y = float ( sin(lng) )

                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr0, y * zr0, z0)
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(x * zr1, y * zr1, z1)

            glEnd()