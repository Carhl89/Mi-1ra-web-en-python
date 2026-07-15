###Welcome to Reflex! This file outlines the steps to create a basic app.

import reflex as rx

########## BORRAR SOLO LOS NUMERALES

####from rxconfig import config


##class State(rx.State):
##   ##"""The app state."""


##def index() -> rx.Component:
    # Welcome Page (Index)
    #return rx.container(
        #rx.color_mode.button(position="top-right"),
        #rx.vstack(
            #rx.heading("¡Bienvenidos a primera Web con  Reflex!", size="9"),
            #rx.text(
                #"Get started by editing ",
                #rx.code(f"{config.app_name}/{config.app_name}.py"),
                #size="5",
            #),
            #rx.link(
                #rx.button("Check out our docs!"),
                #href="https://reflex.dev/docs/getting-started/introduction/",
                #is_external=True,
            #),
            #spacing="5",
            #justify="center",
            #min_height="85vh",
        #),
    #)

def index():
    return rx.container(
        rx.heading("Sistema de Ventas", size="8"),
        rx.text("Articulos de Limpieza LCV"),
        rx.divider(),
        rx.hstack(
            rx.card(
                rx.heading("Productos"),
                rx.text("Administrar Productos"),
                width="250px",
            ),
            rx.card(
                rx.heading("Clientes"),
                rx.text("Administrar Clientes"),
                width="250px",
            ),
            rx.card(
                rx.heading("Ventas"),
                rx.text("Registrar ventas"),
                width="250px",
            ),
            spacing="4",
        ),
        padding="2em",
    )


app = rx.App()
app.add_page(index)
