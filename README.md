# Руководство по использованию приложения для применения фильтров к изображениям

Это приложение позволяет загружать изображения, применять к ним различные фильтры (например, размытие, повышение резкости и другие), а также сохранять результат. Фильтры задаются с помощью матриц 3x3, которые можно выбирать из списка или вводить вручную.

---

## **Как пользоваться приложением**

### 1. **Загрузка изображения**
   - Нажмите кнопку **"Load Image"**.
   - Выберите изображение в формате JPG, JPEG, PNG или BMP.
   - Изображение отобразится в окне приложения.

### 2. **Выбор фильтра**
   - В выпадающем списке выберите один из предустановленных фильтров (например, "Blur", "Sharpen" и т.д.).
   - Матрица фильтра автоматически заполнится в полях ввода.

### 3. **Ручное редактирование фильтра**
   - Вы можете вручную изменить значения в матрице 3x3, чтобы создать собственный фильтр.
   - Вводите числовые значения в каждое поле.

### 4. **Применение фильтра**
   - Нажмите кнопку **"Apply Filter"**, чтобы применить выбранный фильтр к изображению.
   - В процессе обработки появится сообщение **"Обработка..."**.

### 5. **Смешивание результата**
   - В поле **"Blending (%)"** укажите процент смешивания отфильтрованного изображения с оригиналом.
     - **100%** — полностью отфильтрованное изображение.
     - **0%** — оригинальное изображение.
   - Нажмите **"Apply Filter"** для обновления результата.

### 6. **Сброс к оригиналу**
   - Нажмите кнопку **"Reset to Original"**, чтобы вернуть изображение к исходному виду.

### 7. **Сохранение результата**
   - Нажмите кнопку **"Save Image"**.
   - Выберите формат (JPG, PNG, BMP) и укажите путь для сохранения.

---

## **Описание фильтров**
В приложении доступны следующие предустановленные фильтры:

- **Blur** (Размытие): Усредняет цвета пикселей, создавая эффект размытия.
- **Sharpen** (Резкость): Увеличивает контраст между соседними пикселями, делая изображение более четким.
- **Sobel Vertical** (Собель по вертикали): Выделяет вертикальные границы на изображении.
- **Sobel Horizontal** (Собель по горизонтали): Выделяет горизонтальные границы на изображении.
- **Laplacian** (Лапласиан): Подчеркивает границы и детали изображения.
- **Emboss** (Тиснение): Создает эффект объемности, как будто изображение выдавлено на поверхности.
- **Gaussian Blur** (Гауссово размытие): Размытие с использованием гауссова распределения.
- **Motion Blur** (Размытие в движении): Создает эффект размытия в направлении движения.

---

## **Как работает приложение**
1. **Загрузка изображения:** Изображение открывается и преобразуется в формат RGB.
2. **Применение фильтра:** Каждый пиксель изображения обрабатывается с учетом его соседей и значений из матрицы фильтра.
3. **Смешивание:** Результат фильтрации смешивается с оригинальным изображением в указанной пропорции.
4. **Сохранение:** Отфильтрованное изображение сохраняется в выбранном формате.

---

## **Требования**
- Установленный Python 3.
- Установленные библиотеки:
  - `tkinter` (для графического интерфейса).
  - `Pillow` (для работы с изображениями).

Установите необходимые библиотеки с помощью команды:
```bash
pip install pillow
```

---

## **Пример использования**
1. Загрузите изображение.
2. Выберите фильтр "Sharpen" из списка.
3. Нажмите "Apply Filter".
4. Установите значение "Blending (%)" на 50, чтобы смешать результат с оригиналом.
5. Сохраните результат.

---

## **Примечания**
- Если введены некорректные значения в матрицу фильтра, появится сообщение об ошибке.
- Для создания собственных фильтров вручную введите числовые значения в поля матрицы 3x3.
