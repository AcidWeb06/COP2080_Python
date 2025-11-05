from nicegui import ui

#Create a greeting
#------------GREETING-----------
def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "stranger"}!"
    ui.notify(msg) #Creates a popup


#Create a counter
#------------COUNTER-----------
class State: 
    count = 0

def add_one():
    State.count += 1
    count_label.text = f"Count: {State.count}"


#TODO
#Create Reset button which sets the counter back to 0
def reset():
    State.count = 0
    count_label.text = f"Count: {State.count}"

#------------LAYOUT-------------
ui.label("Welcome to nicegui!").style("color: green; font-size: 40px")

with ui.row().classes("w-full"):
    with ui.column().classes("flex-1"):
        with ui.card().classes("h-65 w-full self-auto"):
            ui.label("Greeter").style("font-size: 30px")
            input_field = ui.input("Enter your name: ")
            ui.button("Greet ME!", on_click=greet, color="green")

    with ui.column().classes("flex-1"):
        with ui.card().classes("h-65 w-full self-auto"):
            ui.label("Counter").style("font-size: 30px")
            with ui.column():
                count_label = ui.label("Count: 0").classes("font-mono text-lg")
                with ui.row():
                    ui.button("Add 1", on_click=add_one)
                    ui.button("Reset", on_click=reset, color="red")
            
            #Add slider
            label_slider = ui.label("Step: 5").classes("font-mono text-lg")
            slider = ui.slider(min=1, max=10, value=5).classes("w-30")
            slider.on("update:model-value", lambda: label_slider.set_text(f"Step: {slider.value}"))

with ui.row():
    n1 = ui.number("Number 1", value=0).classes('w-24')
    ui.label("+").classes("text-lg")
    n2 = ui.number("Number 2", value=0).classes("w-24")
    ui.label("=").classes("text-lg")
    result = ui.label("0").classes("text-lg")

ui.switch("Dark Mode", on_change= lambda e: ui.dark_mode().enable() if e.value else ui.dark_mode().disable())
ui.run(title="Simple Greeting App")