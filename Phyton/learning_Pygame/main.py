from settings import *
import pygame as pg
import colors


window = pg.display.set_mode(resolutions[resolution]) # Задаём переменную нашего окна
pg.display.set_caption(windowTitle, icontitle=windowIcon) # Залаём этому окну название и иконку

clock = pg.time.Clock() # Задаём переменную с модулем, который отвечает за работу со временем в окне


run = True
while run: # Основной цикл окна
    clock.tick(MAXFPS) # Задаём ограничение FPS для окна
    fps = clock.get_fps() # Получение FPS окна

    if fps > 0:
        deltaFPS = MAXFPS / fps # Подщет отклонения реального FPS от требуемого(MAXFPS)
    else:
        deltaFPS = 0

    
    for event in pg.event.get(): # Обработка событий в окне
        if event.type == pg.QUIT: # Проверка на нажатие кнопки закрытия окна
            run = False

    window.fill(colors.BLACK) # Начало отрисовки графики



    pg.display.update() # Конец отрисовки графики
    
pg.quit() # заверешение процессов окна
exit() # завершение работы python