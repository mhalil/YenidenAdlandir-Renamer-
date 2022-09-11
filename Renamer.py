#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Sep 04, 2022 03:43:19 PM +03  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Renamer_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("750x700+485+173")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title(".: Renamer :.")
        top.configure(highlightcolor="black")

        self.top = top
        self.SiraliArtir = tk.IntVar()
        self.OnEk = tk.IntVar()
        self.SonEk = tk.IntVar()
        self.KarakterSil = tk.IntVar()
        self.Degistir = tk.IntVar()
        self.Radio = tk.IntVar()        # Bunu ben ekledim. 
        # self.KucukHarf = tk.IntVar()
        # self.BuyukHarf = tk.IntVar()
        # self.BasHarflerBuyuk = tk.IntVar()
        # self.HarfleriTersCevir = tk.IntVar()
        # self.ismiTersCevir = tk.IntVar()

        self.Onizleme_ekrani = tk.LabelFrame(self.top)
        self.Onizleme_ekrani.place(relx=0.52, rely=0.017, relheight=0.571
                , relwidth=0.468)
        self.Onizleme_ekrani.configure(relief='groove')
        self.Onizleme_ekrani.configure(text='''Yeni İsim Önizleme Ekranı''')

        self.onizle_text = ScrolledText(self.Onizleme_ekrani)
        self.onizle_text.place(relx=0.028, rely=0.145, relheight=0.825
                , relwidth=0.946, bordermode='ignore')
        self.onizle_text.configure(background="white")
        self.onizle_text.configure(font="TkTextFont")
        self.onizle_text.configure(insertborderwidth="3")
        self.onizle_text.configure(selectbackground="blue")
        self.onizle_text.configure(selectforeground="white")
        self.onizle_text.configure(wrap="none")

        self.Etiket_onizleme_ekrani = tk.Label(self.Onizleme_ekrani)
        self.Etiket_onizleme_ekrani.place(relx=0.04, rely=0.063, height=21
                , width=319, bordermode='ignore')
        self.Etiket_onizleme_ekrani.configure(anchor='w')
        self.Etiket_onizleme_ekrani.configure(compound='left')
        self.Etiket_onizleme_ekrani.configure(text='''Adlandırılacak Dosyaların Önizleme Ekranı:''')

        self.Etiket_dosya_sec = tk.LabelFrame(self.top)
        self.Etiket_dosya_sec.place(relx=0.013, rely=0.014, relheight=0.571
                , relwidth=0.467)
        self.Etiket_dosya_sec.configure(relief='groove')
        self.Etiket_dosya_sec.configure(text='''İsimlendirilecek Dosyaları Seçin''')

        self.girdi_text = ScrolledText(self.Etiket_dosya_sec)
        self.girdi_text.place(relx=0.029, rely=0.15, relheight=0.825
                , relwidth=0.949, bordermode='ignore')
        self.girdi_text.configure(background="white")
        self.girdi_text.configure(font="TkTextFont")
        self.girdi_text.configure(insertborderwidth="3")
        self.girdi_text.configure(selectbackground="blue")
        self.girdi_text.configure(selectforeground="white")
        self.girdi_text.configure(wrap="none")

        self.Buton_cikar = tk.Button(self.Etiket_dosya_sec)
        self.Buton_cikar.place(relx=0.509, rely=0.058, height=33, width=165
                , bordermode='ignore')
        self.Buton_cikar.configure(borderwidth="2")
        self.Buton_cikar.configure(command=Renamer_support.cikar)
        self.Buton_cikar.configure(compound='left')
        self.Buton_cikar.configure(text='''Çıkar''')

        self.Buton_ekle = tk.Button(self.Etiket_dosya_sec)
        self.Buton_ekle.place(relx=0.029, rely=0.058, height=33, width=165
                , bordermode='ignore')
        self.Buton_ekle.configure(borderwidth="2")
        self.Buton_ekle.configure(command=Renamer_support.ekle)
        self.Buton_ekle.configure(compound='left')
        self.Buton_ekle.configure(text='''Ekle...''')

        self.Buton_onizle = tk.Button(self.top)
        self.Buton_onizle.place(relx=0.52, rely=0.886, height=65, width=165)
        self.Buton_onizle.configure(activebackground="#f9f9f9")
        self.Buton_onizle.configure(borderwidth="2")
        self.Buton_onizle.configure(command=Renamer_support.Buton_onizle)
        self.Buton_onizle.configure(compound='left')
        self.Buton_onizle.configure(text='''Önizle''')

        self.YerineKoyulacakYazi = tk.Entry(self.top)
        self.YerineKoyulacakYazi.place(relx=0.253, rely=0.871, height=33
                , relwidth=0.227)
        self.YerineKoyulacakYazi.configure(background="white")
        self.YerineKoyulacakYazi.configure(font="TkFixedFont")
        self.YerineKoyulacakYazi.configure(selectbackground="blue")
        self.YerineKoyulacakYazi.configure(selectforeground="white")
        self.YerineKoyulacakYazi.configure(state='disabled')

        self.Etiket_degistirilecek_deger = tk.Label(self.top)
        self.Etiket_degistirilecek_deger.place(relx=0.027, rely=0.879, height=21, width=153)
        self.Etiket_degistirilecek_deger.configure(activebackground="#f9f9f9")
        self.Etiket_degistirilecek_deger.configure(anchor='w')
        self.Etiket_degistirilecek_deger.configure(compound='left')
        self.Etiket_degistirilecek_deger.configure(text='''Değiştirilecek Değer :''')

        self.uygula = tk.Button(self.top)
        self.uygula.place(relx=0.76, rely=0.886, height=65, width=165)
        self.uygula.configure(activebackground="#f9f9f9")
        self.uygula.configure(borderwidth="2")
        self.uygula.configure(command=Renamer_support.Uygula)
        self.uygula.configure(compound='left')
        self.uygula.configure(text='''Uygula''')

        self.OnEkYaz = tk.Entry(self.top)
        self.OnEkYaz.place(relx=0.173, rely=0.607, height=33, relwidth=0.307)
        self.OnEkYaz.configure(background="white")
        self.OnEkYaz.configure(font="TkFixedFont")
        self.OnEkYaz.configure(selectbackground="blue")
        self.OnEkYaz.configure(selectforeground="white")
        self.OnEkYaz.configure(state='disabled')

        self.SonEkYaz = tk.Entry(self.top)
        self.SonEkYaz.place(relx=0.173, rely=0.664, height=33, relwidth=0.307)
        self.SonEkYaz.configure(background="white")
        self.SonEkYaz.configure(font="TkFixedFont")
        self.SonEkYaz.configure(selectbackground="blue")
        self.SonEkYaz.configure(selectforeground="white")
        self.SonEkYaz.configure(state='disabled')

        self.Baslangic_Deger_Etiket = tk.Label(self.top)
        self.Baslangic_Deger_Etiket.place(relx=0.16, rely=0.729, height=23, width=128)
        self.Baslangic_Deger_Etiket.configure(activebackground="#f9f9f9")
        self.Baslangic_Deger_Etiket.configure(anchor='w')
        self.Baslangic_Deger_Etiket.configure(compound='left')
        self.Baslangic_Deger_Etiket.configure(text='''Başlangıç Değeri:''')

        self.Sirali_artir = tk.Checkbutton(self.top)
        self.Sirali_artir.place(relx=0.013, rely=0.729, relheight=0.033
                , relwidth=0.143)
        self.Sirali_artir.configure(activebackground="#f9f9f9")
        self.Sirali_artir.configure(anchor='w')
        self.Sirali_artir.configure(compound='left')
        self.Sirali_artir.configure(justify='left')
        self.Sirali_artir.configure(text='''Sıralı Artır''')
        self.Sirali_artir.configure(variable=self.SiraliArtir)
        self.Sirali_artir.configure(command=Renamer_support.SiraliArtir)
        self.Sirali_artir.configure(onvalue=1) 
        self.Sirali_artir.configure(offvalue=0)


        self.BaslDegerYaz = tk.Entry(self.top)
        self.BaslDegerYaz.place(relx=0.333, rely=0.721, height=33
                , relwidth=0.147)
        self.BaslDegerYaz.configure(background="white")
        self.BaslDegerYaz.configure(font="TkFixedFont")
        self.BaslDegerYaz.configure(selectbackground="blue")
        self.BaslDegerYaz.configure(selectforeground="white")
        self.BaslDegerYaz.configure(state='disabled')

        self.OnEkEkle = tk.Checkbutton(self.top)
        self.OnEkEkle.place(relx=0.013, rely=0.614, relheight=0.033
                , relwidth=0.143)
        self.OnEkEkle.configure(activebackground="#f9f9f9")
        self.OnEkEkle.configure(anchor='w')
        self.OnEkEkle.configure(compound='left')
        self.OnEkEkle.configure(justify='left')
        self.OnEkEkle.configure(text='''Ön Ek Ekle :''')
        self.OnEkEkle.configure(variable=self.OnEk)
        self.OnEkEkle.configure(command=Renamer_support.OnEkEkle) 
        self.OnEkEkle.configure(onvalue=1) 
        self.OnEkEkle.configure(offvalue=0)

        self.SonEkEkle = tk.Checkbutton(self.top)
        self.SonEkEkle.place(relx=0.013, rely=0.671, relheight=0.033
                , relwidth=0.156)
        self.SonEkEkle.configure(activebackground="#f9f9f9")
        self.SonEkEkle.configure(anchor='w')
        self.SonEkEkle.configure(compound='left')
        self.SonEkEkle.configure(justify='left')
        self.SonEkEkle.configure(text='''Son Ek Ekle :''')
        self.SonEkEkle.configure(variable=self.SonEk)
        self.SonEkEkle.configure(command=Renamer_support.SonEkEkle) 
        self.SonEkEkle.configure(onvalue=1) 
        self.SonEkEkle.configure(offvalue=0)

        self.KarakterKelimeSil = tk.Checkbutton(self.top)
        self.KarakterKelimeSil.place(relx=0.013, rely=0.786, relheight=0.033
                , relwidth=0.236)
        self.KarakterKelimeSil.configure(activebackground="#f9f9f9")
        self.KarakterKelimeSil.configure(anchor='w')
        self.KarakterKelimeSil.configure(compound='left')
        self.KarakterKelimeSil.configure(justify='left')
        self.KarakterKelimeSil.configure(text='''Karakter / Kelime Sil :''')
        self.KarakterKelimeSil.configure(variable=self.KarakterSil)
        self.KarakterKelimeSil.configure(command=Renamer_support.KarakterKelimeSil) 
        self.KarakterKelimeSil.configure(onvalue=1) 
        self.KarakterKelimeSil.configure(offvalue=0)


        self.SilYaz = tk.Entry(self.top)
        self.SilYaz.place(relx=0.253, rely=0.779, height=33, relwidth=0.227)
        self.SilYaz.configure(background="white")
        self.SilYaz.configure(font="TkFixedFont")
        self.SilYaz.configure(selectbackground="blue")
        self.SilYaz.configure(selectforeground="white")
        self.SilYaz.configure(state='disabled')

        self.DegistirYerineKoy = tk.Checkbutton(self.top)
        self.DegistirYerineKoy.place(relx=0.013, rely=0.836, relheight=0.033
                , relwidth=0.236)
        self.DegistirYerineKoy.configure(activebackground="#f9f9f9")
        self.DegistirYerineKoy.configure(anchor='w')
        self.DegistirYerineKoy.configure(compound='left')
        self.DegistirYerineKoy.configure(justify='left')
        self.DegistirYerineKoy.configure(text='''Değiştir / Yerine Koy''')
        self.DegistirYerineKoy.configure(variable=self.Degistir)
        self.DegistirYerineKoy.configure(command=Renamer_support.DegistirYerineKoy) 
        self.DegistirYerineKoy.configure(onvalue=1) 
        self.DegistirYerineKoy.configure(offvalue=0)

        self.Etiket_yerine_koyulacak_deger = tk.Label(self.top)
        self.Etiket_yerine_koyulacak_deger.place(relx=0.027, rely=0.936, height=21, width=174)
        self.Etiket_yerine_koyulacak_deger.configure(activebackground="#f9f9f9")
        self.Etiket_yerine_koyulacak_deger.configure(anchor='w')
        self.Etiket_yerine_koyulacak_deger.configure(compound='left')
        self.Etiket_yerine_koyulacak_deger.configure(text='''Yerine Koyulacak Değer :''')

        self.DegistirilecekYazi = tk.Entry(self.top)
        self.DegistirilecekYazi.place(relx=0.253, rely=0.929, height=33
                , relwidth=0.227)
        self.DegistirilecekYazi.configure(background="white")
        self.DegistirilecekYazi.configure(font="TkFixedFont")
        self.DegistirilecekYazi.configure(selectbackground="blue")
        self.DegistirilecekYazi.configure(selectforeground="white")
        self.DegistirilecekYazi.configure(state='disabled')

        self.RadioButon_kucuk = tk.Radiobutton(self.top)
        self.RadioButon_kucuk.place(relx=0.507, rely=0.607, relheight=0.033
                , relwidth=0.185)
        self.RadioButon_kucuk.configure(activebackground="#f9f9f9")
        self.RadioButon_kucuk.configure(anchor='w')
        self.RadioButon_kucuk.configure(compound='left')
        self.RadioButon_kucuk.configure(justify='left')
        self.RadioButon_kucuk.configure(text='''küçük harf''')
        self.RadioButon_kucuk.configure(variable=self.Radio)
        self.RadioButon_kucuk.configure(command=Renamer_support.KucukHarf)
        self.RadioButon_kucuk.configure(value=1)

        self.RadioButon_buyuk = tk.Radiobutton(self.top)
        self.RadioButon_buyuk.place(relx=0.507, rely=0.664, relheight=0.033
                , relwidth=0.185)
        self.RadioButon_buyuk.configure(activebackground="#f9f9f9")
        self.RadioButon_buyuk.configure(anchor='w')
        self.RadioButon_buyuk.configure(compound='left')
        self.RadioButon_buyuk.configure(justify='left')
        self.RadioButon_buyuk.configure(text='''BÜYÜK HARF''')
        self.RadioButon_buyuk.configure(variable=self.Radio)
        self.RadioButon_buyuk.configure(command=Renamer_support.BuyukHarf)
        self.RadioButon_buyuk.configure(value=2)
        

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.RadioButon_kelime_basharf_buyuk = tk.Radiobutton(self.top)
        self.RadioButon_kelime_basharf_buyuk.place(relx=0.507, rely=0.721, relheight=0.033
                , relwidth=0.4)
        self.RadioButon_kelime_basharf_buyuk.configure(activebackground="#f9f9f9")
        self.RadioButon_kelime_basharf_buyuk.configure(anchor='w')
        self.RadioButon_kelime_basharf_buyuk.configure(compound='left')
        self.RadioButon_kelime_basharf_buyuk.configure(justify='left')
        self.RadioButon_kelime_basharf_buyuk.configure(text='''Kelimelerin Baş Harfleri Büyük''')
        self.RadioButon_kelime_basharf_buyuk.configure(variable=self.Radio)
        self.RadioButon_kelime_basharf_buyuk.configure(command=Renamer_support.BasHarfBuyuk)
        self.RadioButon_kelime_basharf_buyuk.configure(value=3)

        self.RadioButon_harfler_ters = tk.Radiobutton(self.top)
        self.RadioButon_harfler_ters.place(relx=0.507, rely=0.779, relheight=0.033
                , relwidth=0.4)
        self.RadioButon_harfler_ters.configure(activebackground="#f9f9f9")
        self.RadioButon_harfler_ters.configure(anchor='w')
        self.RadioButon_harfler_ters.configure(compound='left')
        self.RadioButon_harfler_ters.configure(justify='left')
        self.RadioButon_harfler_ters.configure(text='''hARFLERİ tERS çEVİR''')
        self.RadioButon_harfler_ters.configure(variable=self.Radio)
        self.RadioButon_harfler_ters.configure(command=Renamer_support.TersHarf)
        self.RadioButon_harfler_ters.configure(value=4)        

        self.RadioButon_ters = tk.Radiobutton(self.top)
        self.RadioButon_ters.place(relx=0.507, rely=0.829, relheight=0.033
                , relwidth=0.4)
        self.RadioButon_ters.configure(activebackground="#f9f9f9")
        self.RadioButon_ters.configure(anchor='w')
        self.RadioButon_ters.configure(compound='left')
        self.RadioButon_ters.configure(justify='left')
        self.RadioButon_ters.configure(text='''İsmi ters çevir ( riveç sret imsi )''')
        self.RadioButon_ters.configure(variable=self.Radio)
        self.RadioButon_ters.configure(command=Renamer_support.TersIsim)
        self.RadioButon_ters.configure(value=5)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    Renamer_support.main()

if __name__ == '__main__':
    Renamer_support.main()




