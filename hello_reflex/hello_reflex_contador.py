import reflex as rx

class State(rx.State):
    contador: int =0

    def incrementa(self):
        self.contador +=1

    def decrementa(self):
        self.contador -=1

def index():
    return rx.hstack(
    
        rx.button(
            "Decrementa",
            color_scheme="purple",
            border_radius="1rem",
            on_click=State.decrementa,
        ),
        rx.heading(State.contador, font_size="2rem"),
        rx.button(
            "Aumenta",
            color_scheme="blue",
            border_radius="1rem",
        on_click=State.incrementa,
        ),
    )

app= rx.App()
app.add_page(index)
app.compile()