from nicegui import ui

ui.label("Welcome to nicegui!").style("color: green; font-size: 40px")

#Create a greeting

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "stranger"}!"
    ui.notify(msg) #Creates a popup

input_field = ui.input("Enter your name: ")
ui.button("Greet ME!", on_click=greet, color="red")

#Create a counter
class State: 
    count = 0

count_label = ui.label("Count: 0")

def add_one():
    State.count += 1
    count_label.text = f"Count: {State.count}"

#TODO
#Create Reset button which sets the counter back to 0
ui.button("Add 1", on_click=add_one)
ui.run(title="Simple Greeting App")