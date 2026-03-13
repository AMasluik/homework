import tkinter as tk
from tkinter import messagebox, font
import json
import os


class ShoppingList:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Мамин список покупок")
        self.root.geometry("600x550")
        self.root.configure(bg='#fff3e6')  # Тёплый кремовый фон

        # Настройка шрифтов
        self.title_font = font.Font(family="Arial", size=18, weight="bold")
        self.normal_font = font.Font(family="Arial", size=11)
        self.button_font = font.Font(family="Arial", size=10)

        # Файл для сохранения списка
        self.save_file = "shopping_list.json"

        # Предустановленные наборы продуктов
        self.preset_lists = {
            "Для борща": ["свёкла", "картошка", "морковка", "капуста", "лук", "томатная паста", "чеснок", "мясо"],
            "Для выпечки": ["мука", "сахар", "яйца", "масло сливочное", "дрожжи", "ванилин", "соль"],
            "Фрукты": ["яблоки", "бананы", "апельсины", "груши", "виноград", "киви"],
            "Овощи": ["огурцы", "помидоры", "перец", "лук", "чеснок", "зелень"],
            "Молочное": ["молоко", "кефир", "творог", "сметана", "йогурт", "сыр"],
            "Чай/кофе": ["чёрный чай", "зелёный чай", "кофе", "сахар", "мёд", "лимон"]
        }

        # Загружаем сохранённый список
        self.items = self.load_list()

        self.create_widgets()
        self.update_listbox()

    def create_widgets(self):
        # Заголовок
        title = tk.Label(
            self.root,
            text="🛍️ Список покупок",
            font=self.title_font,
            bg='#fff3e6',
            fg='#c44f4f'
        )
        title.pack(pady=15)

        # Рамка для ввода
        input_frame = tk.Frame(self.root, bg='#fff3e6')
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Добавить продукт:",
            font=self.normal_font,
            bg='#fff3e6'
        ).pack(side=tk.LEFT, padx=5)

        self.item_entry = tk.Entry(
            input_frame,
            width=30,
            font=self.normal_font,
            bd=2,
            relief=tk.GROOVE
        )
        self.item_entry.pack(side=tk.LEFT, padx=5)
        self.item_entry.bind('<Return>', lambda e: self.add_item())  # Enter добавляет

        tk.Button(
            input_frame,
            text="➕ Добавить",
            bg='#98fb98',
            font=self.button_font,
            padx=10,
            command=self.add_item
        ).pack(side=tk.LEFT, padx=5)

        # Кнопки с наборами продуктов
        preset_frame = tk.Frame(self.root, bg='#fff3e6')
        preset_frame.pack(pady=10)

        tk.Label(
            preset_frame,
            text="Быстрые наборы:",
            font=self.normal_font,
            bg='#fff3e6'
        ).pack(anchor='w', padx=20)

        # Создаём кнопки для каждого набора
        buttons_frame = tk.Frame(self.root, bg='#fff3e6')
        buttons_frame.pack(pady=5)

        row, col = 0, 0
        for preset_name in self.preset_lists:
            btn = tk.Button(
                buttons_frame,
                text=preset_name,
                bg='#ffe4b5',
                font=self.button_font,
                width=12,
                command=lambda name=preset_name: self.add_preset(name)
            )
            btn.grid(row=row, column=col, padx=3, pady=2)
            col += 1
            if col > 2:  # 3 кнопки в ряд
                col = 0
                row += 1

        # Основной список покупок
        list_frame = tk.Frame(self.root, bg='white', bd=2, relief=tk.GROOVE)
        list_frame.pack(pady=15, padx=20, fill='both', expand=True)

        # Заголовок списка
        list_header = tk.Frame(list_frame, bg='#f0d9c0')
        list_header.pack(fill='x')

        tk.Label(
            list_header,
            text="📝 Мои продукты",
            font=self.normal_font,
            bg='#f0d9c0',
            fg='#5d3a1a'
        ).pack(side=tk.LEFT, padx=10, pady=5)

        tk.Label(
            list_header,
            text="(нажмите на продукт, чтобы отметить купленным)",
            font=font.Font(family="Arial", size=9),
            bg='#f0d9c0',
            fg='#7a5c3a'
        ).pack(side=tk.RIGHT, padx=10, pady=5)

        # Список с прокруткой
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill='y')

        self.listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=self.normal_font,
            height=12,
            selectmode=tk.SINGLE,
            bg='white',
            fg='#2c3e50',
            selectbackground='#d4edda'
        )
        self.listbox.pack(fill='both', expand=True, padx=5, pady=5)

        scrollbar.config(command=self.listbox.yview)

        # Привязываем клик по элементу
        self.listbox.bind('<Button-1>', self.on_item_click)

        # Кнопки управления
        control_frame = tk.Frame(self.root, bg='#fff3e6')
        control_frame.pack(pady=10)

        tk.Button(
            control_frame,
            text="✅ Убрать отмеченные",
            bg='#87cefa',
            font=self.button_font,
            padx=15,
            command=self.remove_checked
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            control_frame,
            text="🗑️ Очистить всё",
            bg='#faa0a0',
            font=self.button_font,
            padx=15,
            command=self.clear_all
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            control_frame,
            text="💾 Сохранить",
            bg='#dda0dd',
            font=self.button_font,
            padx=15,
            command=self.save_list
        ).pack(side=tk.LEFT, padx=5)

        # Статусная строка
        self.status_label = tk.Label(
            self.root,
            text="",
            font=font.Font(family="Arial", size=9),
            bg='#fff3e6',
            fg='#666666'
        )
        self.status_label.pack(pady=5)

    def add_item(self):
        """Добавляет новый продукт в список"""
        item = self.item_entry.get().strip().lower()
        if item:
            # Проверяем, нет ли уже такого продукта
            if not any(i['name'] == item for i in self.items):
                self.items.append({"name": item, "checked": False})
                self.update_listbox()
                self.item_entry.delete(0, tk.END)
                self.update_status(f"✅ {item} добавлен в список")
                self.save_list()  # Автосохранение
            else:
                messagebox.showinfo("Уже есть", f"❌ {item} уже в списке!")
        else:
            messagebox.showwarning("Ой!", "Введите название продукта")

    def add_preset(self, preset_name):
        """Добавляет набор продуктов"""
        added = 0
        for item in self.preset_lists[preset_name]:
            if not any(i['name'] == item for i in self.items):
                self.items.append({"name": item, "checked": False})
                added += 1

        self.update_listbox()
        self.save_list()
        self.update_status(f"📦 Добавлен набор '{preset_name}' (+{added} продуктов)")

    def on_item_click(self, event):
        """Обрабатывает клик по элементу списка"""
        index = self.listbox.nearest(event.y)
        if 0 <= index < len(self.items):
            # Переключаем статус checked
            self.items[index]["checked"] = not self.items[index]["checked"]
            self.update_listbox()
            self.save_list()  # Автосохранение при отметке

    def remove_checked(self):
        """Удаляет все отмеченные продукты"""
        before_count = len(self.items)
        self.items = [item for item in self.items if not item["checked"]]
        after_count = len(self.items)
        removed = before_count - after_count

        self.update_listbox()
        self.save_list()

        if removed > 0:
            self.update_status(f"✅ Убрано {removed} купленных продуктов")
        else:
            self.update_status("ℹ️ Нет отмеченных продуктов")

    def clear_all(self):
        """Очищает весь список"""
        if self.items and messagebox.askyesno("Подтверждение", "Очистить весь список?"):
            self.items = []
            self.update_listbox()
            self.save_list()
            self.update_status("🗑️ Список очищен")

    def save_list(self):
        """Сохраняет список в файл"""
        try:
            with open(self.save_file, 'w', encoding='utf-8') as f:
                json.dump(self.items, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить: {e}")

    def load_list(self):
        """Загружает список из файла"""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def update_listbox(self):
        """Обновляет отображение списка"""
        self.listbox.delete(0, tk.END)

        # Сортируем: сначала некупленные, потом купленные
        sorted_items = sorted(self.items, key=lambda x: x["checked"])

        for item in sorted_items:
            display_text = f"  {item['name']}"
            if item["checked"]:
                display_text = f"✓ {item['name']} (куплено)"
                self.listbox.insert(tk.END, display_text)
                # Красим купленное серым
                self.listbox.itemconfig(tk.END, fg='#888888')
            else:
                self.listbox.insert(tk.END, display_text)
                self.listbox.itemconfig(tk.END, fg='#000000')

        # Обновляем статус
        total = len(self.items)
        bought = sum(1 for item in self.items if item["checked"])
        self.update_status(f"📊 Всего: {total} продуктов (куплено: {bought})")

    def update_status(self, message):
        """Обновляет статусную строку"""
        self.status_label.config(text=message)
        # Через 3 секунды возвращаем статистику
        self.root.after(3000, self.show_stats)

    def show_stats(self):
        """Показывает статистику в статусной строке"""
        total = len(self.items)
        bought = sum(1 for item in self.items if item["checked"])
        self.status_label.config(text=f"📊 Всего: {total} продуктов (куплено: {bought})")


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingList(root)
    root.mainloop()