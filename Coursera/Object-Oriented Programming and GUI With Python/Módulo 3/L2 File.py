import ipywidgets as widgets
from IPython.display import display

# Initialize variables
name_input = None
age_input = None

def set_name(name):
    return name

def set_age(age):
    return age

def print_person(_):
    print(f"Name: {name_input.value}, Age: {age_input.value}")

name_input = widgets.Text(description="Name:")
age_input = widgets.IntSlider(description="Age:", min=0, max=120, step=1)

name_input.observe(lambda change: set_name(change['new']), names='value')
age_input.observe(lambda change: set_age(change['new']), names='value')

display(name_input)
display(age_input)

continue_button = widgets.Button(description="Continue")
continue_button.on_click(print_person)
display(continue_button)