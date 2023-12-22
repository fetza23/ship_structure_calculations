
from inputs import *
import math
class coefficients():
    def __init__(self):
        self.loc=x/L
    def calculate_CRW(self):
        if RSA == 200:
            CRW = 0.9
        elif RSA == 50:
            CRW = 0.75
        elif RSA == 20:
            CRW = 0.66
        else:
            CRW = 1
        return CRW

    def calculate_CL(self):
        if L < 90:
            CL = math.sqrt(L / 90)
        else:
            CL = 1
        return CL

    def calculate_C0(self):
        CRW=coefficients().calculate_CRW()
        if 90 < L <= 300:
            C0 = (10.75 -((300 - L) / 100) ** 1.5) * CRW
        elif L < 90:
            C0 = ((L / 25) + 4.1) * CRW
        else:
            C0 = 10.75 * CRW
        return C0

    def calculate_CF(self):
        if self.loc < 0.2:
            CF = 1 + 5 / CB * (0.2 - self.loc)
        elif 0.2 <= self.loc <= 0.7:
            CF = 1
        elif self.loc < 0.7:
            CF = 1 + 20 / CB * (self.loc - 0.7) ** 2
        else:
            CF = 1
        return CF

    def calculate_CD(self):
        if self.loc < 0.2:
            CD = 1.2 - self.loc
        elif 0.2 <= self.loc <= 0.7:
            CD = 1
        elif self.loc < 0.7:
            c = 0.15 * L - 10
            CD = 1 + c / 3 * (self.loc - 0.7)
        else:
            CD = 1
        return CD
    def calculate_CRS(self):
        if RSA == 200:
            CRS = 0.95
        elif RSA == 50:
            CRS = 0.85
        elif RSA == 20:
            CRS = 0.80
        elif RSA==2:
            CRS=0.75
        else:
            CRS = 1
        return CRS

class other_coefficients():
    def __init__(self):
        self.loc=x/L

    def calculate_k(self):
        if ReH < 235:
            k = 235 / ReH
        elif ReH >= 235:
            k = 295 / (ReH + 60)
        return k
    def calculate_nf(self):
        if fs == 1:
            nf = 1
        elif fs == 2:
            nf = 0.83
        else:
            nf = 1
        return nf

    def calculate_GV(self):
        if G == 0 or V == 0:
            x = 0.7
        else:
            x = G / V
        return x

    def calculate_F(self):
        F = 0.11 * V0 / math.sqrt(L)
        return F

    def calculate_m(self):
        F = other_coefficients().calculate_F()
        m0 = 1.5 + F
        if self.loc < 0.2:
            m = m0 - 5 * (m0 - 1) *self.loc
        elif 0.2 <= self.loc <= 0.7:
            m = 1
        elif self.loc < 0.7:
            m = 1 + (m0 + 1) / 0.3 * (self.loc / 0.7)
        else:
            m = 1
        return m

    def calculate_av(self):
        F=other_coefficients().calculate_F()
        m = other_coefficients().calculate_m()
        return F * m


    def calculate_ma(self,l=3): #3.A.4 #MAİN FRAME HESABINDA 9.A.2.1
        l=3 # bunu kesin öğren
        ma=0.204*a/l*(4-(a/l)**2)
        return ma

    def calculate_c(self): #MAİN FRAME HESABINDA 9.A.2.1
        lKu,lKo=0,0   # if no brackets used c = 1
        l=1            # bu l v lKlara bak
        c=1-(lKu/l+0.4*lKo/l)
        if c<0.6:
            c=0.6
        return c

    def calculate_cr(self): #MAİN FRAME HESABINDA 9.A.2.1
        s,l=0,3           # buna da bi bak , for wall sided ships , there is no curvature s/l=0
        cr=1-2*s/l
        if cr<0.75:
            cr=0.75
        return cr
    def calculate_n(self):   #MAİN FRAME HESABINDA 9.A.2.1
        if L<100:
            n=0.9-0.0035*L
        else:
            n=0.55
        return n




class stress_calculations():
    def __init__(self):
        self.k=other_coefficients().calculate_k()
        self.ZLB = self.calculate_ZLB()
        self.Zperm = self.calculate_Zperm()
        self.ZLS=self.calculate_ZLS()

    def calculate_ZLB(self):  # bottom plating
        if L < 90:
            ZLB = 12.6 * math.sqrt(L) / self.k
        else:
            ZLB = 120 / self.k
        return ZLB
    def calculate_Zperm(self):

        if L < 90:
            Zperm = (0.8 + L / 450) * 230 / self.k
        else:
            Zperm = 230 / self.k
        return Zperm


    def calculate_ZPL(self,XL=0):  # bottom plating   XL=0   , # SHELL PLATİNG İÇİN ZPL      XL =55 / self.k
        ZPL = math.sqrt(self.Zperm ** 2 - 3 * XL ** 2) - 0.89 * self.ZLB
        return ZPL

    def calculate_ZLS(self):
        ZLS = 0.76 * self.ZLB # N/mm^2
        return ZLS

    def calculate_ZPLmax(self,XL):   # SHELL PLATİNG
        ZPLmax = math.sqrt((230 / self.k) ** 2 - 3 * XL ** 2) - 0.89 * self.ZLS
        return ZPLmax

class pressure():
    def __init__(self):
        self.GV = other_coefficients().calculate_GV()
        self.C0=coefficients().calculate_C0()
        self.k=other_coefficients().calculate_k()
        self.av=other_coefficients().calculate_av()
        self.CL=coefficients().calculate_CL()
        self.CF=coefficients().calculate_CF()
        self.CD=coefficients().calculate_CD()
        self.P01 = self.calculate_P01()
        self.Pi=self.calculate_Pi()
        self.PC=self.calculate_PC(PC,h)


    def calculate_P0(self,f):
        P0 = 2.1 * (CB + 0.7) * self.C0 * self.CL * f
        return P0

    def calculate_P01(self):
        P01 = 2.6 * (CB + 0.7) * self.CL * self.C0
        return P01

    def calculate_PS(self,z,P0):
        x = (10 * (T - z) + P0 * self.CF * (1 + z / T))  # kN/m^2
        return x

    def calculate_PS1(self,z,y):
        x = (10 * (T - z) + self.P01*(1 + z / T * (2 - z / T)) * 2 * abs(y) / B)
        return x

    def calculate_PB(self,P0):
        x= (10 * T + P0 * self.CF)
        return x

    def calculate_Pi(self):
        hc=7.9  # sil
        return 9.81 * self.GV * hc * (1 + self.av)

    def calculate_P_inner(self):
        hdb=calculations().ha_calculator()/1000
        hc=D-hdb
        Pd = 10 * (T - hdb)  # p damaged
        if vessel_type == 1:
            if self.Pi >= Pd:
                Pinner = self.Pi  # P cargo
            else:
                Pinner = Pd
        elif vessel_type == 2:
            h2 = hc +1 # bu +1 firar borusu yüzünden konuldu
            P2 = 9.81 * h2
            # P1=1   # bunun hesabı haddinden fazla karışık
            if P2 >= Pd:
                Pinner = P2
            else:
                Pinner = Pd
        return Pinner

    def calculate_PD(self,f,z,H,P0):  #SHEER STRAKE HESABINDA
        PD1 = P0 * (20 * T) / ((10 + z - T) * H) * self.CD  # kN/m^2
        PDmin1 = 16 * f
        PDmin2 = 0.7 * P0
        PDlist = [PD1, PDmin1, PDmin2]
        PD = max(PDlist)
        return PD


    def calculate_PC(self,PC,h):
        if PC == 0:
            PC = 7 * h
            if h == 0:
                PC = 15
        else:
            PC = max(PC, 15)  # PC'nin 15'ten küçük olmamasını sağlar
        return PC

    def calculate_PL(self):
        PL = self.PC * (1 + self.av)  # PL Load on cargo decks [kN/m2]
        return PL

    def calculate_Pe(self): # main frames hesabında
        pass                 # aşırı karmaşık eklersin p ya ps ya da pe ye eşit olacak sen ps ye eşitledin şimdilik



def round_t(a):
    decimal = a - int(a)
    if decimal < 0.5:
        if decimal!=0:
            return int(a) + 0.5
    else:
        return int(a) + 1

### SECTION 6-SHELL PLATING / BOTTOM PLATING AND FLAT PLATE KEEL

def bB_calculator(): #6.B.5.1 flat plate keel breadth
    bB = 800 + 5 * L
    return bB




class calculations():
    def __init__(self):
        self.P0=pressure().calculate_P0(1)
        self.PB=pressure().calculate_PB(self.P0)
        self.nf=other_coefficients().calculate_nf()
        self.PB=pressure().calculate_PB(self.P0)
        self.ZPL=stress_calculations().calculate_ZPL(0)
        self.ZPLmax=stress_calculations().calculate_ZPLmax
        self.k=other_coefficients().calculate_k()
        self.tB1 = self.tB_calculator()
        self.tB = round_t(self.tB1)
        self.loc=x/L
        self.hcg = self.hcg_calculator()
        self.ha = self.ha_calculator()
        self.tmcg = round_t(self.tmcg_calculator())
        self.tpf=self.tpf_calculator()
        self.n = other_coefficients().calculate_n()
        self.c = other_coefficients().calculate_c()
        self.cr = other_coefficients().calculate_cr()
        self.ZLB=stress_calculations().calculate_ZLB()
        self.Zperm=stress_calculations().calculate_Zperm()
    def tB_calculator(self):  # 6.B.1 BOTTOM PLATING
        if L >= 90:
            ttB1 = 18.3 * self.nf * a * math.sqrt(self.PB / self.ZPL)
            if ttB1 <= 10:
                tK1 = 1.5
            else:
                tK1 = 0.1 * ttB1 / math.sqrt(self.k)
                if tK1 > 3:
                    tK1 = 3
            tB1 = 18.3 * self.nf * a * math.sqrt(self.PB / self.ZPL) + tK1  # mm
            ttB2 = 1.21 * a * math.sqrt(self.PB * self.k)
            if ttB2 <= 10:
                tK2 = 1.5
            else:
                tK2 = 0.1 * ttB1 / math.sqrt(self.k)
                if tK2 > 3:
                    tK2 = 3
            tB2 = 1.21 * a * math.sqrt(self.PB * self.k) + tK2
            if tB1 <= tB2:
                tB = tB2
            else:
                tB = tB1
        if L < 90:
            ttB1 = 1.9 * self.nf * a * math.sqrt(self.PB * self.k)
            if ttB1 <= 10:
                tk = 1.5
            else:
                tk = 0.1 * ttB1 / math.sqrt(self.k)
                if tk > 3:
                    tk = 3
            tB = 1.9 * self.nf * a * math.sqrt(self.PB * self.k) + tk
        return tB

    def calculate_tFPK(self): #6.B.5.1 flat plate keel thickness
        if 0.75>self.loc>0.15:
            tFPK = self.tB + 2  # mm
        else:
            tFPK=self.tB
        tFKGL = math.sqrt(L * self.k)
        if L >= 50:
            if tFPK <= tFKGL:
                tFPK = tFKGL
        return tFPK

    def hcg_calculator(self): #8.B.2.2 # CENTRE GİRDER #
        lcg = B
        hcg = 350 + 45 * lcg
        if hcg < 600:
            hcg = 600
        return hcg
    def ha_calculator(self): #8.B.2.2 # CENTRE GİRDER #
        if self.hcg % 100 >= 50:
            ha= (self.hcg // 100 + 1) * 100
        else:
            ha= (self.hcg // 100) * 100 + 50
        return ha
    def tmcg_calculator(self): #8.B.2.2 # CENTRE GİRDER #
        if self.ha <= 1200:
            tmcg = self.hcg / self.ha * ((self.hcg / 100) + 1) * math.sqrt(self.k)
        else:
            tmcg = self.hcg / self.ha * ((self.hcg / 120) + 3) * math.sqrt(self.k)
        tmincg = (5 + 0.03 * L) * math.sqrt(self.k)
        if tmcg <= tmincg:
            tmcg = tmincg
        return tmcg

    def number_of_SG(self):  # SIDE GİRDER #8.B.3.1
        if 0 < B / 2 < 4.5:  #"no need for side girders"
            locx1 = []
        elif 4.5 <= B / 2 < 8: #one side girder at each side")
            locx1 = [-B / 4, B / 4]
        elif 8 <= B / 2 <= 10:
            locx1 = [-B / 3, -B / 6, B / 6, B / 3]
        elif B / 2 > 10:
            locx1 = [-3 * B / 8, -B / 4, -B / 8, B / 8, B / 4, 3 * B / 8]
        locx = [round(num, 2) for num in locx1]
        return locx

    def tsg_calculator(self): #8.B.3.1
        tsg = self.hcg ** 2 / (120 * self.ha) * math.sqrt(self.k)
        return tsg


    def tpf_calculator(self):  #PLATE FLOORS  8.B.6.1
        tpf = self.tmcg - 2 * math.sqrt(self.k)
        if tpf > 16:
            tpf = 16
        return tpf

    def tBr_calculator(self):  # BRACKETS  8.B.6.4.1
        tBr = self.tpf
        return tBr
    def bBr_calculator(self):  # BRACKETS  8.B.6.4.1
        bBr = 0.75 * self.hcg
        return bBr

    def tinner_calculator(self): # INNER BOTTOM 8.B.4.1
        P =pressure().calculate_P_inner()
        ttinner = 1.1 * a * math.sqrt(P * self.k)
        if ttinner <= 10:
            tKinner = 1.5
        else:
            tKinner = 0.1 * ttinner / math.sqrt(self.k)
            if tKinner > 3:
                tKinner = 3

        return 1.1 * a * math.sqrt(P * self.k) + tKinner + 2  # hoca ahşap kaplama yoksa +2 gibi bir şey dedi ona bi bakarsın sonra


    def ts_calculator(self): # SHELL PLATİNG #  6.C.1
        hdb = calculations().ha_calculator() / 1000
        z = hdb + a / 2
        y=B/2
        P0=pressure().calculate_P0(1)
        PS = pressure().calculate_PS(z,P0)
        PS1 = pressure().calculate_PS1(z,y)

        if L < 90:
            ts = 1.9 * self.nf * a * math.sqrt(PS * self.k) + self.k
            if L < 50:  # last check for min
                ts1 = (1.5 - 0.01 * L) * math.sqrt(L * self.k)
                if ts <= ts1:
                    ts = ts1
            else:
                ts1 = math.sqrt(L * self.k)
                if ts <= ts1:
                    ts = ts1

        elif L >= 90:

            ttS1 = 18.3 * self.nf * a * math.sqrt(PS / self.ZPL)
            if ttS1 <= 10:
                tKs1 = 1.5
            else:
                tKs1 = 0.1 * ttS1 / math.sqrt(self.k)
                if tKs1 > 3:
                    tKs1 = 3
            ts1 = ttS1 + tKs1
            P = PS  # 4.B.2 DEN P YA PS YE YA DA PE YE EŞİT OLACAK FALAN DİYOR ONU AYARLA
            ttS2 = 1.21 * a * math.sqrt(P * self.k)
            if ttS2 <= 10:
                tKs2 = 1.5
            else:
                tKs2 = 0.1 * ttS2 / math.sqrt(self.k)
                if tKs2 > 3:
                    tKs2 = 3
            ts2 = ttS2 + tKs2

            ttS3 = 18.3 * self.nf * a * math.sqrt(PS1 / (self.ZPLmax(0)))
            if ttS3 <= 10:
                tKs3 = 1.5
            else:
                tKs3 = 0.1 * ttS3 / math.sqrt(self.k)
                if tKs3 > 3:
                    tKs3 = 3
            ts3 = ttS3 + tKs3
            tslist = [ts1, ts2, ts3]
            ts = max(tslist)
            ts11 = math.sqrt(L * self.k)
            if ts11 > ts:
                ts = ts11
        return ts

    def calculate_tD(self):  # DECK PLATİNG      # 7.A.6.1
        z = H = D
        P0=pressure().calculate_P0(1)
        PD = pressure().calculate_PD(1,z,H,P0)
        tFKGL = math.sqrt(L * self.k)
        ttE1 = 1.21 * a * math.sqrt(PD * self.k)
        PL=pressure().calculate_PL()
        if ttE1 <= 10:                              #7.B.1
            tKss = 1.5
        else:
            tKss = 0.1 * ttE1 / math.sqrt(self.k)
            if tKss > 3:
                tKss = 3
        tE1 = 1.21 * a * math.sqrt(PD * self.k) + tKss

        ttE2 = 1.1 * a * math.sqrt(PL * self.k)
        if ttE2 <= 10:
            tKss = 1.5
        else:
            tKss = 0.1 * ttE2 / math.sqrt(self.k)
            if tKss > 3:
                tKss = 3

        tE2 = 1.1 * a * math.sqrt(PL * self.k) + tKss

        tEmin = (5.5 + 0.02 * L) * math.sqrt(self.k)
        tmin = (4.5 + 0.05 * L) * math.sqrt(self.k)
        tcheck = math.sqrt(L * self.k)
        tlist = [tE1, tE2, tEmin, tmin, tcheck]
        tD = max(tlist)
        if tD < tFKGL:
            tD = tFKGL
        return tD

    def calculate_bss(self):  # SHEER STRAKE #
        bss = 800 + 5 * L  # mm     #6.C.3.1
        return bss

    def calculate_tss(self):   #6.C.3.2
        tD = calculations().calculate_tD()
        ts = calculations().ts_calculator()
        tss = 0.5 * (tD + ts)
        if tss < ts:
            tss = ts
        return tss
    def side_f_l(self): # SIDE FRAMES ( HOLD FRAMES ) and SIDE LONGİTUDİNALS  #
        l = (D / 3)
        round_t(l)
        P0 = pressure().calculate_P0(0.75)
        if fs == 2:
            ma = other_coefficients().calculate_ma(l)
            z = l / 2+self.ha_calculator()/1000

            PS = pressure().calculate_PS(z,P0)
            def calculate_WRmf(): #9.A.2.1
                WR = (1 -  ma** 2) * self.n * self.c * a * l ** 2 * PS * self.cr * self.k
                return WR

            Ws_fl = calculate_WRmf()
            print("section modulus for side frame Ws_fl", Ws_fl)

        if fs == 1:
            Zperm=self.Zperm
            ZL = self.ZLB * ((0.4 * D - self.ha_calculator()/1000) / (0.4 * D))
            def calculate_Zpr():
                Zpr = Zperm - abs(ZL)
                return Zpr

            Zpr = calculate_Zpr()
            z = self.ha_calculator()/1000+ a
            PS = pressure().calculate_PS(z,P0)
            m=other_coefficients().calculate_m()
            def calculate_Wl_sl():
                l = e
                Wl_sl = 83 / Zpr * m * a * l ** 2 * PS
                return Wl_sl

            Ws_fl = calculate_Wl_sl()
            print("section modulus for side longitudinal Ws_fl", Ws_fl)
        if fs==2:
            WR=calculate_WRmf()
        elif fs==1:
            WR=calculate_Wl_sl()
        return WR

    def deck_b_l(self): # DECK BEAMS and DECK LONGİTUDİNALS #
        mk = 1  # with no brackets assuption as a first approximation , hesabı baya zorlu
        z = H = D
        P0 = pressure().calculate_P0(1)
        PD = pressure().calculate_PD(1, z, H, P0)
        PL=pressure().calculate_PL()

        P = max(PL, PD)

        if fs == 1:
            def calculate_Wd():
                loc_DG = calculations().number_of_SG() + [0]
                l = B / (len(loc_DG) - 1)
                ma = other_coefficients().calculate_ma(l)
                m = mk ** 2 - ma ** 2
                c = 0.75  # for beams,girders and transverses simply supported on one or both ends , bi tane değeri de c=0.55 ama nedeni yok
                Wd = m * c * a * P * l ** 2 * self.k
                return Wd

            Wd_bl = calculate_Wd()
            print("section modulus for deck beams Wd_bl", Wd_bl)

        if fs == 2:
            ZLD = self.ZLB * ((D - 0.4 * D) / (0.4 * D))
            ZL = ZLD
            Zpr = self.Zperm - abs(ZL)
            l = e
            m=other_coefficients().calculate_m()
            def calculate_Wl_dl():
                Wl_dl = (83 / Zpr) * m * a * l ** 2 * P
                return Wl_dl

            Wd_bl = calculate_Wl_dl()
            print("section modulus for deck longitudinals Wd_bl", Wd_bl)
        if fs == 2:
            W_d= calculate_Wl_dl()
        elif fs == 1:
            W_d = calculate_Wd()
        return W_d

    def calculate_W_dg(self):  # DECK GİRDER
        loc_DG = calculations().number_of_SG() + [0]
        P0=pressure().calculate_P0(0.6)
        z=H=D
        PD = pressure().calculate_PD(0.6,z,H,P0)
        P=PD
        l = 2.4 * 6  # e*6 dedim iki bulkhead arası mesafe
        e = B / (len(loc_DG) + 1)
        W_dg = 0.55 * e * l ** 2 * P * self.k
        return W_dg

    def calculate_W_dt(self):  # DECK TRANSVERSE
        l = B  # if there is no longitudinal bulkhead
        P0 = pressure().calculate_P0(0.6)
        z = H = D
        PD = pressure().calculate_PD(0.6, z, H, P0)
        P = PD
        W_dt = 0.55 * e * l ** 2 * P * self.k  # e distance between deck transverses
        return W_dt


    if fs==1:
        def calculate_Wr_wf(self):  # WEB FRAME # #9.A.5.3.1
            P0 = pressure().calculate_P0(0.6)
            l = D - self.ha_calculator() / 1000
            if l//3==0:
                nc=1    #depends on number of cross ties
            elif l//3==1:
                nc=0.5
            elif l//3==2:
                nc=0.3
            else:
                nc=0.2
            z = self.ha_calculator()/1000 + l / 2
            PS = pressure().calculate_PS(z, P0)
            P=PS
            Wr_wf = 0.55 * e * l ** 2 * P * nc * self.k
            return Wr_wf



        def calculate_Wr_ss(self):
            P0 = pressure().calculate_P0(0.6)
            z = self.ha_calculator()/1000  + 3  # ilk side stringer dibden yüksekliği,ilkinin yüksekliği 3 m olsun
            l=2.4*6 #ikibulkhead arası mesafe , gemi teorisinden onu hesaplayıp eklersin
            if l//2.4==0:
                nc=1    #depends on number of cross ties 2.4 e olacak iki posta arası mesafe
            elif l//2.4==1:
                nc=0.5
            elif l//2.4==2:
                nc=0.3
            else:
                nc=0.2

            if (D-z)<=3:
                locst =(D-z)//2
            elif 3<(D-z)<=6:
                locst=(D-z)//4
            elif 6<=(D-z):
                locst=3/2
            PS = pressure().calculate_PS(z, P0)
            P=PS
            e = 3 / 2 + locst  # buna bi bak anlaşılmadı
            Wr_ss = 0.55 * e * l ** 2 * P * nc * self.k
            return Wr_ss
    if fs==2:
        def calculate_Wr_ST(self):  # side transverse #
            P0 = pressure().calculate_P0(0.6)
            l = D - self.ha_calculator() / 1000
            z = self.ha_calculator()/1000 + l / 2
            PS = pressure().calculate_PS(z, P0)
            P=PS
            Wr_wf = 0.55 * e * l ** 2 * P  * self.k
            return Wr_wf

    if fs == 1:  # bottom and inner bottom frames   8.B.6.3.3
        def calculate_bf(self):
            if len(calculations().number_of_SG()) == 0:
                l = B / 2
            elif len(calculations().number_of_SG()) == 2:
                l = B / 4
            elif len(calculations().number_of_SG()) == 4:
                l = B / 6
            elif len(calculations().number_of_SG()) == 6:
                l = B / 8
            else:
                l = B / 4
            P0 = pressure().calculate_P0(0.75)
            PB = pressure().calculate_PB(P0)
            P = PB

            Wbf = 0.7 * self.c * a * l ** 2 * P * self.k
            return Wbf
        def calculate_W_ibf(self):
            if len(calculations().number_of_SG()) == 0:
                l = B / 2
            elif len(calculations().number_of_SG()) == 2:
                l = B / 4
            elif len(calculations().number_of_SG()) == 4:
                l = B / 6
            elif len(calculations().number_of_SG()) == 6:
                l = B / 8
            else:
                l = B / 4

            Pi=pressure().calculate_P_inner()
            P = Pi
            if  vessel_type == 1:
                Wbf = 0.55 * self.c * a * l ** 2 * P * self.k
            elif vessel_type==2:
                Wbf = 0.44 * self.c * a * l ** 2 * P * self.k
            return Wbf

    if fs==2:  # BOTTOM LONG. ######################
        def calculate_Wl_bl(self):
            P0 = pressure().calculate_P0(0.75)
            PB = pressure().calculate_PB(P0)
            P = PB
            ZL = self.ZLB * ((0.4 * D - self.ha_calculator() / 1000) / (0.4 * D))
            Zpr = self.Zperm - abs(ZL)
            l = e
            mk = 1  # we assumed that there are no brackets
            ma=other_coefficients().calculate_ma()
            m = mk ** 2 -ma ** 2
            Wl_bl=83/Zpr*m*a*l**2*P
            return Wl_bl

        def calculate_Wl_ibl(self): # İNNER BOTTOM LONG . #######################
            Pi = pressure().calculate_P_inner()
            P = Pi
            ZL = self.ZLB * ((0.4 * D - self.ha_calculator() / 1000) / (0.4 * D))
            Zpr = self.Zperm - abs(ZL)
            l = e
            mk = 1  # we assumed that there are no brackets
            ma = other_coefficients().calculate_ma()
            m = mk ** 2 - ma ** 2
            Wl = 83 / Zpr * m * a * l ** 2 * e * P
            return Wl


bB = bB_calculator()
print(f" breadth of flat plate keel bB: {bB} ")

tB=calculations().tB
print(f"bottom plating thickness tB: {tB} ")
tFPK =calculations().calculate_tFPK()
print(f"flat plate keel thickness tFK {tFPK}")


hcg = calculations().hcg_calculator()
print(f"height of centre girder hcg : {hcg}")
ha=calculations().ha_calculator()
print(f"actual height of centre girder ha : {ha}")
tmcg = calculations().tmcg
print("thickness of centre girder tmcg", tmcg)


tsg1 = calculations().tsg_calculator()
tsg = round_t(tsg1)
print("the thickness of side girder tsg", tsg)
loc_SG = calculations().number_of_SG()
print(f"the distance of side girders from centerline {loc_SG}")


tpf =calculations().tpf_calculator()
print(f"the thickness of plate floor tpf", tpf)


bBr = calculations().bBr_calculator()
print("the breadth of brackets bBr", bBr)
tBr = calculations().tBr_calculator()
print("The thickness of brackets tBr", tBr)


tinner =round_t(calculations().tinner_calculator())
print("the thickenss of inner bottom tinner: ", tinner)


ts =calculations().ts_calculator()
print("the thickness of shell plate ts", ts)


tD = calculations().calculate_tD()
print("thickness of deck plating tD: ", tD)

tss = calculations().calculate_tss()
print("thickness of sheer strake tss: ", tss)
bss =calculations().calculate_bss()
print("breadth of sheer strake bss:", bss)

print(calculations().side_f_l())
print(calculations().deck_b_l())

W_dg = calculations().calculate_W_dg()
print("section modulus of deck girder W_dg", W_dg)

W_dt = calculations().calculate_W_dt()
print("section modulus of deck transverse W_dt", W_dt)
if fs==1:
    Wr_wf = calculations().calculate_Wr_wf()
    print("section modulus of web frame Wr_wf", Wr_wf)

    Wr_ss = calculations().calculate_Wr_ss()
    print("section modulus of side stringer Wr_ss", Wr_ss)

    W_bf = calculations().calculate_bf()
    print("section modulus of bottom frame W_bf", W_bf)

    W_ibf = calculations().calculate_W_ibf()
    print("section modulus of inner bottom frame W_ibf", W_ibf)
elif fs==2:
    Wr_ST=calculations().calculate_Wr_ST()
    print("section modulus of side transverse wr_ST",Wr_ST)

    Wl_bl = calculations().calculate_Wl_bl()
    print("section modulus of bottom longitudinal Wl_bl", Wl_bl)

    Wl_ibl = calculations().calculate_Wl_ibl()
    print("section modulus of inner bottom longitudinal Wl_bl", Wl_ibl)




"""
def manhole_calculator():
    LLq = input("is there any bulkhead in your ship? press 1 or 2     1) yes    2) no )")
    if LLq == "1":
        LL = int(input("what is the span between longitudinal bulkheads in meters?"))
    else:
        LL = B
    ymax = 0.4 * LL
    y_manhole = int(input(f"what is the distance between supporting point of the plate floor (ship's side, longitudinal bulkhead) in meters?\
note that The distance y is not to be taken greater than {ymax} : "))
    Ɛ = int(input("what kind of space you are checking for manhole? ( press 1 or 2 )\
1) for spaces which may be empty at full draught, e.g. machinery spaces, storerooms, etc.\
2) elsewhere "))
    if Ɛ == 1:
        Ɛ = 0.5
    else:
        Ɛ = 0.3
    Aw = Ɛ * T * LL * e * (1 - 2 * y_manhole / LL) * k

    rwsa = ha * tpf / 100
    Amh = rwsa - 40 * tpf / 10
    if Amh >= Aw:
        print("a man hole may be opened")
        mh = 1
    else:
        print("you shouldnt open a man hole")
        mh = 2
    return mh


manhole = input("Do you want to check if you want to open manholes? Press 1 or 2    1)yes   2)no) ")
if manhole == "1":
    man_hole = manhole_calculator()
"""

















