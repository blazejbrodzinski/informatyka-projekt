#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Eksperyemnt został zaprojektowany w builderze
grupa: Błażej Brodziński, Aleksandra Kędziora, Aleksandra Maziarka



This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on September 16, 2022, at 19:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import paczek ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
import sys

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Start wszystkich powiązanych plików  z tego samego folderu co plik kodu
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# informacje o eksperymencie
psychopyVersion = '2022.2.4'
expName = 'stroop_projekt'
expInfo = {
    'session': '001',
    'participant': '',
}
# --- okno dialogowe z informacjami o uczestniku ---
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName) #funkcja do tworzenia okna dialogowego
if dlg.OK == False: #dlg.OK -- print(info)
    core.quit()  # jeżeli naciśnie się 'escape'
expInfo['date'] = data.getDateStr()  # dodawanie daty
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Nazwa pliku z danymi = ścieżka + nazwa + .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# kod, który pomaga w zapiswyaniu danych
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\blaze\\Desktop\\final1\\stroop_projekt.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)

endExpNow = False  # wyjście z eksperymentu (jak się da True to się odrazu wyłącza)
frameTolerance = 0.001  #tolerancja czasu trwania klatki w sekundach - ustawione domyślnie

# TUTAJ WŁĄCZA SIĘ KOD PO ZNIKNIĘCIU OKNA DIALOGOWEGO

# --- Ustawienia okna, w którym wyświetla się eksperyment ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
#ustawienie widocznosci kursora
win.mouseVisible = False  
# przechowywanie liczby klatek na sekundę jeżeli da się to zmierzyć
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # jeżeli nie może zmierzyć daje wartość 60
# --- Ustawienia urządzeń wejścia  ---
ioConfig = {}

# Setup iohub dla klawiatury
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

defaultKeyboard = keyboard.Keyboard(backend='iohub')


# SEKCJA ODPOWIADAJĄCA ZA TWORZENIE ELEMENTÓW POTRZEBNYCH  DLA KAŻDEJ PROCEDURY (listy,słownika,textboxy), które będą używane później

# ten kod nie odpowiada jeszcze za samo działanie danej treści

# --- tworzenie elementów dla procedury "niezgodne" (tworzenie list dla bodźców niezgodnych) ---

b_niezgodne = []
kolor1 = []
zgodnosc1 = []
poprawnaOdp1 = []
jezyk1 = []

# --- tworzenie elementów dla procedury "zgodne" (tworzenie list dla bodźców zgodnych)---

b_zgodne =[]
kolor2 = []
zgodnosc2 = []
poprawnaOdp2 = []
jezyk2 = []

# --- tworzenie elementów dla procedury"neutralne" (tworzenie list dla bodźców neutralnych) ---

b_neutralne = []
kolor3 = []
zgodnosc3 = []
poprawnaOdp3 = []
jezyk3 = []

# --- tworzenie elementów dla procedury "mikser" ---
import random

# # --- tworzenie elementów dla procedury "INSTRUKCJA"  ---
textbox_instrukcja = visual.TextBox2(
     win, text='INSTRUKCJA WYKONANIA ZADANIA\nZadanie opierać się będzie na wskazywaniu za pomocą odpowiednich klawiszy, koloru w\njakim wyświetlany jest napis po polsku i po angielsku. Znaczenie słowa powinno zostać\npominięte.\nKolor czcionki słowa wyświetlanego należy wybierać za pomocą klucza podanego poniżej\n\nA” – dla czcionki CZARNEJ\n„S” – dla czcionki BRĄZOWEJ\n„K” – dla czcionki FIOLETOWEJ\n„L” – dla czcionki RÓŻOWEJ\n\nprzykład poprawnego rozwiązania zadania\nJeżeli na ekranie wyświetli się słowo BROWN w kolorze różowym\nwciśnij klawisz “L”\nJeżeli wyświetli się BRĄZ w kolorze brązowym “S”\nPomiędzy słowami oznaczającymi kolory będzie wyświetlany również bodziec w postaci\nsłowa o znaczeniu neutralnym, w tym przypadku naciśnij klawisz zgodny z kolorem czcionki\nPostaraj się rozwiązać zadanie poprawnie i jak najszybciej, dokonywany będzie\npomiar czasu Twoich reakcji.\nPrzed rozpoczęciem badania, zostaniesz przeprowadzony przez trening, który umożliwi Ci\nzapoznanie się z odpowiednimi klawiszami. W tej sesji będą również wyświetlane twoje\nodpowiedzi po każdym naciśnięciu klawisza. W sesji eksperymentalnej nie będziesz\ninformowany o poprawności swoich odpowiedzi.\nJeżeli zapoznałeś się z instrukcja, możesz przejść dalej klikając spację.', font='Open Sans',
     pos=(0, 0),     letterHeight=0.03,
     size=(1.3 , 0.82), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textbox_instrukcja',
     autoLog=False,
)
key_resp_instrukcja = keyboard.Keyboard()

# --- tworzenie elementów dla procedury "text_Trening " ---
text_trening = visual.TextStim(win=win, name='text_trening',
    text='TRENING',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_GetReady = visual.TextStim(win=win, name='text_GetReady',
    text='Zadanie zaraz się rozpocznie.\nWskazujący i środkowy palec lewej ręki umieść na klawiszach “A” i “S”\nWskazujący i środkowy palec prawej ręki umieść na klawiszach “K” i “L”\nSkup uwagę na środku ekranu, patrząc na punkt “+”\nUdzielaj odpowiedzi możliwie jak najszybciej\nPo zniknięciu wyrazu nadal będziesz miał 5 sekund na udzielenie odpowiedzi\nJeżeli jesteś gotowy\nnaciśnij spację',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0)
ready = keyboard.Keyboard()

# --- tworzenie elementów dla procedury "fixation (w treningu) " ---
polygon_cross = visual.ShapeStim(
    win=win, name='polygon_cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=0.0, interpolate=True)

# --- tworzenie elementów dla procedury "stroop"( w  treningu)   ---
element_listy = -1

text_Slowo = visual.TextStim(win=win, name='text_Slowo',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_stroop = keyboard.Keyboard()
textbox_ASKL = visual.TextBox2(
     win, text='"A" - czarny    "S" - brązowy   "K" - fioletowy   "L" - różowy', font='Open Sans',
     pos=(0,-0.65),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=0.8,
     padding=0.0, alignment='center',
     anchor='bottom-center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textbox_ASKL',
     autoLog=False,)

# --- tworzenie elementów dla procedury "feedback" (w treningu) ---
text_feedback = visual.TextStim(win=win, name='text_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_wait800 = visual.TextStim(win=win, name='text_wait800',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- tworzenie elementów dla procedury "PRZERWA" (w treningu) ---
text_przerwa = visual.TextStim(win=win, name='text_przerwa',
    text='PRZERWA',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Przerwa = keyboard.Keyboard()

# --- tworzenie elementów dla procedury "eksperyment" (tekst przed sesją eksperyemtalną) ---
text_eksperyment = visual.TextStim(win=win, name='text_eksperyment',
    text='SESJA EKSPERYMENTALNA',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)
text_GetReady2 = visual.TextStim(win=win, name='text_GetReady2',
    text='Zadanie zaraz się rozpocznie.\nWskazujący i środkowy palec lewej ręki umieść na klawiszach “A” i “S”\nWskazujący i środkowy palec prawej ręki umieść na klawiszach “K” i “L”\nSkup uwagę na środku ekranu, patrząc na punkt “+”\nUdzielaj odpowiedzi możliwie jak najszybciej\nPo zniknięciu wyrazu nadal będziesz miał 5 sekund na udzielenie odpowiedzi\nJeżeli jesteś gotowy\nnaciśnij spację',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0)
key_resp_ready2 = keyboard.Keyboard()

# --- tworzenie elementów dla procedury "fixation" (w sesji eksperymentalnej) ---
polygon_cross = visual.ShapeStim(
    win=win, name='polygon_cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=0.0, interpolate=True)

# --- tworzenie elementów dla procedury "stroop2" (w sesji eksperymentalnej) ---
text_Slowo2 = visual.TextStim(win=win, name='text_Slowo2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_stroop2 = keyboard.Keyboard()
textbox_ASKL2 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0,-0.65),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=0.8,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textbox_ASKL2',
     autoLog=False,)

# --- tworzenie elementów dla procedury "PRZERWA" (w sesji eksperymentalnej) ---
text_przerwa = visual.TextStim(win=win, name='text_przerwa',
    text='PRZERWA',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Przerwa = keyboard.Keyboard()

# --- tworzenie elementów dla procedury "koniec" (na zakończenie sesji eksperymetnalne) ---
text_koniec = visual.TextStim(win=win, name='text_koniec',
    text='To koniec zadania.\nDziękujemy za udział w badaniu',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# tworzenie  zegarów (pobocznych)
globalClock = core.Clock()  #mierzenie czasu od rozpoczęcia eksperyemtnu
routineTimer = core.Clock()  # mierzenie czasu podczas każdej z procedru


#SEKCJA ODPOWIADAJĄCA ZA DZIAŁANIE KAŻDEJ Z PROCEDURY

#PROCEDURA NIEZGODNE, ZGODNE i NEUTRALNE

# Randomizacja NIEZGODNYCH bodźców

trials_niezgodne = data.TrialHandler(nReps=1.0, method='random', #data.trialHandler - funkcja do sekwencjonowania prób i przechowywania danych.
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bniezgodne_zmienione.xlsx'),
    seed=None, name='trials_niezgodne')
thisExp.addLoop(trials_niezgodne)  # dodawnie pętli do eksperymetnu
thisTrials_niezgodne = trials_niezgodne.trialList[0] # możliwość zainicjowania bodźców z pewnymi wartościami

if thisTrials_niezgodne != None:
    for paramName in thisTrials_niezgodne:
        exec('{} = thisTrials_niezgodne[paramName]'.format(paramName))

for thisTrials_niezgodne in trials_niezgodne:
    currentLoop = trials_niezgodne

    if thisTrials_niezgodne != None:
        for paramName in thisTrials_niezgodne:
            exec('{} = thisTrials_niezgodne[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "niezgodne" --- 
    continueRoutine = True
    routineForceEnded = False
#dodawanie do listy bodzcow neizgodnych wartości
    b_niezgodne.append(word)
    kolor1.append(kolor)
    zgodnosc1.append(zgodnosc)
    poprawnaOdp1.append(poprawnaOdp)
    jezyk1.append(jezyk)
    
    

    # śledzenie które komponenty zostały ukończone
    niezgodneComponents = []
    for thisComponent in niezgodneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # resetowanie liczników czasu
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "niezgodne" --- przeprowadzanie procedury "niezgodne"
    while continueRoutine:
        # pobieranie aktualnego czasu
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
        # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        # sprawdzanie czy wszystkie komponenty się zakończyły
        if not continueRoutine:
            routineForceEnded = True
            break
        continueRoutine = False # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
        for thisComponent in niezgodneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        # odświeżenie ekranu
        if continueRoutine:
            win.flip()
    #  kończenie procedury niezgodne
    for thisComponent in niezgodneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    routineTimer.reset()
    thisExp.nextEntry()
# pobieranie nazw parametrów bodźców
if trials_niezgodne.trialList in ([], [None], None):
    params = []
else:
    params = trials_niezgodne.trialList[0].keys()
# zapisywanie danych z tej pętli (niezgodne)
trials_niezgodne.saveAsExcel(filename + '.xlsx', sheetName='trials_niezgodne',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
    
#PROCEDURA ZGODNE

# randomizacja
trials_zgodne = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bzgodne_zmienione.xlsx'),
    seed=None, name='trials_zgodne')
thisExp.addLoop(trials_zgodne)   # dodanie pętli
thisTrials_zgodne = trials_zgodne.trialList[0]  # możliwość zainicjowania bodźców z pewnymi wartościami

if thisTrials_zgodne != None:
    for paramName in thisTrials_zgodne:
        exec('{} = thisTrials_zgodne[paramName]'.format(paramName))

for thisTrials_zgodne in trials_zgodne:
    currentLoop = trials_zgodne

    if thisTrials_zgodne != None:
        for paramName in thisTrials_zgodne:
            exec('{} = thisTrials_zgodne[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "zgodne" --- #dodawanie do listy bodzcow zgodnych wartości
    continueRoutine = True
    routineForceEnded = False

    b_zgodne.append(word)
    kolor2.append(kolor)
    zgodnosc2.append(zgodnosc)
    poprawnaOdp2.append(poprawnaOdp)
    jezyk2.append(jezyk)
    
    
    
      # śledzenie które komponenty zostały ukończone
    zgodneComponents = []
    for thisComponent in zgodneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # resetowanie liczników czasu
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    #  przeprowadzenie procedury zgodne
    while continueRoutine:
         # pobieranie aktualnego czasu
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)

        # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # sprawdzanie czy wszystkie komponenty się zakończyły
        if not continueRoutine:  # komponent wymaga zakończenia procedury
            routineForceEnded = True
            break
        continueRoutine = False  #  (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
        for thisComponent in zgodneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
                #hasatrr jest True jezeli dany obiekt ma okreslony atrybut jezeli status != finish to kontunuj routine
        
        # odświeżenie ekranu
        if continueRoutine:
            win.flip()
    
    # --- Ending Routine "zgodne" ---
    
    for thisComponent in zgodneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # resetowanie non slip timer (?)
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_zgodne'

# pobieranie nazw parametrów bodźców
if trials_zgodne.trialList in ([], [None], None):
    params = []
else:
    params = trials_zgodne.trialList[0].keys()
# zapisywanie danych z tej pętli
trials_zgodne.saveAsExcel(filename + '.xlsx', sheetName='trials_zgodne',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# randomizacja NEUTRALNE
trials_neutral = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Bneutralne_zmienione.xlsx'),
    seed=None, name='trials_neutral')
thisExp.addLoop(trials_neutral)  # dodawanie pętli do eksperymentu
thisTrials_neutral = trials_neutral.trialList[0]  # możliwość zainicjowania bodźców z pewnymi wartościami

if thisTrials_neutral != None:
    for paramName in thisTrials_neutral:
        exec('{} = thisTrials_neutral[paramName]'.format(paramName))

for thisTrials_neutral in trials_neutral:
    currentLoop = trials_neutral
    if thisTrials_neutral != None:
        for paramName in thisTrials_neutral:
            exec('{} = thisTrials_neutral[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "neutralne" ---
    continueRoutine = True
    routineForceEnded = False

    # Run 'Begin Routine' code from code_neutral
    b_neutralne.append(word)
    kolor3.append(kolor)
    zgodnosc3.append(zgodnosc)
    poprawnaOdp3.append(poprawnaOdp)
    jezyk3.append(jezyk)
    pula_neutralnych = list(zip(b_neutralne, kolor3, zgodnosc3, poprawnaOdp3, jezyk3))
    
    
    losowe_neutralne = random.choices(pula_neutralnych, k=3)

    # śledzenie które komponenty zostały ukończone
    neutralneComponents = []
    for thisComponent in neutralneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # resetowanie liczników czasu
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "neutralne" ---
    while continueRoutine:
        # pobieranie aktualnego czasu
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)

        
        # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # sprawdzanie czy wszystkie komponenty się zakończyły
        if not continueRoutine:  #komponent wymaga zakończenia procedury
            routineForceEnded = True
            break
        continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
        for thisComponent in neutralneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
        
        # odświeżenie ekranu
        if continueRoutine:
            win.flip()
    
    # --- Ending Routine "neutralne" ---
    for thisComponent in neutralneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # resetowanie non-slip timer?
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_neutral'

# pobieranie nazw parametrów bodźców
if trials_neutral.trialList in ([], [None], None):
    params = []
else:
    params = trials_neutral.trialList[0].keys()
# zapisywanie danych z tej pętli
trials_neutral.saveAsExcel(filename + '.xlsx', sheetName='trials_neutral',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "mikser" --- mieszanie tych wszystkich bodźców
continueRoutine = True
routineForceEnded = False

# Run 'Begin Routine' 
#tworzenie iteracji krotek przez list() i zip(), potem randomizacja krotek
pula_niezgodnych = list(zip(b_niezgodne, kolor1, zgodnosc1, poprawnaOdp1, jezyk1))
losowe_niezgodne = random.choices(pula_niezgodnych, k=8)

pula_zgodnych = list(zip(b_zgodne, kolor2, zgodnosc2, poprawnaOdp2, jezyk2))
losowe_zgodne = random.choices(pula_zgodnych, k=8)

pula_neutralnych = list(zip(b_neutralne, kolor3, zgodnosc3, poprawnaOdp3,jezyk3))
losowe_neutralne = random.choices(pula_neutralnych, k=4)


losowo_wybrane_bodzce = losowe_niezgodne + losowe_zgodne + losowe_neutralne
shuffle(losowo_wybrane_bodzce)

losowo_wybrane_slowo = [x[0] for x in losowo_wybrane_bodzce]
losowo_wybrany_kolor = [x[1] for x in losowo_wybrane_bodzce]
czy_jest_zgodne = [x[2] for x in losowo_wybrane_bodzce]
co_klikac = [x[3] for x in losowo_wybrane_bodzce]
wybrany_jezyk = [x[4] for x in losowo_wybrane_bodzce]
# śledzenie które komponenty zostały ukończone
mikserComponents = []
for thisComponent in mikserComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# resetowanie liczników czasu
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "mikser" ---
while continueRoutine:
    #  pobieranie aktualnego czasu
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)

    # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # sprawdzanie czy wszystkie komponenty się zakończyły
    if not continueRoutine:  #komponent wymaga zakończenia procedury
        routineForceEnded = True
        break
    continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
    for thisComponent in mikserComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
    
    # odświeżenie ekranu
    if continueRoutine:
        win.flip()

# --- Ending Routine "mikser" ---
for thisComponent in mikserComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#resetowanie non slip timer (?)
routineTimer.reset()


# --- Prepare to start Routine "INSTRUKCJA" ---
continueRoutine = True
routineForceEnded = False
 #aktualizowanie parametrów komponentu dla każdego powtórzenia
textbox_instrukcja.reset()
key_resp_instrukcja.keys = []
key_resp_instrukcja.rt = []
_key_resp_instrukcja_allKeys = []
# śledzenie które komponenty zostały ukończone
INSTRUKCJAComponents = [textbox_instrukcja, key_resp_instrukcja]
for thisComponent in INSTRUKCJAComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# resetowanie liczników czasu
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "INSTRUKCJA" ---
while continueRoutine:
    # pobieranie aktualnego czasu
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)

    
    # *textbox_instrukcja* updates
    if textbox_instrukcja.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        #śledzenie czasu rozpoczęcia
        textbox_instrukcja.frameNStart = frameN  # dokładny frame index
        textbox_instrukcja.tStart = t  #  local time, który nie liczy się do odświeżania ekranu
        textbox_instrukcja.tStartRefresh = tThisFlipGlobal  #według global time
        win.timeOnFlip(textbox_instrukcja, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        textbox_instrukcja.setAutoDraw(True)
    
    # *key_resp_instrukcja* updates
    if key_resp_instrukcja.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # śledzenie czasu rozpoczęcia
        key_resp_instrukcja.frameNStart = frameN  # dokładny frame index
        key_resp_instrukcja.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        key_resp_instrukcja.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(key_resp_instrukcja, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        key_resp_instrukcja.status = STARTED
        # rozpocznięcie sprawdzania klawiatury
        key_resp_instrukcja.clock.reset()  # teraz t=0
    if key_resp_instrukcja.status == STARTED:
        theseKeys = key_resp_instrukcja.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_instrukcja_allKeys.extend(theseKeys)
        if len(_key_resp_instrukcja_allKeys):
            key_resp_instrukcja.keys = _key_resp_instrukcja_allKeys[-1].name  # jedynie ostatni kliknięty przycisk
            key_resp_instrukcja.rt = _key_resp_instrukcja_allKeys[-1].rt
            # odpowiedź kończy procedurę
            continueRoutine = False
    
    # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # sprawdzanie czy wszystkie komponenty się zakończyły
    if not continueRoutine:  #komponent wymaga zakończenia procedury
        routineForceEnded = True
        break
    continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
    for thisComponent in INSTRUKCJAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
    
    # odświeżenie ekranu
    if continueRoutine:
        win.flip()

# --- Ending Routine "INSTRUKCJA" ---
for thisComponent in INSTRUKCJAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#resetowanie non slip timer (?)
routineTimer.reset()
routineTimer.reset()

# --- Prepare to start Routine "text_Trening" ---
continueRoutine = True
routineForceEnded = False
# aktualizowanie parametrów komponentu dla każdego powtórzenia
ready.keys = []
ready.rt = []
_ready_allKeys = []
# skladniki w text_Trening
text_TreningComponents = [text_trening, text_GetReady, ready]
for thisComponent in text_TreningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# resetowanie liczników czasu
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "text_Trening" ---
while continueRoutine:
    # pobieranie aktualnego czasu
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)

    
    # *text_trening* updates
    if text_trening.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # śledzenie czasu rozpoczęcia
        text_trening.frameNStart = frameN  # dokładny frame index
        text_trening.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        text_trening.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(text_trening, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        text_trening.setAutoDraw(True)
    if text_trening.status == STARTED:
        # # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
        if tThisFlipGlobal > text_trening.tStartRefresh + 2.0 - frameTolerance:
            #śledzenie czasu zatrzymania klatki
            text_trening.tStop = t  # nie liczy się do odświeżania ekranu
            text_trening.frameNStop = frameN  # dokładny frame index
            text_trening.setAutoDraw(False)    
    # *text_GetReady* updates
    if text_GetReady.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # śledzenie czasu rozpoczęcia
        text_GetReady.frameNStart = frameN  # dokładny frame index
        text_GetReady.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        text_GetReady.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(text_GetReady, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        text_GetReady.setAutoDraw(True)    
    # *ready* updates
    if ready.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # śledzenie czasu rozpoczęcia
        ready.frameNStart = frameN  # dokładny frame index
        ready.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        ready.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(ready, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        ready.status = STARTED
        # rozpocznięcie sprawdzania klawiatury
        ready.clock.reset()  # teraz t=0
    if ready.status == STARTED:
        theseKeys = ready.getKeys(keyList=['space'], waitRelease=False)
        _ready_allKeys.extend(theseKeys)
        if len(_ready_allKeys):
            ready.keys = _ready_allKeys[-1].name  # jedynie ostatni kliknięty przycisk
            ready.rt = _ready_allKeys[-1].rt
            # odpowiedź kończy procedurę
            continueRoutine = False
    
    # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # sprawdzanie czy wszystkie komponenty się zakończyły
    if not continueRoutine:  #komponent wymaga zakończenia procedury
        routineForceEnded = True
        break
    continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
    for thisComponent in text_TreningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
    
    # odświeżenie ekranu
    if continueRoutine:
        win.flip()

# --- Ending Routine "text_Trening" ---
for thisComponent in text_TreningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#resetowanie non slip timer (?)routineTimer.reset()
routineTimer.reset()
# randomizacja
s_treningowa = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='s_treningowa')
thisExp.addLoop(s_treningowa)  # dodawnie pętli do eksperymetnu
thisS_treningowa = s_treningowa.trialList[0]  # możliwość zainicjowania bodźców z pewnymi wartościami

if thisS_treningowa != None:
    for paramName in thisS_treningowa:
        exec('{} = thisS_treningowa[paramName]'.format(paramName))

for thisS_treningowa in s_treningowa:
    currentLoop = s_treningowa

    if thisS_treningowa != None:
        for paramName in thisS_treningowa:
            exec('{} = thisS_treningowa[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # śledzenie które komponenty zostały ukończone
    fixationComponents = [polygon_cross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # resetowanie liczników czasu
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # pobieranie aktualnego czasu
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
        
        # *polygon_cross* updates
        if polygon_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # śledzenie czasu rozpoczęcia
            polygon_cross.frameNStart = frameN  # dokładny frame index
            polygon_cross.tStart = t  # local time, który nie liczy się do odświeżania ekranu
            polygon_cross.tStartRefresh = tThisFlipGlobal  # według global time
            win.timeOnFlip(polygon_cross, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
            polygon_cross.setAutoDraw(True)
        if polygon_cross.status == STARTED:
            # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
            if tThisFlipGlobal > polygon_cross.tStartRefresh + 0.5-frameTolerance:
                # śledzenie czasu zatrzymania klatki
                polygon_cross.tStop = t  # nie liczy się do odświeżania ekranu
                polygon_cross.frameNStop = frameN  # dokładny frame index
                polygon_cross.setAutoDraw(False)
        
        # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # sprawdzanie czy wszystkie komponenty się zakończyły
        if not continueRoutine:  #komponent wymaga zakończenia procedury
            routineForceEnded = True
            break
        continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)        
        # odświeżenie ekranu
        if continueRoutine:
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #  używano non-slip timer więc należy odjąć oczekiwany czas tej procedury
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "stroop" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code_Stroop
    element_listy += 1
    #zmienne do wciśnięcia w okienka z tekstem i kolorem
    pokazywane_slowo = losowo_wybrane_slowo[element_listy]
    pokazywany_kolor = losowo_wybrany_kolor[element_listy]
    kliknij_to = co_klikac[element_listy]
    zgodny_czy_nie = czy_jest_zgodne[element_listy]
    jaki_jezyk = wybrany_jezyk[element_listy]
    
    text_Slowo.setColor(pokazywany_kolor, colorSpace='rgb')
    text_Slowo.setText(pokazywane_slowo)
    key_resp_stroop.keys = []
    key_resp_stroop.rt = []
    _key_resp_stroop_allKeys = []
    textbox_ASKL.reset()
    # śledzenie które komponenty zostały ukończone
    stroopComponents = [text_Slowo, key_resp_stroop, textbox_ASKL]
    for thisComponent in stroopComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # resetowanie liczników czasu
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "stroop" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # pobieranie aktualnego czasu
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
        
        # *text_Slowo* updates
        if text_Slowo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # śledzenie czasu rozpoczęcia
            text_Slowo.frameNStart = frameN  # dokładny frame index
            text_Slowo.tStart = t  # local time, który nie liczy się do odświeżania ekranu
            text_Slowo.tStartRefresh = tThisFlipGlobal  # według global time
            win.timeOnFlip(text_Slowo, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
            text_Slowo.setAutoDraw(True)
        if text_Slowo.status == STARTED:
            # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
            if tThisFlipGlobal > text_Slowo.tStartRefresh + 0.5-frameTolerance:
                # śledzenie czasu zatrzymania klatki
                text_Slowo.tStop = t  # nie liczy się do odświeżania ekranu
                text_Slowo.frameNStop = frameN  # dokładny frame index
                text_Slowo.setAutoDraw(False)
        
        # *key_resp_stroop* updates
        waitOnFlip = False
        if key_resp_stroop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # śledzenie czasu rozpoczęcia
            key_resp_stroop.frameNStart = frameN  # dokładny frame index
            key_resp_stroop.tStart = t  # local time, który nie liczy się do odświeżania ekranu
            key_resp_stroop.tStartRefresh = tThisFlipGlobal  # według global time
            win.timeOnFlip(key_resp_stroop, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
            key_resp_stroop.status = STARTED
            # rozpocznięcie sprawdzania klawiatury
            waitOnFlip = True
            win.callOnFlip(key_resp_stroop.clock.reset)  #  t=0 przy następnym przerzuceniu ekranu (screen flip)
            win.callOnFlip(key_resp_stroop.clearEvents, eventType='keyboard')  #  czyszczenie wydarzeń przy następnym przerzuceniu ekranu (screen flip)
        if key_resp_stroop.status == STARTED:
            # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
            if tThisFlipGlobal > key_resp_stroop.tStartRefresh + 5.0-frameTolerance:
                # śledzenie czasu zatrzymania klatki
                key_resp_stroop.tStop = t  # nie liczy się do odświeżania ekranu
                key_resp_stroop.frameNStop = frameN  # dokładny frame index
                key_resp_stroop.status = FINISHED
        if key_resp_stroop.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_stroop.getKeys(keyList=['a', 's', 'k', 'l'], waitRelease=False)
            _key_resp_stroop_allKeys.extend(theseKeys)
            if len(_key_resp_stroop_allKeys):
                key_resp_stroop.keys = _key_resp_stroop_allKeys[-1].name  # jedynie ostatni kliknięty przycisk
                key_resp_stroop.rt = _key_resp_stroop_allKeys[-1].rt
                # sprawdzanie czy to było poprawne
                if (key_resp_stroop.keys == str(kliknij_to)) or (key_resp_stroop.keys == kliknij_to):
                    key_resp_stroop.corr = 1
                else:
                    key_resp_stroop.corr = 0
                # odpowiedź kończy procedurę
                continueRoutine = False
        # *textbox_ASKL* updates
        if textbox_ASKL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # śledzenie czasu rozpoczęcia
            textbox_ASKL.frameNStart = frameN  # dokładny frame index
            textbox_ASKL.tStart = t  # local time, który nie liczy się do odświeżania ekranu
            textbox_ASKL.tStartRefresh = tThisFlipGlobal  # według global time
            win.timeOnFlip(textbox_ASKL, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
            textbox_ASKL.setAutoDraw(True)
        if textbox_ASKL.status == STARTED:
            # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
            if tThisFlipGlobal > textbox_ASKL.tStartRefresh + 5.0-frameTolerance:
                # śledzenie czasu zatrzymania klatki
                textbox_ASKL.tStop = t  # nie liczy się do odświeżania ekranu
                textbox_ASKL.frameNStop = frameN  # dokładny frame index
                textbox_ASKL.setAutoDraw(False)        
        # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        # sprawdzanie czy wszystkie komponenty się zakończyły
        if not continueRoutine:  #komponent wymaga zakończenia procedury
            routineForceEnded = True
            break
        continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
        for thisComponent in stroopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
        
        # odświeżenie ekranu
        if continueRoutine:
            win.flip()
    
    # --- Ending Routine "stroop" ---
    for thisComponent in stroopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_Stroop
    if key_resp_stroop.keys == kliknij_to:
        czypoprawna = 'dobrze'
    else:
        czypoprawna = 'źle' 
    #dodawanie danych do zebrania
    s_treningowa.addData('pokazywane_slowo', pokazywane_slowo)
    s_treningowa.addData('jaki_jezyk', jaki_jezyk)
    s_treningowa.addData('zgodny_czy_nie',zgodny_czy_nie)
    # sprwadzanie odpowiedzi
    if key_resp_stroop.keys in ['', [], None]:  # nie udzielono odpowiedzi
        key_resp_stroop.keys = None
        #  sprwadzanie czy nie udzielono odpowiedzi było poprawne (bez sensu bo nie ma takiego warunku w tym eksperymencie)
        if str(kliknij_to).lower() == 'none':
           key_resp_stroop.corr = 1;  # poprawna była brak odpowiedzi
        else:
           key_resp_stroop.corr = 0;  # zła odpowiedź
    # PRZECHOWYWANIE DANYCH DLA s_treningowa (TrialHandler)
    s_treningowa.addData('key_resp_stroop.keys',key_resp_stroop.keys)
    s_treningowa.addData('key_resp_stroop.corr', key_resp_stroop.corr)
    if key_resp_stroop.keys != None:  # mamy odpowiedź
        s_treningowa.addData('key_resp_stroop.rt', key_resp_stroop.rt)
    #używano non-slip timer więc należy odjąć oczekiwany czas tej procedury
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code_feedback
    if key_resp_stroop.keys == kliknij_to:
        czypoprawna = 'dobrze'
    else:
        czypoprawna = 'źle'
    text_feedback.setText(czypoprawna)
    # śledzenie które komponenty zostały ukończone
    feedbackComponents = [text_feedback, text_wait800]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # resetowanie liczników czasu
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.8:
        # pobieranie aktualnego czasu
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
        
        # *text_feedback* updates
        if text_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # śledzenie czasu rozpoczęcia
            text_feedback.frameNStart = frameN  # dokładny frame index
            text_feedback.tStart = t  # local time, który nie liczy się do odświeżania ekranu
            text_feedback.tStartRefresh = tThisFlipGlobal  # według global time
            win.timeOnFlip(text_feedback, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
            text_feedback.setAutoDraw(True)
        if text_feedback.status == STARTED:
            # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
            if tThisFlipGlobal > text_feedback.tStartRefresh + 1.0-frameTolerance:
                # śledzenie czasu zatrzymania klatki
                text_feedback.tStop = t  # nie liczy się do odświeżania ekranu
                text_feedback.frameNStop = frameN  # dokładny frame index
                text_feedback.setAutoDraw(False)
        
        # *text_wait800* updates
        if text_wait800.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # śledzenie czasu rozpoczęcia
            text_wait800.frameNStart = frameN  # dokładny frame index
            text_wait800.tStart = t  # local time, który nie liczy się do odświeżania ekranu
            text_wait800.tStartRefresh = tThisFlipGlobal  # według global time
            win.timeOnFlip(text_wait800, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
            text_wait800.setAutoDraw(True)
        if text_wait800.status == STARTED:
            # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
            if tThisFlipGlobal > text_wait800.tStartRefresh + 1.8-frameTolerance:
                # śledzenie czasu zatrzymania klatki
                text_wait800.tStop = t  # nie liczy się do odświeżania ekranu
                text_wait800.frameNStop = frameN  # dokładny frame index
                text_wait800.setAutoDraw(False)
        
        # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # sprawdzanie czy wszystkie komponenty się zakończyły
        if not continueRoutine:  #komponent wymaga zakończenia procedury
            routineForceEnded = True
            break
        continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
        
        # odświeżenie ekranu
        if continueRoutine:
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #używano non-slip timer więc należy odjąć oczekiwany czas tej procedury
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.800000)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 's_treningowa'

# pobieranie nazw parametrów bodźców
if s_treningowa.trialList in ([], [None], None):
    params = []
else:
    params = s_treningowa.trialList[0].keys()
# zapisywanie danych z tej pętli
s_treningowa.saveAsExcel(filename + '.xlsx', sheetName='s_treningowa',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "PRZERWA" ---
continueRoutine = True
routineForceEnded = False
# aktualizowanie parametrów komponentu dla każdego powtórzenia
key_resp_Przerwa.keys = []
key_resp_Przerwa.rt = []
_key_resp_Przerwa_allKeys = []
# śledzenie które komponenty zostały ukończone
PRZERWAComponents = [text_przerwa, key_resp_Przerwa]
for thisComponent in PRZERWAComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# resetowanie liczników czasu
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "PRZERWA" ---
while continueRoutine:
    # pobieranie aktualnego czasu
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
    
    # *text_przerwa* updates
    if text_przerwa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # śledzenie czasu rozpoczęcia
        text_przerwa.frameNStart = frameN  # dokładny frame index
        text_przerwa.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        text_przerwa.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(text_przerwa, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        text_przerwa.setAutoDraw(True)
    
    # *key_resp_Przerwa* updates
    if key_resp_Przerwa.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # śledzenie czasu rozpoczęcia
        key_resp_Przerwa.frameNStart = frameN  # dokładny frame index
        key_resp_Przerwa.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        key_resp_Przerwa.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(key_resp_Przerwa, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        key_resp_Przerwa.status = STARTED
        # rozpocznięcie sprawdzania klawiatury
        key_resp_Przerwa.clock.reset()  # teraz t=0
    if key_resp_Przerwa.status == STARTED:
        theseKeys = key_resp_Przerwa.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_Przerwa_allKeys.extend(theseKeys)
        if len(_key_resp_Przerwa_allKeys):
            key_resp_Przerwa.keys = _key_resp_Przerwa_allKeys[-1].name  # jedynie ostatni kliknięty przycisk
            key_resp_Przerwa.rt = _key_resp_Przerwa_allKeys[-1].rt
            # odpowiedź kończy procedurę
            continueRoutine = False
    
    # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # sprawdzanie czy wszystkie komponenty się zakończyły
    if not continueRoutine:  #komponent wymaga zakończenia procedury
        routineForceEnded = True
        break
    continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
    for thisComponent in PRZERWAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
    
    # odświeżenie ekranu
    if continueRoutine:
        win.flip()

# --- Ending Routine "PRZERWA" ---
for thisComponent in PRZERWAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# resetowanie non slip timer (?)
routineTimer.reset()

# --- Prepare to start Routine "eksperyment" ---
continueRoutine = True
routineForceEnded = False
# aktualizowanie parametrów komponentu dla każdego powtórzenia
key_resp_ready2.keys = []
key_resp_ready2.rt = []
_key_resp_ready2_allKeys = []
# śledzenie które komponenty zostały ukończone
eksperymentComponents = [text_eksperyment, text_GetReady2, key_resp_ready2]
for thisComponent in eksperymentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# resetowanie liczników czasu
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "eksperyment" ---
while continueRoutine:
    # pobieranie aktualnego czasu
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
    
    # *text_eksperyment* updates
    if text_eksperyment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # śledzenie czasu rozpoczęcia
        text_eksperyment.frameNStart = frameN  # dokładny frame index
        text_eksperyment.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        text_eksperyment.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(text_eksperyment, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        text_eksperyment.setAutoDraw(True)
    if text_eksperyment.status == STARTED:
        # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
        if tThisFlipGlobal > text_eksperyment.tStartRefresh + 2.0-frameTolerance:
            # śledzenie czasu zatrzymania klatki
            text_eksperyment.tStop = t  # nie liczy się do odświeżania ekranu
            text_eksperyment.frameNStop = frameN  # dokładny frame index
            text_eksperyment.setAutoDraw(False)
    
    # *text_GetReady2* updates
    if text_GetReady2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # śledzenie czasu rozpoczęcia
        text_GetReady2.frameNStart = frameN  # dokładny frame index
        text_GetReady2.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        text_GetReady2.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(text_GetReady2, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        text_GetReady2.setAutoDraw(True)
    
    # *key_resp_ready2* updates
    if key_resp_ready2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # śledzenie czasu rozpoczęcia
        key_resp_ready2.frameNStart = frameN  # dokładny frame index
        key_resp_ready2.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        key_resp_ready2.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(key_resp_ready2, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        key_resp_ready2.status = STARTED
        # rozpocznięcie sprawdzania klawiatury
        key_resp_ready2.clock.reset()  # teraz t=0
    if key_resp_ready2.status == STARTED:
        theseKeys = key_resp_ready2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_ready2_allKeys.extend(theseKeys)
        if len(_key_resp_ready2_allKeys):
            key_resp_ready2.keys = _key_resp_ready2_allKeys[-1].name  # jedynie ostatni kliknięty przycisk
            key_resp_ready2.rt = _key_resp_ready2_allKeys[-1].rt
            # odpowiedź kończy procedurę
            continueRoutine = False
    
    # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # sprawdzanie czy wszystkie komponenty się zakończyły
    if not continueRoutine:  #komponent wymaga zakończenia procedury
        routineForceEnded = True
        break
    continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
    for thisComponent in eksperymentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
    
    # odświeżenie ekranu
    if continueRoutine:
        win.flip()

# --- Ending Routine "eksperyment" ---
for thisComponent in eksperymentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# resetowanie non slip timer (?)
routineTimer.reset()

# randomizacja
trials_6 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # dodawnie pętli do eksperymetnu
thisTrial_6 = trials_6.trialList[0]  # możliwość zainicjowania bodźców z pewnymi wartościami

if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6

    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mikser2" ---
    continueRoutine = True
    routineForceEnded = False
    # Run 'Begin Routine' code from code_mikser2
    element_listy2 = -1  #mikser 2
    
    losowe_niezgodne2 = random.choices(pula_niezgodnych, k=8)
    losowe_zgodne2 = random.choices(pula_zgodnych, k=8)
    losowe_neutralne2 = random.choices(pula_neutralnych, k=4)
    
    losowo_wybrane_bodzce2 = losowe_niezgodne2 + losowe_zgodne2 + losowe_neutralne2
    shuffle(losowo_wybrane_bodzce2)
    
    losowo_wybrane_slowo2 = [x[0] for x in losowo_wybrane_bodzce2]
    losowo_wybrany_kolor2 = [x[1] for x in losowo_wybrane_bodzce2]
    czy_jest_zgodne2 = [x[2] for x in losowo_wybrane_bodzce2]
    co_klikac2 = [x[3] for x in losowo_wybrane_bodzce2]
    wybrany_jezyk = [x[4] for x in losowo_wybrane_bodzce2]
    # śledzenie które komponenty zostały ukończone
    mikser2Components = []
    for thisComponent in mikser2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # resetowanie liczników czasu
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mikser2" ---
    while continueRoutine:
        # pobieranie aktualnego czasu
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
        
        # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # sprawdzanie czy wszystkie komponenty się zakończyły
        if not continueRoutine:  #komponent wymaga zakończenia procedury
            routineForceEnded = True
            break
        continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
        for thisComponent in mikser2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
        
        # odświeżenie ekranu
        if continueRoutine:
            win.flip()
    
    # --- Ending Routine "mikser2" ---
    for thisComponent in mikser2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # resetowanie non slip timer (?)
    routineTimer.reset()
    
    # randomizacja
    s_eksperymentalna = data.TrialHandler(nReps=20.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='s_eksperymentalna')
    thisExp.addLoop(s_eksperymentalna)  # dodawnie pętli do eksperymetnu
    thisS_eksperymentalna = s_eksperymentalna.trialList[0]  # możliwość zainicjowania bodźców z pewnymi wartościami

    if thisS_eksperymentalna != None:
        for paramName in thisS_eksperymentalna:
            exec('{} = thisS_eksperymentalna[paramName]'.format(paramName))
    
    for thisS_eksperymentalna in s_eksperymentalna:
        currentLoop = s_eksperymentalna

        if thisS_eksperymentalna != None:
            for paramName in thisS_eksperymentalna:
                exec('{} = thisS_eksperymentalna[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # śledzenie które komponenty zostały ukończone
        fixationComponents = [polygon_cross]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # resetowanie liczników czasu
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # pobieranie aktualnego czasu
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)

            
            # *polygon_cross* updates
            if polygon_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # śledzenie czasu rozpoczęcia
                polygon_cross.frameNStart = frameN  # dokładny frame index
                polygon_cross.tStart = t  # local time, który nie liczy się do odświeżania ekranu
                polygon_cross.tStartRefresh = tThisFlipGlobal  # według global time
                win.timeOnFlip(polygon_cross, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
                polygon_cross.setAutoDraw(True)
            if polygon_cross.status == STARTED:
                # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
                if tThisFlipGlobal > polygon_cross.tStartRefresh + 0.5-frameTolerance:
                    # śledzenie czasu zatrzymania klatki
                    polygon_cross.tStop = t  # nie liczy się do odświeżania ekranu
                    polygon_cross.frameNStop = frameN  # dokładny frame index
                    polygon_cross.setAutoDraw(False)
            
            # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # sprawdzanie czy wszystkie komponenty się zakończyły
            if not continueRoutine:  #komponent wymaga zakończenia procedury
                routineForceEnded = True
                break
            continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
            
            # odświeżenie ekranu
            if continueRoutine:
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #używano non-slip timer więc należy odjąć oczekiwany czas tej procedury
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "stroop2" ---
        continueRoutine = True
        routineForceEnded = False
        # Run 'Begin Routine' code from code_Stroop2
        element_listy2 += 1
        #zmienne do wciśnięcia w okienka z tekstem i kolorem
        pokazywane_slowo2 = losowo_wybrane_slowo2[element_listy2]
        pokazywany_kolor2 = losowo_wybrany_kolor2[element_listy2]
        kliknij_to2 = co_klikac2[element_listy2]
        zgodny_czy_nie2 = czy_jest_zgodne2[element_listy2]
        jaki_jezyk2 = wybrany_jezyk[element_listy2]
        text_Slowo2.setColor(pokazywany_kolor2, colorSpace='rgb')
        text_Slowo2.setText(pokazywane_slowo2)
        key_resp_stroop2.keys = []
        key_resp_stroop2.rt = []
        _key_resp_stroop2_allKeys = []
        textbox_ASKL2.reset()
        textbox_ASKL2.setText('"A" - czarny    "S" - brązowy   "K" - fioletowy   "L" - różowy')
        # śledzenie które komponenty zostały ukończone
        stroop2Components = [text_Slowo2, key_resp_stroop2, textbox_ASKL2]
        for thisComponent in stroop2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # resetowanie liczników czasu
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stroop2" ---
        while continueRoutine and routineTimer.getTime() < 5.0:
            # pobieranie aktualnego czasu
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
            
            # *text_Slowo2* updates
            if text_Slowo2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # śledzenie czasu rozpoczęcia
                text_Slowo2.frameNStart = frameN  # dokładny frame index
                text_Slowo2.tStart = t  # local time, który nie liczy się do odświeżania ekranu
                text_Slowo2.tStartRefresh = tThisFlipGlobal  # według global time
                win.timeOnFlip(text_Slowo2, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
                text_Slowo2.setAutoDraw(True)
            if text_Slowo2.status == STARTED:
                # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
                if tThisFlipGlobal > text_Slowo2.tStartRefresh + 0.5-frameTolerance:
                    # śledzenie czasu zatrzymania klatki
                    text_Slowo2.tStop = t  # nie liczy się do odświeżania ekranu
                    text_Slowo2.frameNStop = frameN  # dokładny frame index
                    text_Slowo2.setAutoDraw(False)
            
            # *key_resp_stroop2* updates
            waitOnFlip = False
            if key_resp_stroop2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # śledzenie czasu rozpoczęcia
                key_resp_stroop2.frameNStart = frameN  # dokładny frame index
                key_resp_stroop2.tStart = t  # local time, który nie liczy się do odświeżania ekranu
                key_resp_stroop2.tStartRefresh = tThisFlipGlobal  # według global time
                win.timeOnFlip(key_resp_stroop2, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
                key_resp_stroop2.status = STARTED
                # rozpocznięcie sprawdzania klawiatury
                waitOnFlip = True
                win.callOnFlip(key_resp_stroop2.clock.reset)  # t=0 przy następnym przerzuceniu ekranu (screen flip)
                win.callOnFlip(key_resp_stroop2.clearEvents, eventType='keyboard')  # czyszczenie wydarzeń przy następnym przerzuceniu ekranu (flip screen)
            if key_resp_stroop2.status == STARTED:
                # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
                if tThisFlipGlobal > key_resp_stroop2.tStartRefresh + 5.0-frameTolerance:
                    # śledzenie czasu zatrzymania klatki
                    key_resp_stroop2.tStop = t  # nie liczy się do odświeżania ekranu
                    key_resp_stroop2.frameNStop = frameN  # dokładny frame index
                    key_resp_stroop2.status = FINISHED
            if key_resp_stroop2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_stroop2.getKeys(keyList=['a', 's', 'k', 'l'], waitRelease=False)
                _key_resp_stroop2_allKeys.extend(theseKeys)
                if len(_key_resp_stroop2_allKeys):
                    key_resp_stroop2.keys = _key_resp_stroop2_allKeys[-1].name  # jedynie ostatni kliknięty przycisk
                    key_resp_stroop2.rt = _key_resp_stroop2_allKeys[-1].rt
                    # sprawdzanie czy to było poprawne
                    if (key_resp_stroop2.keys == str(kliknij_to2)) or (key_resp_stroop2.keys == kliknij_to2):
                        key_resp_stroop2.corr = 1
                    else:
                        key_resp_stroop2.corr = 0
                    # odpowiedź kończy procedurę
                    continueRoutine = False
            
            # *textbox_ASKL2* updates
            if textbox_ASKL2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # śledzenie czasu rozpoczęcia
                textbox_ASKL2.frameNStart = frameN  # dokładny frame index
                textbox_ASKL2.tStart = t  # local time, który nie liczy się do odświeżania ekranu
                textbox_ASKL2.tStartRefresh = tThisFlipGlobal  # według global time
                win.timeOnFlip(textbox_ASKL2, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
                textbox_ASKL2.setAutoDraw(True)
            if textbox_ASKL2.status == STARTED:
                # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
                if tThisFlipGlobal > textbox_ASKL2.tStartRefresh + 5.0-frameTolerance:
                    # śledzenie czasu zatrzymania klatki
                    textbox_ASKL2.tStop = t  # nie liczy się do odświeżania ekranu
                    textbox_ASKL2.frameNStop = frameN  # dokładny frame index
                    textbox_ASKL2.setAutoDraw(False)
            
            # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # sprawdzanie czy wszystkie komponenty się zakończyły
            if not continueRoutine:  #komponent wymaga zakończenia procedury
                routineForceEnded = True
                break
            continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
            for thisComponent in stroop2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
            
            # odświeżenie ekranu
            if continueRoutine:
                win.flip()
        
        # --- Ending Routine "stroop2" ---
        for thisComponent in stroop2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_Stroop2
        s_eksperymentalna.addData('pokazywane_slowo2', pokazywane_slowo2)
        s_eksperymentalna.addData('jaki_jezyk2', jaki_jezyk2)
        s_eksperymentalna.addData('zgodny_czy_nie2', zgodny_czy_nie2)
        # sprwadzanie odpowiedzi
        if key_resp_stroop2.keys in ['', [], None]:  # nie udzielono odpowiedzi
            key_resp_stroop2.keys = None
            # sprwadzanie czy nie udzielono odpowiedzi było poprawne (bez sensu bo nie ma takiego warunku w tym eksperymencie)
            if str(kliknij_to2).lower() == 'none':
               key_resp_stroop2.corr = 1;  # poprawne było brak odpoweidzi
            else:
               key_resp_stroop2.corr = 0;  # zła odpowiedź
        # PRZECHOWYWANIE DANYCH DLA s_eksperymentalna (TrialHandler)
        s_eksperymentalna.addData('key_resp_stroop2.keys',key_resp_stroop2.keys)
        s_eksperymentalna.addData('key_resp_stroop2.corr', key_resp_stroop2.corr)
        if key_resp_stroop2.keys != None:  # mamy odpowiedź
            s_eksperymentalna.addData('key_resp_stroop2.rt', key_resp_stroop2.rt)
        # używano non-slip timer więc należy odjąć oczekiwany czas tej procedury
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed 20.0 repeats of 's_eksperymentalna'
    
    # pobieranie nazw parametrów bodźców
    if s_eksperymentalna.trialList in ([], [None], None):
        params = []
    else:
        params = s_eksperymentalna.trialList[0].keys()
    # zapisywanie danych z tej pętli
    s_eksperymentalna.saveAsExcel(filename + '.xlsx', sheetName='s_eksperymentalna',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "PRZERWA" ---
    continueRoutine = True
    routineForceEnded = False
    # aktualizowanie parametrów komponentu dla każdego powtórzenia
    key_resp_Przerwa.keys = []
    key_resp_Przerwa.rt = []
    _key_resp_Przerwa_allKeys = []
    # śledzenie które komponenty zostały ukończone
    PRZERWAComponents = [text_przerwa, key_resp_Przerwa]
    for thisComponent in PRZERWAComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # resetowanie liczników czasu
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PRZERWA" ---
    while continueRoutine:
        # pobieranie aktualnego czasu
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
        
        # *text_przerwa* updates
        if text_przerwa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # śledzenie czasu rozpoczęcia
            text_przerwa.frameNStart = frameN  # dokładny frame index
            text_przerwa.tStart = t  # local time, który nie liczy się do odświeżania ekranu
            text_przerwa.tStartRefresh = tThisFlipGlobal  # według global time
            win.timeOnFlip(text_przerwa, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
            text_przerwa.setAutoDraw(True)
        
        # *key_resp_Przerwa* updates
        if key_resp_Przerwa.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # śledzenie czasu rozpoczęcia
            key_resp_Przerwa.frameNStart = frameN  # dokładny frame index
            key_resp_Przerwa.tStart = t  # local time, który nie liczy się do odświeżania ekranu
            key_resp_Przerwa.tStartRefresh = tThisFlipGlobal  # według global time
            win.timeOnFlip(key_resp_Przerwa, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
            key_resp_Przerwa.status = STARTED
            # rozpocznięcie sprawdzania klawiatury
            key_resp_Przerwa.clock.reset()  # teraz t=0
        if key_resp_Przerwa.status == STARTED:
            theseKeys = key_resp_Przerwa.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_Przerwa_allKeys.extend(theseKeys)
            if len(_key_resp_Przerwa_allKeys):
                key_resp_Przerwa.keys = _key_resp_Przerwa_allKeys[-1].name  # jedynie ostatni kliknięty przycisk
                key_resp_Przerwa.rt = _key_resp_Przerwa_allKeys[-1].rt
                # odpowiedź kończy procedurę
                continueRoutine = False
        
        # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # sprawdzanie czy wszystkie komponenty się zakończyły
        if not continueRoutine:  #komponent wymaga zakończenia procedury
            routineForceEnded = True
            break
        continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
        for thisComponent in PRZERWAComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
        
        # odświeżenie ekranu
        if continueRoutine:
            win.flip()
    
    # --- Ending Routine "PRZERWA" ---
    for thisComponent in PRZERWAComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # resetowanie non slip timer (?)
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials_6'

# pobieranie nazw parametrów bodźców
if trials_6.trialList in ([], [None], None):
    params = []
else:
    params = trials_6.trialList[0].keys()
# zapisywanie danych z tej pętli
trials_6.saveAsExcel(filename + '.xlsx', sheetName='trials_6',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "koniec" ---
continueRoutine = True
routineForceEnded = False
# śledzenie które komponenty zostały ukończone
koniecComponents = [text_koniec]
for thisComponent in koniecComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# resetowanie liczników czasu
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "koniec" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # pobieranie aktualnego czasu
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # liczba zakończonych klatek (0 to pierwsza klatka)
    
    # *text_koniec* updates
    if text_koniec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # śledzenie czasu rozpoczęcia
        text_koniec.frameNStart = frameN  # dokładny frame index
        text_koniec.tStart = t  # local time, który nie liczy się do odświeżania ekranu
        text_koniec.tStartRefresh = tThisFlipGlobal  # według global time
        win.timeOnFlip(text_koniec, 'tStartRefresh')  # czas kiedy następny ekran się odświeży
        text_koniec.setAutoDraw(True)
    if text_koniec.status == STARTED:
        # badanie kiedy bodźiec ma przestać być wyświetlany (wg global time)
        if tThisFlipGlobal > text_koniec.tStartRefresh + 5-frameTolerance:
            # śledzenie czasu zatrzymania klatki
            text_koniec.tStop = t  # nie liczy się do odświeżania ekranu
            text_koniec.frameNStop = frameN  # dokładny frame index
            text_koniec.setAutoDraw(False)
    
    # sprawdzanie czy wyszło się z procedury w jej trakcie (escape)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # sprawdzanie czy wszystkie komponenty się zakończyły
    if not continueRoutine:  #komponent wymaga zakończenia procedury
        routineForceEnded = True
        break
    continueRoutine = False  # (zamieni się w True jeżeli chociaż jeden komponent będzie wciąż chodził)
    for thisComponent in koniecComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # (jeżeli przynajmniej jeden konponent nie został jeszcze zakończony)
    
    # odświeżenie ekranu
    if continueRoutine:
        win.flip()

# --- Ending Routine "koniec" ---
for thisComponent in koniecComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# używano non-slip timer więc należy odjąć oczekiwany czas tej procedury
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- KONIEC EKSPERYMENTU ---

# ostatnie przerzucenie ekranu żeby nic nie zostało
win.flip()

# to nie jest wymagane gdyż działa autozapis ale może się przydać
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# zapewnienie czy eyetracker jest wyłączony xd
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  
win.close()
core.quit()
