class Button:
    def __init__(self, text, locator=""):
        self.text = text
        self.type = "Кнопка"
        self.locator = locator

    def click(self):
        return f"Клик по кнопке {self.text}"


if __name__ == "__main__":
    button_texts = [
        "Text Box",
        "Check Box",
        "Radio Button",
        "Web Tables",
        "Buttons",
        "Links",
        "Broken Links - Images",
        "Upload and Download",
        "Dynamic Properties",
        "Practice Form",
        "Browser Windows",
        "Alerts",
        "Frames",
        "Nested Frames",
        "Modal Dialogs",
        "Accordian",
        "Auto Complete",
        "Date Picker",
        "Slider",
        "Progress Bar",
        "Tabs",
        "Tool Tips",
        "Menu",
        "Select Menu",
        "Sortable",
        "Selectable",
        "Resizable",
        "Droppable",
        "Draggable",
        "Login",
        "Book Store",
        "Profile",
        "Book Store API",
    ]

    buttons = [Button(text) for text in button_texts]

    for button in buttons:
        print(button.text)

    print()

    for button in buttons:
        print(button.click())