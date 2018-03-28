from __future__ import division
import numpy as np

def calcWS2(i, j, y, isotope):
   if isotope not in dispatchtable.keys():
       ws2 = 0.
   else:
       ws2 = dispatchtable[isotope](i, j, y)
   return ws2

def Ni59(i,j,y):
    if i == 0 and j == 0:
        WS2 = (0.04324609124625189 - 0.13123806013643788*y 
                + 0.3877927358232908*y**2 - 0.5031807533098597*y**3 
                + 0.3129460800842625*y**4 - 0.09294069957664952*y**5 
                + 0.010939268410990407*y**6)/np.exp(2.*y)
    elif i == 1 and j == 1:
        WS2 = (0.04303736359136173 - 0.13075035793210424*y 
                + 0.39523546864548936*y**2 - 0.5154051965707896*y**3 
                + 0.3200479908216438*y**4 - 0.09463672886482437*y**5 
                + 0.011062285090794717*y**6)/np.exp(2.*y)
    else:
        WS2 = (-0.043141601185748175 + 0.13099400242546577*y 
                - 0.3914764587179549*y**2 + 0.5092418818256778*y**3 
                - 0.31647445348085534*y**4 + 0.09378518405364651*y**5 
                - 0.011000597190320371*y**6)/np.exp(2.*y)
    return WS2

def Al27(i,j,y):
    if i == 0 and j == 0:
        WS2 = (0.030946466658602678 - 0.036724195099056736*y 
                + 0.02653470770381152*y**2 - 0.002416057844169939*y**3 
                + 0.011001067283047518*y**4)/np.exp(2.*y)
    elif i == 1 and j == 1:
        WS2 = (0.021883360052856037 - 0.009444764771082234*y 
                + 0.011506022741508951*y**2 + 0.0009535368761278121*y**3 
                + 0.010481297740411958*y**4)/np.exp(2.*y)
    else:
        WS2 = (0.026023310170958405 - 0.021056715592501225*y 
                + 0.01586427118299763*y**2 + 0.0006060767741112289*y**3 
                + 0.010571282241782384*y**4)/np.exp(2.*y)
    return WS2

def N14(i,j,y):
    if i == 0 and j == 0:
        WS2 = (0.023007853423118257*(1.2098553307496394 + 1.*y)**2)/np.exp(2.*y)
    else:
        WS2 = 0.
    return WS2


def He3(i,j,y):
    if i == 0 and j == 0:
        WS2 = 0.0397887/np.exp(2.*y)
    elif i == 1 and j == 1:
        WS2 = 0.0397887/np.exp(2.*y)
    else:
        WS2 = -0.0397887/np.exp(2.*y)
    return WS2

def H(i,j,y):
    WS2 = 0.039788735772973836#/np.exp(2.*y)
    return WS2   

def Xe129(i,j,y):
    if i == 0 and j == 0:     
        WS2 = (0.010404436144595613 - 0.036544366808683726*y + 
                 0.06435315117845676*y**2 - 0.06636061394953534*y**3 + 
                 0.04319773517899248*y**4 - 0.01706358482436624*y**5 + 
                 0.00405027170634069*y**6 - 0.0005404221227330367*y**7 + 
                 0.000032952872479730084*y**8 - 
                 1.2849348515446646e-7*y**9 + 1.295121171568424e-10*y**10)/np.exp(2.*y)
    elif i == 1 and j == 1:
        WS2 = (0.009256942521290935 - 0.030494848130468506*y + 
                 0.051234027256647774*y**2 - 0.05089830170682882*y**3 + 
                 0.03238601981523851*y**4 - 0.012741768322147035*y**5 + 
                 0.0030733393742958747*y**6 - 
                 0.0004235714049895079*y**7 + 
                 0.0000273160570250448*y**8 - 
                 1.1691210783186218e-7*y**9 + 1.2951223518285722e-10*y**10)/np.exp(2.*y)
    else:
        WS2 = (-0.00981393230855825 + 0.03340000636472022*y - 
                 0.057450420574708144*y**2 + 0.058128093534203534*y**3 - 
                 0.03740107149254411*y**4 + 0.014743897053985473*y**5 - 
                 0.0035285222323281308*y**6 + 
                 0.00047863089552092176*y**7 - 
                 0.000030005008237028564*y**8 + 
                 1.2270279913173943e-7*y**9 - 1.2951217616983635e-10*y**10)/np.exp(2.*y)
    return WS2

def Xe131(i,j,y):
    if i == 0 and j == 0: 
        WS2 = (0.007353910694021366 + 0.024013554202436335*y - 
                 0.02014650487125114*y**2 - 0.037184108285885614*y**3 + 
                 0.10207295648693686*y**4 - 0.08818794415698591*y**5 + 
                 0.03593113383888596*y**6 - 0.007020155839698539*y**7 + 
                 0.0005402993168705856*y**8 - 6.167594109512812e-7*y**9 + 
                 1.787035062316364e-10*y**10)/np.exp(2.*y)
    elif i == 1 and j == 1:
        WS2 = (0.0066360458734753686 + 0.0230091769076141*y - 
                 0.0167703486318344*y**2 - 0.036938300365609425*y**3 + 
                 0.09593468456183336*y**4 - 0.08255616478254374*y**5 + 
                 0.03381938601451815*y**6 - 0.006662512003029585*y**7 + 
                 0.0005185483277899781*y**8 - 6.047848694091502e-7*y**9 + 
                 1.7870236298441898e-10*y**10)/np.exp(2.*y)
    else:
        WS2 = (-0.006985763287928304 - 0.02351657691879264*y + 
                 0.018478701186953755*y**2 + 0.03696179519459378*y**3 - 
                 0.09886450319704412*y**4 + 0.08528791992678614*y**5 - 
                 0.03485107661177335*y**6 + 0.006838186074602294*y**7 - 
                 0.0005292745155866782*y**8 + 6.107721235197574e-7*y**9 - 
                 1.787029346070819e-10*y**10)/np.exp(2.*y)
    return WS2


def Ge73(i,j,y):
    if i == 0 and j == 0: 
        WS2 = (0.07569236645209282 - 0.24996303506903517*y + 
                 0.47562025484670917*y**2 - 0.41626333438694146*y**3 + 
                 0.21340048448586535*y**4 - 0.06166649195002185*y**5 + 
                 0.01159464153733673*y**6 - 0.001207801478277386*y**7 + 
                 0.0001895056721698479*y**8)/np.exp(2.*y)
    elif i == 1 and j == 1:
        WS2 = (0.07081519200592393 - 0.21918779412890274*y + 
                 0.4298595915810334*y**2 - 0.37365224041221856*y**3 + 
                 0.1928788579858286*y**4 - 0.05648456470258957*y**5 + 
                 0.010944968038757084*y**6 - 0.0011757815793682139*y**7 + 
                 0.00018891925256489718*y**8)/np.exp(2.*y)
    else:
        WS2 = (-0.07321317821053604 + 0.2341929690527564*y - 
                 0.45140624842646826*y**2 + 0.39350912161581447*y**3 - 
                 0.20234425646974472*y**4 + 0.058891431850794866*y**5 - 
                 0.011253792200882237*y**6 + 0.0011916541971631986*y**7 - 
                 0.00018921195056604791*y**8)/np.exp(2.*y)
    return WS2
        
def Na23(i,j,y):
    if i == 0 and j == 0:
        WS2 = (0.012667246658050316 - 0.026253291678392687*y + 
            0.04018857660630753*y**2 - 0.010514019578400978*y**3 + 
            0.0007860504953119211*y**4)/np.exp(2.*y)
    elif i == 1 and j == 1:
        WS2 = (0.009175774944806989 - 0.01670527897824205*y + 
            0.033275141545253885*y**2 - 0.007657193717801536*y**3 + 
            0.0005976759200725353*y**4)/np.exp(2.*y)
    else:
        WS2 = (0.010781085497510359 - 0.02098602155667607*y + 
            0.03609705227114852*y**2 - 0.008762130109562867*y**3 + 
            0.0006267179237745168*y**4)/np.exp(2.*y)
    return WS2

def Iodine(i,j,y):
    if i == 0 and j == 0:
        WS2 = (0.024197401761378398 - 0.09202428326341876*y 
            + 0.28839169064476144*y**2 - 0.41007547604471595*y**3 
            + 0.37687028835140307*y**4 - 0.21340443097677236*y**5 
            + 0.06977577048588966*y**6 - 0.012028060570887664*y**7 
            + 0.0008774041212728086*y**8 - 2.4335549723261276e-6*y**9 
            + 2.0143142512669966e-9*y**10)/np.exp(2.*y)
    elif i == 1 and j == 1:
        WS2 = (0.008781603142616383 - 0.03225553483830543*y 
            + 0.16212613932979994*y**2 - 0.26834882763889173*y**3 
            + 0.274618863866354*y**4 - 0.1664979321266973*y**5 
            + 0.05682445016054854*y**6 - 0.010009885388455177*y**7 
            + 0.000719711149108427*y**8 + 2.2100355006206994e-6*y**9 
            + 2.014309360420509e-9*y**10)/np.exp(2.*y)
    else:
        WS2 = (0.014577104628521803 - 0.054490274684087486*y 
            + 0.21250266403746382*y**2 - 0.32819096643782064*y**3 
            + 0.31983877243738634*y**4 - 0.18790269593692718*y**5 
            + 0.06284581722291*y**6 - 0.010956417733624636*y**7 
            + 0.0007934558671664674*y**8 + 1.1175823565108932e-7*y**9 
            - 2.01431180584053e-9*y**10)/np.exp(2.*y)
    return WS2
                
def Fluorine(i,j,y):
    if i == 0 and j == 0:
        WS2 = (0.034615485600459156 - 0.09034478868635375*y 
            + 0.08961135238521979*y**2 - 0.04001376348018315*y**3 
            + 0.006790207047554329*y**4)/np.exp(2.*y)
    elif i == 1 and j == 1:
        WS2 = (0.03724959674606853 - 0.09845341534907655*y 
            + 0.09773315849258363*y**2 - 0.043185518108098564*y**3 
            + 0.007166981300667365*y**4)/np.exp(2.*y)
    else:
        WS2 = (0.03590839567268977 - 0.09431387285785792*y 
            + 0.09358137207912237*y**2 - 0.04157198017325701*y**3 
            + 0.006976050955768718*y**4)/np.exp(2.*y)
    return WS2
    
dispatchtable = {}
dispatchtable['Ni59'] = Ni59
dispatchtable['Al27'] = Al27
dispatchtable['N14'] = N14
dispatchtable['He3'] = He3
dispatchtable['H'] = H
dispatchtable['Xe129'] = Xe129
dispatchtable['Xe131'] = Xe131
dispatchtable['Ge73'] = Ge73
dispatchtable['Na23'] = Na23
dispatchtable['Iodine'] = Iodine
dispatchtable['Fluorine'] = Fluorine