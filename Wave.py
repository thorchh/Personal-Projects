import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Slider, Button
fig, ax = plt.subplots()
plt.subplots_adjust(left = 0.1, bottom =0.6)

t1= 0
dt0 = 0.2
TT0 = 100
ct = 0
w0= 1.25
X0 =5
arrT = []
arrS = []
arrV = []
arrA = []

def displacementCalc(ct):
    return (X0 * math.sin(w0* ct))
def velocityCalc(ct):
    return (X0 * w0 * math.cos(w0* ct))
def accelerationCalc(ct):
    return (-X0 * (w0*w0)*math.sin(w0* ct))


for ct in range (0,TT0+1,1):
    arrT.append(ct*dt0)
for element in arrT:
    arrS.append(displacementCalc(element))
for element in arrT:
    arrV.append(velocityCalc(element))
for element in arrT:
    arrA.append(accelerationCalc(element))

lineS = plt.plot(arrT,arrS)
lineV = plt.plot(arrT,arrV)
lineA = plt.plot(arrT,arrA)

axAngFreq = plt.axes([0.1,0.4,0.8,0.05])
axAmp = plt.axes([0.1,0.3,0.8,0.05])
axDT = plt.axes([0.1,0.2,0.8,0.05])
axTT = plt.axes([0.1,0.1,0.8,0.05])

sAngFreq = Slider(axAngFreq, 'w', 0.1, 30.0, valinit=w0)
sAmp = Slider(axAmp, 'X0', 0.1, 30.0, valinit=X0)
sDT = Slider(axDT, 'dt', 0.1, 30.0, valinit=dt0)
sTT = Slider(axTT, 'TT', 0.1, 100.0, valinit=TT0)

#AngFreq = 0
#Amp = 0
#DT = 0
#TT = 0

#def displacementCalc2(ct):
    #return (Amp * math.sin(AngFreq* ct))
#def velocityCalc2(ct):
    #return (Amp * AngFreq * math.cos(AngFreq* ct))
#def accelerationCalc2(ct):
    #return (-Amp * (AngFreq*AngFreq)*math.sin(AngFreq* ct))

def update(val):
    AngFreq = sAngFreq.val
    Amp = sAmp.val
    DT = sDT.val
    TT = sTT.val
    t1= 0
    ct = 0
    arrT = []
    arrS = []
    arrV = []
    arrA = []
    for ct in range (0,int(TT)+1,1):
        arrT.append(ct*dt0)
    for element in arrT:
        arrS.append(Amp * math.sin(AngFreq* element))
    for element in arrT:
        arrV.append(Amp * AngFreq * math.cos(AngFreq* element))
    for element in arrT:
        arrA.append(-Amp * (AngFreq*AngFreq)*math.sin(AngFreq* element))
    ax.cla()
    lineS = ax.plot(arrT,arrS)
    lineV = ax.plot(arrT,arrV)
    lineA = ax.plot(arrT,arrA)
    fig.canvas.draw_idle()
    
sAngFreq.on_changed(update)
sAmp.on_changed(update)
sDT.on_changed(update)
sTT.on_changed(update)

plt.show()

    #w.set_ydata(yval)
    #plt.draw
#slider2.on_changed(valUpdate)

#slider1 = Slider(axSlider1, 'Slider 1', valmin=0, valmax= 100)
#slider2 = Slider( ax=axSlider2, label='Slider 2', valmin=0, valmax=100,valinit=30, valfmt='%1.2f', valstep=10, color = 'green', closedmax = True)



#t1= 0
#dt = 0.2
#TT = 100
#ct = 0
#w= 1.25
#X0 =5
#arrT = []
#arrS = []
#arrV = []
#arrA = []
#def displacementCalc(ct):
    #return (X0 * math.sin(w* ct))
#def velocityCalc(ct):
    #return (X0 * w * math.cos(w* ct))
#def accelerationCalc(ct):
    #return (-X0 * (w*w)*math.sin(w* ct))
#displacementCalc(ct)
#velocityCalc(ct)
#accelerationCalc(ct)
##for ct in range (0,TT0+1,1):
    ##arrT.append(ct*dt0)
#print(arrT)
##for element in arrT:
    ##arrS.append(displacementCalc(element))
#print (arrS)
#plt.plot(arrT,arrS)
#plt.show()
##for element in arrT:
    ##arrV.append(velocityCalc(element))
#print (arrV)
##for element in arrT:
    ##arrA.append(accelerationCalc(element))
#print (arrA)
#lineS = ax.plot(arrT,arrS)
#lineV = ax.plot(arrT,arrV)
#lineA = ax.plot(arrT,arrA)
#plt.show()
