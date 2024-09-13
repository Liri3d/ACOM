import cv2 as cv2

print(cv2.__version__)

# Задание 2 
# Вывести на экран изображение. Протестировать три
# возможных расширения, три различных флага для создания окна и три
# различных флага для чтения изображения.

img1 = cv2.imread(r'E:/4kurs1sem/ACOM/lab1/malamut.png', cv2.IMREAD_COLOR)              # Цветовой формат RGB
cv2.namedWindow('img1', cv2.WINDOW_AUTOSIZE)
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.imshow('img1', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2 = cv2.imread(r'E:/4kurs1sem/ACOM/lab1/malamut.jpg', cv2.IMREAD_GRAYSCALE)          # Оттенки серого
cv2.namedWindow('img2', cv2.WINDOW_FULLSCREEN)
cv2.imshow('img2', cv2.resize(img2, (1920, 1080), interpolation=cv2.INTER_CUBIC))
cv2.waitKey(0)
cv2.destroyAllWindows()


img3= cv2.imread(r'E:/4kurs1sem/ACOM/lab1/malamut.tif', cv2.IMREAD_REDUCED_COLOR_4)         # Четверь от размера оригинала
cv2.namedWindow('img3', cv2.WINDOW_NORMAL)
cv2.imshow('img3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Задание 3
# Отобразить видео в окне. Рассмотреть методы класса
# VideoCapture и попробовать отображать видео в разных форматах, в частности
# размеры и цветовая гамма.

# cap = cv2.VideoCapture(r'E:/4kurs1sem/ACOM/lab1/dog_video.mp4', cv2.CAP_ANY)

# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     resized_frame = cv2.resize(frame, (640, 480)) 
#     cv2.imshow('frame', cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY))                        # Отображение в оттенках серого
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     cv2.imshow('frame', hsv)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     resized_frame = cv2.resize(frame, (200, 200)) 
#     cv2.imshow('frame', cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGBA))                        # Отображение кадра с сохранением альфа-канала, альфа определяет уровень прозрачности пикселя
#     if cv2.waitKey(1) & 0xFF == 27:
#         break



# Задание 4
# Записать видео из файла в другой файл.

# # Открываем видеофайл для чтения
# input_video = cv2.VideoCapture(r'E:/4kurs1sem/ACOM/lab1/playing_cards.mp4')

# # Чтение характеристик видео (размеры кадра, FPS и т.д.)
# width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = input_video.get(cv2.CAP_PROP_FPS)

# # Определение кодека для записи видео
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# # Создаем объект VideoWriter для записи видео в новый файл
# output_video = cv2.VideoWriter('E:/4kurs1sem/ACOM/lab1/output_playing_cards.mp4', fourcc, fps, (width, height))

# # Чтение кадров из исходного видео и запись их в новый файл
# while True:
#     ret, frame = input_video.read()
#     if not ret:
#         break
#     # cv2.imshow('frame', frame) # Отображение
   
#     # При нажатии Esc прикратится запись и отображение
#     if fps > 0:
#         delay = int(500 / fps) # Задержка = 500 миллисекунд / кол-во кадров в секунду
#     else: 1
#     if cv2.waitKey(delay) & 0xFF == 27:
#         break
#     # Записываем кадр в выходное видео
#     output_video.write(frame)

# # Освобождаем ресурсы
# input_video.release()
# output_video.release()
# cv2.destroyAllWindows()



# Задание 5.
# Прочитать изображение, перевести его в формат HSV.
# Вывести на экран два окна, в одном изображение в формате HSV, в другом –
# исходное изображение.

# img1 = cv2.imread(r'E:/4kurs1sem/ACOM/lab1/ATM.jpg', cv2.IMREAD_COLOR) # Цветовой формат RGB
# hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

# cv2.namedWindow('img1', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('img1', cv2.resize(img1, (640, 480)) )

# cv2.namedWindow('hsv', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('hsv', cv2.resize(hsv, (640, 480)) )

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Задание 6. 
# Прочитать изображение с камеры. Вывести
# в центре на экране Красный крест в формате, как на изображении. Указать
# команды, которые позволяют это сделать.

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# while True:
#     ret, frame = cap.read()

#     thickness = 2
#     color = (0, 0, 255) 
#     center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2

#     # Горизонтальный прямоугольник
#     top_left = (center_x - 80, center_y - 10)
#     bottom_right = (center_x + 80, center_y + 10)
#     cv2.rectangle(frame, top_left, bottom_right, color, thickness)
        
#     # Верхний прямоугольникё
#     top_left = (center_x - 10, center_y - 100)
#     bottom_right = (center_x + 10, center_y - 10)
#     cv2.rectangle(frame, top_left, bottom_right, color, thickness)
        
#     # Нижний прямоугольник
#     top_left = (center_x - 10, center_y + 10)
#     bottom_right = (center_x + 10, center_y + 100)
#     cv2.rectangle(frame, top_left, bottom_right, color, thickness) 

#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()



# Задание 7. 
# Отобразить информацию с вебкамеры,
# записать видео в файл, продемонстрировать видео.

# cap = cv2.VideoCapture(0) # Захват видео с камеры
# cap.set(3, 640) # Размеры захвата видео
# cap.set(4, 480)

# fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Формат сжатия видео
# out = cv2.VideoWriter('E:/4kurs1sem/ACOM/lab1/output_camera.mp4', fourcc, 20.0, (640, 480))

# while True:
#     # Захват кадра из видео
#     ret, frame = cap.read()
        
#     # Если кадр не захвачен, то break
#     if not ret:
#         break
        
#     # Записываем кадр в файл
#     out.write(frame)

#     # Делаем кадр серым
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Отображаем кадр в окне
#     cv2.imshow('frame', frame)
#     # Esc для закрытия окна
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release() # Освобождаем резурсы захвата экрана
# out.release() # ОСвобождаем ресурсы записи видео 
# cv2.destroyAllWindows()



# Задание 8. Залить крест одним из 3 цветов – красный,
# зеленый, синий по следующему правилу: НА ОСНОВАНИИ ФОРМАТА RGB
# определить, центральный пиксель ближе к какому из цветов красный,
# зеленый, синий и таким цветом заполнить крест.

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# while True:
#     ret, frame = cap.read()

#     center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2

#     # Получение цвета центрального пикселя
#     r, g, b = frame[center_y, center_x]

#     thickness = -1

#     if (b > g) & (b > r):
#         color = (0, 0, 255)
#     if (g > r) & (g > b):
#         color = (0, 255, 0)
#     if (r > g) & (r > b):
#         color = (255, 0, 0)

#     # Горизонтальный прямоугольник
#     top_left = (center_x - 80, center_y - 10)
#     bottom_right = (center_x + 80, center_y + 10)
#     cv2.rectangle(frame, top_left, bottom_right, color, thickness)
        
#     # Верхний прямоугольник
#     top_left = (center_x - 10, center_y - 100)
#     bottom_right = (center_x + 10, center_y - 10)
#     cv2.rectangle(frame, top_left, bottom_right, color, thickness)
        
#     # Нижний прямоугольник
#     top_left = (center_x - 10, center_y + 10)
#     bottom_right = (center_x + 10, center_y + 100)
#     cv2.rectangle(frame, top_left, bottom_right, color, thickness) 

#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()



# Задание 9. Подключите телефон, подключитесь к его
# камере, выведете на экран видео с камеры. Продемонстрировать процесс на
# ноутбуке преподавателя и своем телефоне.

# url = "http://192.168.0.101:8080/video"

# cap = cv2.VideoCapture(url) # Захват видео с камеры
# cap.set(3, 1280) # Размеры захвата видео
# cap.set(4, 860)

# # fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Формат сжатия видео

# while True:
#     # Захват кадра из видео
#     ret, frame = cap.read()
        
#     # Если кадр не захвачен, то break
#     if not ret:
#         break
        
#     # Отображаем кадр в окне
#     cv2.imshow('frame', frame)
#     # Esc для закрытия окна
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release() # Освобождаем резурсы захвата экрана
# cv2.destroyAllWindows()