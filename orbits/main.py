# import libraries

import sys
import random
import math
import pygame
from pygame import mixer
from PyQt5 import QtCore, QtGui, QtWidgets

pygame.init()
pygame.mixer.init()

# colour variables
white = (255, 255, 255)
red = (247, 12, 36)
blue = (26, 9, 181)
light_blue = (12, 224, 247)
yellow = (247, 224, 12)
green = (12, 247, 32)
pink = (235, 63, 226)
orange = (235, 158, 63)
cyan = (52, 235, 204)
black = (0, 0, 0)

# star basic parameters, default X,Y used for object position calculation, super important, do not change!
star_radius = 30
center = (640, 360)
defaultX = 640
defaultY = 360

# object basic parameters

distance1 = 75
size1 = 6
planet1_sound = mixer.Sound('G4_ff.wav')

distance2 = 125
size2 = 10
planet2_sound = mixer.Sound('C5_ff.wav')

distance3 = 225
size3 = 9
planet3_sound = mixer.Sound('C4_ff.wav')
sat_dist3 = 22
sat_angle_inc3 = .12
sat_size3 = 4
sat_dist4 = 45
sat_angle_inc4 = .08
sat_size4 = 3

distance4 = 325
size4 = 14
planet4_sound = mixer.Sound('C3_ff.wav')
sat_dist1 = 30
sat_angle_inc1 = .06
sat_size1 = 2
sat_dist2 = 60
sat_angle_inc2 = .03
sat_size2 = 5


# this part was auto completed from Qt Designer, it's the options menu's items and their basic parameters such as labels and menu items
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Run = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.checked())
        self.Run.setGeometry(QtCore.QRect(354, 510, 93, 28))
        self.Run.setObjectName("Run")
        self.planet1__flag = QtWidgets.QCheckBox(self.centralwidget)
        self.planet1__flag.setGeometry(QtCore.QRect(80, 110, 141, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planet1__flag.setFont(font)
        self.planet1__flag.setObjectName("planet1__flag")
        self.planet2__flag = QtWidgets.QCheckBox(self.centralwidget)
        self.planet2__flag.setGeometry(QtCore.QRect(80, 210, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planet1__flag.setChecked(True)
        self.planet2__flag.setFont(font)
        self.planet2__flag.setObjectName("planet2__flag")
        self.planet3__flag = QtWidgets.QCheckBox(self.centralwidget)
        self.planet3__flag.setGeometry(QtCore.QRect(80, 310, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planet2__flag.setChecked(True)
        self.planet3__flag.setFont(font)
        self.planet3__flag.setObjectName("planet3__flag")
        self.planet4__flag = QtWidgets.QCheckBox(self.centralwidget)
        self.planet4__flag.setGeometry(QtCore.QRect(80, 390, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planet3__flag.setChecked(True)
        self.planet4__flag.setFont(font)
        self.planet4__flag.setObjectName("planet4__flag")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.planet4__flag.setChecked(True)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.speed = QtWidgets.QComboBox(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(560, 130, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.speed.setFont(font)
        self.speed.setObjectName("speed")
        self.speed.addItem("Slow 1/2")
        self.speed.addItem("Slow 1/3")
        self.speed.addItem("Fast 1/2")
        self.speed.addItem("Fast 1/3")
        self.speed.addItem("Faster 1/2")
        self.speed.addItem("Faster 1/3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 40, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        
        #this is the "exit" button, i think
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionExit.triggered.connect(QtWidgets.qApp.quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orbital Resonance Options"))
        self.Run.setStatusTip(_translate("MainWindow", "RUN!"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.planet1__flag.setText(_translate("MainWindow", "Planet 1"))
        self.planet2__flag.setText(_translate("MainWindow", "Planet 2"))
        self.planet3__flag.setText(_translate("MainWindow", "Planet 3"))
        self.planet4__flag.setText(_translate("MainWindow", "Planet 4"))
        self.label.setText(_translate("MainWindow", "Choose which planets you want to have orbiting."))
        self.speed.setItemText(0, _translate("MainWindow", "Slow 1/2"))
        self.speed.setItemText(1, _translate("MainWindow", "Slow 1/3"))
        self.speed.setItemText(2, _translate("MainWindow", "Fast 1/2"))
        self.speed.setItemText(3, _translate("MainWindow", "Fast 1/3"))
        self.speed.setItemText(4, _translate("MainWindow", "Faster 1/2"))
        self.speed.setItemText(5, _translate("MainWindow", "Faster 1/3"))
        self.label_2.setText(_translate("MainWindow", "Speed and resonance frequency"))
        #this is the file menu, there's only one option, "quit"
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Quit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

       #clicking on the option must "connect" with something in order to trigger an action
        self.Run.clicked.connect(self.pressed)
        self.Run.clicked.connect(QtWidgets.qApp.quit)

        
    #Qt Designer can only do so much, specific actions have to be added according to purpose
    #in this case unchecking the planet boxes switches their flags to False and ensures they will not appear in the animation once it triggers
    def checked(self):
        if self.planet1__flag.isChecked() == False:
            main.Planet1 = False
        else:
            main.Planet1 = True
        if self.planet2__flag.isChecked() == False:
            main.Planet2 = False
        else:
            main.Planet2 = True
        if self.planet3__flag.isChecked() == False:
            main.Planet3 = False
        else:
            main.Planet3 = True
        if self.planet4__flag.isChecked() == False:
            main.Planet4 = False
        else:
            main.Planet4 = True


    #this part conveys a set of parameters to the main(), user selection in the options-speed drop-down menu controls the animation's speed
    # angle_inc defines the rotation speed, it is the angle change per frame so the lower the value=the slower the rotation speed relative to orbit radius
    def pressed(self):
        index = self.speed.currentIndex()
        if index == 0:
            main.angle1_inc = .04
            main.angle2_inc = .02
            main.angle3_inc = .01
            main.angle4_inc = .005
        if index == 1:
            main.angle1_inc = .06
            main.angle2_inc = .03
            main.angle3_inc = .015
            main.angle4_inc = .005
        if index == 2:
            main.angle1_inc = .08
            main.angle2_inc = .04
            main.angle3_inc = .02
            main.angle4_inc = .01
        if index == 3:
            main.angle1_inc = .09
            main.angle2_inc = .06
            main.angle3_inc = .03
            main.angle4_inc = .01
        if index == 4:
            main.angle1_inc = .16
            main.angle2_inc = .08
            main.angle3_inc = .04
            main.angle4_inc = .02
        if index == 5:
            main.angle1_inc = .18
            main.angle2_inc = .09
            main.angle3_inc = .06
            main.angle4_inc = .03
        main()
    

def main():

    planet1_orbit = 0
    planet2_orbit = 0
    planet3_orbit = 0
    planet4_orbit = 0
    sat_orb1 = 0
    sat_orb2 = 0
    sat_orb3 = 0
    sat_orb4 = 0

    # setup screen
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Orbital Resonance Cosmic Sounds")

    # background stars and clock variable
    stars = [(random.randint(0, 1279), random.randint(0, 719)) for x in range(140)]
    clock = pygame.time.Clock()

    # heart of the beast, X and Y are a function of distance (orbit radius) + X or Y
    # where X and Y are either the default (central) X and Y for planets or the parent planet's X and Y for satellites

    class PlanetMove:
        def planetX(planet_orbit, distance, X):
            # changing this to a negative value will move the starting point
            # to the left instead of the right where it is as it is at the moment
            x = math.cos(planet_orbit) * distance + X
            return x

        def planetY(planet_orbit, distance, Y):
            # changing this to a positive value (removing the minus sign) will change the output to a clockwise rotation
            # instead of the counter-clockwise rotation we are currently implementing
            y = -math.sin(planet_orbit) * distance + Y
            return y

        def tone(sound):
            sound.play(0)

    class img:
        def Planet_1():
            pygame.draw.circle(screen, red, (X1, Y1), size1)

        def Planet_2():
            pygame.draw.circle(screen, green, (X2, Y2), size2)

        def Planet_3():
            pygame.draw.circle(screen, yellow, (X3, Y3), size3)
            pygame.draw.circle(screen, cyan, (sat_X3, sat_Y3), sat_size3)
            pygame.draw.circle(screen, light_blue, (sat_X4, sat_Y4), sat_size4)

        def Planet_4():
            pygame.draw.circle(screen, blue, (X4, Y4), size4)
            pygame.draw.circle(screen, pink, (sat_X1, sat_Y1), sat_size1)
            pygame.draw.circle(screen, orange, (sat_X2, sat_Y2), sat_size2)

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # coordinates calculations
        X1 = PlanetMove.planetX(planet1_orbit, distance1, defaultX)
        Y1 = PlanetMove.planetY(planet1_orbit, distance1, defaultY)
        if pygame.Rect(710, 355, 10, 10).collidepoint(X1, Y1):
            if main.Planet1 == True:
                PlanetMove.tone(planet1_sound)
            else:
                pass
        # changing the angle is what makes it move
        planet1_orbit += main.angle1_inc
        
        X2 = PlanetMove.planetX(planet2_orbit, distance2, defaultX)
        Y2 = PlanetMove.planetY(planet2_orbit, distance2, defaultY)
        if pygame.Rect(760, 355, 10, 10).collidepoint(X2, Y2):
            if main.Planet2 == True:
                PlanetMove.tone(planet2_sound)
            else:
                pass
        planet2_orbit += main.angle2_inc
        
        X3 = PlanetMove.planetX(planet3_orbit, distance3, defaultX)
        Y3 = PlanetMove.planetY(planet3_orbit, distance3, defaultY)
        if pygame.Rect(860, 355, 10, 10).collidepoint(X3, Y3):
            if main.Planet3 == True:
                PlanetMove.tone(planet3_sound)
            else:
                pass
        planet3_orbit += main.angle3_inc
        
        X4 = PlanetMove.planetX(planet4_orbit, distance4, defaultX)
        Y4 = PlanetMove.planetY(planet4_orbit, distance4, defaultY)
        if pygame.Rect(960, 355, 10, 10).collidepoint(X4, Y4):
            if main.Planet4 == True:
                PlanetMove.tone(planet4_sound)
            else:
                pass
        planet4_orbit += main.angle4_inc

        #since satellites orbit planets, not stars, the defaultX and Y have to be replaced by the planet's dynamic coordinates
        #in order to center the satellite around a planet and not our main star
        sat_X3 = PlanetMove.planetX(sat_orb3, sat_dist3, X3)
        sat_Y3 = PlanetMove.planetY(sat_orb3, sat_dist3, Y3)
        sat_orb3 += sat_angle_inc3
        sat_X4 = PlanetMove.planetX(sat_orb4, sat_dist4, X3)
        sat_Y4 = PlanetMove.planetY(sat_orb4, sat_dist4, Y3)
        sat_orb4 += sat_angle_inc4

        # same for the satellites of planet 4
        sat_X1 = PlanetMove.planetX(sat_orb1, sat_dist1, X4)
        sat_Y1 = PlanetMove.planetY(sat_orb1, sat_dist1, Y4)
        sat_orb1 += sat_angle_inc1
        sat_X2 = PlanetMove.planetX(sat_orb2, sat_dist2, X4)
        sat_Y2 = PlanetMove.planetY(sat_orb2, sat_dist2, Y4)
        sat_orb2 += sat_angle_inc2

        # here we start drawing by first resetting the screen to black
        screen.fill(black)

        # then we add the stars
        for star in stars:
            x, y = star[0], star[1]
            pygame.draw.line(screen, white, (x, y), (x, y))

        # then we add everything else starting with our stationary central star
        pygame.draw.circle(screen, white, center, star_radius)
        # and then, depending on the user's choises earlier we get the planets
        if main.Planet1 == True:
            img.Planet_1()
        else:
            pass
        if main.Planet2 == True:
            img.Planet_2()
        else:
            pass
        if main.Planet3 == True:
            img.Planet_3()
        else:
            pass
        if main.Planet4 == True:
            img.Planet_4()
        else:
            pass

        # flip, tick, repeat!
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    