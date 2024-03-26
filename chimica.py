from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size=(1250, 600)
Window.minimum_width, Window.minimum_height = (700,350)
elemento = []
elementi = [
    [ 'Idrogeno'    , 'H' , 1.008 , 1  , ],
    [ 'Elio'        , 'He', 4.003 , 2  , ],
    [ 'Litio'       , 'Li', 6.941 , 3  , ],
    [ 'Berillio'    , 'Be', 9.012 , 4  , ],
    [ 'Boro'        , 'B' , 10.81 , 5  , ],
    [ 'Carbonio'    , 'C' , 12.01 , 6  , ],
    [ 'Azoto'       , 'N' , 14.01 , 7  , ],
    [ 'Ossigeno'    , 'O' , 16.00 , 8  , ],
    [ 'Flurio'      , 'F' , 19.00 , 9  , ],
    [ 'Neon'        , 'Ne', 20.18 , 10 , ],
    [ 'Sodio'       , 'Na', 22.99 , 11 , ],
    [ 'Magnesio'    , 'Mg', 24.31 , 12 , ],
    [ 'Alluminio'   , 'Al', 26.98 , 13 , ],
    [ 'Silicio'     , 'Si', 28.09 , 14 , ],
    [ 'Fosforo'     , 'P' , 30.97 , 15 , ],
    [ 'Zolfo'       , 'S' , 32.07 , 16 , ],
    [ 'Cloro'       , 'Cl', 35.45 , 17 , ],
    [ 'Argon'       , 'Ar', 39.95 , 18 , ],
    [ 'Potassio'    , 'K' , 39.10 , 19 , ],
    [ 'Calcio'      , 'Ca', 40.08 , 20 , ],
    [ 'Scandio'     , 'Sc', 44.96 , 21 , ],
    [ 'Titanio'     , 'Ti', 47.87 , 22 , ],
    [ 'Vanadio'     , 'V' , 50.94 , 23 , ], 
    [ 'Cromo'       , 'Cr', 52.00 , 24 , ], 
    [ 'Manganese'   , 'Mn', 54.94 , 25 , ],
    [ 'Ferro'       , 'Fe', 55.85 , 26 , ],
    [ 'Colbato'     , 'Co', 58.93 , 27 , ], 
    [ 'Nichel'      , 'Ni', 58.69 , 28 , ],
    [ 'Rame'        , 'Cu', 63.55 , 29 , ],
    [ 'Zinco'       , 'Zn', 65.38 , 30 , ],
    [ 'Gallio'      , 'Ga', 69.72 , 31 , ],
    [ 'Germanio'    , 'Ge', 72.63 , 32 , ],
    [ 'Arsenico'    , 'As', 74.92 , 33 , ],
    [ 'Selenio'     , 'Se', 78.96 , 34 , ],
    [ 'Bromo'       , 'Br', 79.90 , 35 , ],
    [ 'Krypton'     , 'Kr', 83.80 , 36 , ],
    [ 'Rubidio'     , 'Rb', 84.47 , 37 , ],
    [ 'Stronzio'    , 'Sr', 87.62 , 38 , ],
    [ 'Ittrio'      , 'Y' , 88.91 , 39 , ],
    [ 'Zirconio'    , 'Zr', 91.22 , 40 , ],
    [ 'Niobio'      , 'Nb', 92.91 , 41 , ],
    [ 'Molibdeno'   , 'Mo', 95.95 , 42 , ],
    [ 'Tecnezio'    , 'Tc', 98.91 , 43 , ],
    [ 'Rutenio'     , 'Ru', 101.1 , 44 , ],
    [ 'Rodio'       , 'Rh', 102.9 , 45 , ],
    [ 'Palladio'    , 'Pd', 106.4 , 46 , ],
    [ 'Argento'     , 'Ag', 107.9 , 47 , ],
    [ 'Camdio'      , 'Cd', 112.4 , 48 , ],
    [ 'Indio'       , 'In', 114.8 , 49 , ],
    [ 'Stagno'      , 'Sn', 118.7 , 50 , ],
    [ 'Amtimonio'   , 'Sb', 121.8 , 51 , ],
    [ 'Tellurio'    , 'Te', 127.6 , 52 , ],
    [ 'Iodio'       , 'I' , 126.9 , 53 , ],
    [ 'Xenon'       , 'Xe', 131.3 , 54 , ],
    [ 'Cesio'       , 'Cs', 132.9 , 55 , ],
    [ 'Bario'       , 'Ba', 137.3 , 56 , ],
    [ 'Lantanio'    , 'La', 138.9 , 57 , ],
    [ 'Cerio'       , 'Ce', 140   , 58 , ],
    [ 'Praseodimio' , 'Pr', 141   , 59 , ],
    [ 'Neodimio'    , 'Nd', 144   , 60 , ],
    [ 'Promezio'    , 'Pm', 145   , 61 , ],
    [ 'Samario'     , 'Sm', 150   , 62 , ],
    [ 'Europio'     , 'Eu', 152   , 63 , ],
    [ 'Gadolinio'   , 'Gd', 157   , 64 , ],
    [ 'Terbio'      , 'Tb', 159   , 65 , ],
    [ 'Disprosio'   , 'Dy', 163   , 66 , ],
    [ 'Olmio'       , 'Ho', 165   , 67 , ],
    [ 'Erbio'       , 'Er', 167   , 68 , ],
    [ 'Tullio'      , 'Tm', 169   , 69 , ],
    [ 'Itterbio'    , 'Yb', 173   , 70 , ],
    [ 'Lutezio'     , 'Lu', 175   , 71 , ],
    [ 'Afino'       , 'Hf', 178.49, 72 , ],
    [ 'Tantalio'    , 'Ta', 180.95, 73 , ],
    [ 'Tungsteno'   , 'W' , 183.84, 74 , ],
    [ 'Renio'       , 'Re', 186.2 , 75 , ],
    [ 'Osmio'       , 'Os', 190.2 , 76 , ],
    [ 'Iridio'      , 'Ir', 192.2 , 77 , ],
    [ 'Platio'      , 'Pt', 195.1 , 78 , ],
    [ 'Oro'         , 'Au', 196.9 , 79 , ],
    [ 'Mercurio'    , 'Hg', 201.0 , 80 , ],
    [ 'Tallio'      , 'Tl', 204.3 , 81 , ],
    [ 'Piombo'      , 'Pb', 207.2 , 82 , ],
    [ 'Bismuto'     , 'Bi', 209.0 , 83 , ],
    [ 'Polonio'     , 'Po', 209   , 84 , ],
    [ 'Astato'      , 'At', 210   , 85 , ],
    [ 'Radon'       , 'Rn', 222   , 86 , ],
    [ 'Francio'     , 'Fr', 223.02, 87 , ],
    [ 'Radio'       , 'Ra', 226.03, 88 , ],
    [ 'Attinio'     , 'Ac', 88.91 , 89 , ],
    [ 'Torio'       , 'Th', 232   , 90 , ],
    [ 'Protoattinio', 'Pa', 209   , 91 , ],
    [ 'Uranio'      , 'U' , 238   , 92 , ],
    [ 'Nettunio'    , 'Np', 237   , 93 , ],
    [ 'Plutonio'    , 'Pu', 244   , 94 , ],
    [ 'Americio'    , 'Am', 243   , 95 , ],
    [ 'Curio'       , 'Cm', 247   , 96 , ],
    [ 'Berkelio'    , 'Bk', 247   , 97 , ],
    [ 'Californio'  , 'Cf', 247   , 98 , ],
    [ 'Einstenio'   , 'Es', 252   , 99 , ],
    [ 'Fermio'      , 'Fm', 257   , 100, ],
    [ 'Mendelevio'  , 'Md', 258   , 101, ],
    [ 'Nobelio'     , 'No', 259   , 102, ],
    [ 'Luarenzio'   , 'Lr', 260   , 103, ],
    [ 'Rutherfordio', 'Rf', 261   , 104, ],
    [ 'Dubnio'      , 'Db', 262   , 105, ],
    [ 'Seaborgio'   , 'Sg', 266   , 106, ],
    [ 'Bohrio'      , 'Bh', 264   , 107, ],
    [ 'Hassio'      , 'Hs', '--'  , 108, ],
    [ 'Meitnerio'   , 'Mt', 268   , 109, ],
    [ 'Darmstadtio' , 'Ds', 271   , 110, ],
    [ 'Roentgenio'  , 'Rg', 272   , 111, ],
    [ 'Copernicio'  , 'Cn', 285   , 102, ],
    [ 'Nihonio'     , 'Nh', '--'  , 113, ],
    [ 'Flreovio'    , 'Fl', '--'  , 114, ],
    [ 'Moscovio'    , 'Mc', '--'  , 115, ],
    [ 'Livermorio'  , 'Lv', '--'  , 116, ],
    [ 'Tennesso'    , 'Ts', '--'  , 117, ],
    [ 'Oganesson'   , 'Og', '--'  , 118, ]
]

class TavolaPeriodica(Screen):
    def color_change(self, idd):
        self.ids.layout.background_color = self.ids[idd].background_color
        self.ids.Simbolo.text = self.ids[idd].text
        for elemento in elementi:
            if idd == elemento[1]:
                indx = elementi.index(elemento)
        self.ids.NumeroAtomico.text = str(elementi[indx][3])
        self.ids.Nome.text = elementi[indx][0]
        self.ids.MassaAtomica.text = str(elementi[indx][2]) if type(elementi[indx][2]) != 'str' else elementi[indx][2]     

Builder.load_string("""
<Elementi@Button>:
    bold: True
    font_size: root.width/2.5
    background_normal: ''
    color: 0 , 0 , 0 , 1

<Numeri@Label>:
    bold: True
    font_size: root.width/2

<Belementi@BoxLayout>:
    spacing: 4

<TavolaPeriodica>:
    rows: 1
    padding: 20
    spacing: 20
    Belementi:
        orientation: 'horizontal'
        padding: 20
        BoxLayout:
            id: layout
            size_hint_x: .25
            orientation: 'vertical'
            size_hint_y: .7
            pos_hint: {'x': 0, 'center_y': .55}
            spacing: 0
            background_color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: self.background_color
                Rectangle:
                    size: self.size
                    pos: self.pos
            Label:
                id: NumeroAtomico
                text:'1'
                size_hint_y: .1
                bold: True
                color: 0,0,0,1
                font_size: (root.width/3+root.height)/2/14
            Label:
                id: Simbolo
                text:'H'
                size_hint_y: .2
                bold: True
                color: 0,0,0,1
                background_color: 0,0,0,1
                font_size: (root.width/5+root.height)/2/3
            Label:
                id: Nome
                text:'Idrogeno'
                size_hint_y: .1
                bold: True
                color: 0,0,0,1
                font_size:  (root.width+root.height)/2/20
            
            Label:
                id: MassaAtomica
                text:'1.008'
                size_hint_y: .1
                pos_hint: {'x_left': 0, 'y': 0}
                bold: True
                color: 0,0,0,1
                font_size:  (root.width/3+root.height)/2/14
            
        Belementi:
            size_hint_x: .75
            orientation: 'vertical'
            Belementi:
                Numeri:
                    text: '1'
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Numeri:
                    text: '18'
            Belementi:
                Elementi:
                    id: H
                    text: "H"
                    background_color: '#00FF00'
                    on_press: root.color_change(self.text)
                Numeri:
                    text: '2'
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Numeri:
                    text: '13'
                Numeri:
                    text: '14'
                Numeri:
                    text: '15'
                Numeri:
                    text: '16'
                Numeri:
                    text: '17'
                Elementi:
                    id: He
                    text: "He"
                    background_color: '#DC6786'
                    on_press: root.color_change(self.text)
            Belementi:
                Elementi:
                    id: Li
                    text: "Li"
                    background_color: '#FF0000'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Be
                    text: "Be"
                    background_color: '#FF6400'
                    on_press: root.color_change(self.text)
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Label:
                    text: ''
                Elementi:
                    id: B
                    text: 'B'
                    background_color: '#FDCF0B'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: C
                    text: 'C'
                    background_color: '#00FF00'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: N
                    text: 'N'
                    background_color: '#00FF00'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: O
                    text: 'O'
                    background_color: '#00FF00'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: F
                    text: 'F'
                    background_color: '#FFFFFF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ne
                    text: 'Ne'
                    background_color: '#DC6786'
                    on_press: root.color_change(self.text)
            Belementi:
                Elementi:
                    id: Na
                    text: 'Na'
                    background_color: '#FF0000'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Mg
                    text: 'Mg'
                    background_color: '#FF6400'
                    on_press: root.color_change(self.text)
                Numeri:
                    text: '3'
                Numeri:
                    text: '4'
                Numeri:
                    text: '5'
                Numeri:
                    text: '6'
                Numeri:
                    text: '7'
                Numeri:
                    text: '8'
                Numeri:
                    text: '9'
                Numeri:
                    text: '10'
                Numeri:
                    text: '11'
                Numeri:
                    text: '12'
                Elementi:
                    id: Al
                    text: 'Al'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Si
                    text: 'Si'
                    background_color: '#FDCF0B'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: P
                    text: 'P'
                    background_color: '#00FF00'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: S
                    text: 'S'
                    background_color: '#00FF00'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Cl
                    text: 'Cl'
                    background_color: '#FFFFFF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ar
                    text: 'Ar'
                    background_color: '#DC6786'
                    on_press: root.color_change(self.text)
            Belementi:
                Elementi:
                    id: K
                    text: 'K'
                    background_color: '#FF0000'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ca
                    text: 'Ca'
                    background_color: '#FF6400'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Sc
                    text: 'Sc'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ti
                    text: 'Ti'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: V
                    text: 'V'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Cr
                    text: 'Cr'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Mn
                    text: 'Mn'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Fe
                    text: 'Fe'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Co
                    text: 'Co'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ni
                    text: 'Ni'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Cu
                    text: 'Cu'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Zn
                    text: 'Zn'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ga
                    text: 'Ga'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ge
                    text: 'Ge'
                    background_color: '#FDCF0B'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: As
                    text: 'As'
                    background_color: '#FDCF0B'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Se
                    text: 'Se'
                    background_color: '#00FF00'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Br
                    text: 'Br'
                    background_color: '#FFFFFF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Kr
                    text: 'Kr'
                    background_color: '#DC6786'
                    on_press: root.color_change(self.text)
            Belementi:
                Elementi:
                    id: Rb
                    text: 'Rb'
                    background_color: '#FF0000'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Sr
                    text: 'Sr'
                    background_color: '#FF6400'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Y
                    text: 'Y'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Zr
                    text: 'Zr'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Nb
                    text: 'Nb'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Mo
                    text: 'Mo'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Tc
                    text: 'Tc'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ru
                    text: 'Ru'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Rh
                    text: 'Rh'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Pd
                    text: 'Pd'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ag
                    text: 'Ag'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Cd
                    text: 'Cd'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: In
                    text: 'In'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Sn
                    text: 'Sn'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Sb
                    text: 'Sb'
                    background_color: '#FDCF0B'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Te
                    text: 'Te'
                    background_color: '#FDCF0B'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: I
                    text: 'I'
                    background_color: '#FFFFFF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Xe
                    text: 'Xe'
                    background_color: '#DC6786'
                    on_press: root.color_change(self.text)
            Belementi:
                Elementi:
                    id: Cs
                    text: 'Cs'
                    background_color: '#FF0000'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ba
                    text: 'Ba'
                    background_color: '#FF6400'
                    on_press: root.color_change(self.text)
                Label:
                    text: ''
                Elementi:
                    id: Hf
                    text: 'Hf'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ta
                    text: 'Ta'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: W
                    text: 'W'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Re
                    text: 'Re'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Os
                    text: 'Os'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ir
                    text: 'Ir'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Pt
                    text: 'Pt'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Au
                    text: 'Au'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Hg
                    text: 'Hg'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ti
                    text: 'Ti'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Pb
                    text: 'Pb'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Bi
                    text: 'Bi'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Po
                    text: 'Po'
                    background_color: '#FDCF0B'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: At
                    text: 'At'
                    background_color: '#FFFFFF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Rn
                    text: 'Rn'
                    background_color: '#DC6786'
                    on_press: root.color_change(self.text)
            Belementi:
                Elementi:
                    id: Fr
                    text: 'Fr'
                    background_color: '#FF0000'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ra
                    text: 'Ra'
                    background_color: '#FF6400'
                    on_press: root.color_change(self.text)
                Label:
                    text: ''
                Elementi:
                    id: Rf
                    text: 'Rf'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Db
                    text: 'Db'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Sg
                    text: 'Sg'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Bh
                    text: 'Bh'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Hs
                    text: 'Hs'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Mt
                    text: 'Mt'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ds
                    text: 'Ds'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Rg
                    text: 'Rg'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Cn
                    text: 'Cn'
                    background_color: '#41B3FF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Nh
                    text: 'Nh'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Fl
                    text: 'Fl'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Mc
                    text: 'Mc'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Lv
                    text: 'Lv'
                    background_color: '#C500DD'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ts
                    text: 'Ts'
                    background_color: '#FFFFFF'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Og
                    text: 'Og'
                    background_color: '#DC6786'
                    on_press: root.color_change(self.text)
            Belementi:
                Label:
                    text: ''
                Label:
                    text: ''
                Elementi:
                    id: La
                    text: 'La'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ce
                    text: 'Ce'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Pr
                    text: 'Pr'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Nd
                    text: 'Nd'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Pm
                    text: 'Pm'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Sm
                    text: 'Sm'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Eu
                    text: 'Eu'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Gd
                    text: 'Gd'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Tb
                    text: 'Tb'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Dy
                    text: 'Dy'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Ho
                    text: 'Ho'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Er
                    text: 'Er'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Tm
                    text: 'Tm'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Yb
                    text: 'Yb'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Lu
                    text: 'Lu'
                    background_color: '#0047B4'
                    on_press: root.color_change(self.text)
                Label:
                    text: ''
            Belementi:
                Label:
                    text: ''
                Label:
                    text: ''
                Elementi:
                    id: Ac
                    text: 'Ac'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Th
                    text: 'Th'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Pa
                    text: 'Pa'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: U
                    text: 'U'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Np
                    text: 'Np'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Pu
                    text: 'Pu'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Am
                    text: 'Am'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Cm
                    text: 'Cm'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Bk
                    text: 'Bk'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Cf
                    text: 'Cf'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Es
                    text: 'Es'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Fm
                    text: 'Fm'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Md
                    text: 'Md'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: No
                    text: 'No'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Elementi:
                    id: Lr
                    text: 'Lr'
                    background_color: '#00FF50'
                    on_press: root.color_change(self.text)
                Label:
                    text: ''
""")

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TavolaPeriodica(name= 'main'))
        return sm
    
MyApp().run()
