import pandas as pd
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Create root layout with vertical orientation
        root = GridLayout(cols=1, spacing=10, padding=10)

        # Create search bar components
        search_layout = GridLayout(cols=2, size_hint_y=None, height=50)
        self.search_input = TextInput(multiline=False, hint_text='Enter br_code')
        search_button = Button(text='Search', size_hint=(None, None), size=(100, 50))
        search_button.bind(on_press=self.search_button_pressed)

        search_layout.add_widget(self.search_input)
        search_layout.add_widget(search_button)

        # Add search bar to root layout
        root.add_widget(search_layout)

        # Create main content layout
        self.layout = GridLayout(cols=3, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        # Add header labels
        self.layout.add_widget(Label(text='Branch Code', bold=True, size_hint_y=None, height=40))
        self.layout.add_widget(Label(text='Branch', bold=True, size_hint_y=None, height=40))
        self.layout.add_widget(Label(text='ISP', bold=True, size_hint_y=None, height=40))

        # Read and display initial data
        self.update_display()

        # Create a ScrollView and add the main layout
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 120))
        scroll_view.add_widget(self.layout)

        # Add ScrollView to root layout
        root.add_widget(scroll_view)

        return root

    def update_display(self):
        # Clear existing data
        self.layout.clear_widgets()

        # Read the CSV file
        df = pd.read_csv('branches.csv')

        # Display the data
        for index, row in df.iterrows():
            # Format br_code as 4 digits without decimal point
            formatted_br_code = f"{int(row['br_code']):04d}"
            
            self.layout.add_widget(Label(text=formatted_br_code, size_hint_y=None, height=40))
            self.layout.add_widget(Label(text=str(row['Branch']), size_hint_y=None, height=40))
            self.layout.add_widget(Label(text=str(row['ISP']), size_hint_y=None, height=40))

    def search_button_pressed(self, instance):
        # Get search text from TextInput
        search_text = self.search_input.text.strip()

        # Read the CSV file
        df = pd.read_csv('branches.csv')

        # Clear existing data
        self.layout.clear_widgets()

        # Add header labels again
        self.layout.add_widget(Label(text='Branch Code', bold=True, size_hint_y=None, height=40))
        self.layout.add_widget(Label(text='Branch', bold=True, size_hint_y=None, height=40))
        self.layout.add_widget(Label(text='ISP', bold=True, size_hint_y=None, height=40))

        # Display filtered data based on search_text
        for index, row in df.iterrows():
            # Format br_code as 4 digits without decimal point
            formatted_br_code = f"{int(row['br_code']):04d}"
            
            if formatted_br_code.startswith(search_text):
                self.layout.add_widget(Label(text=formatted_br_code, size_hint_y=None, height=40))
                self.layout.add_widget(Label(text=str(row['Branch']), size_hint_y=None, height=40))
                self.layout.add_widget(Label(text=str(row['ISP']), size_hint_y=None, height=40))

    # Handle app running directly from script
if __name__ == '__main__':
    from kivy.core.window import Window
    Window.size = (600, 800)  # Set initial window size
    MyApp().run()
