from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

Builder.load_file('Front-end/class.kv')
Builder.load_file('Front-end/task.kv')
Builder.load_file('Front-end/reminder.kv')
Builder.load_file('Front-end/project.kv')

sm = ScreenManager(transition = NoTransition())

class MyApp(App):
    def build(self):
        Window.maximize()

        sm.add_widget(Task(name='task'))
        sm.add_widget(Reminder(name='reminder'))
        sm.add_widget(Project(name='project'))
        sm.add_widget(New_Task(name='new_task'))

        nav_bar = NavigationBar(orientation='horizontal')

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(nav_bar)
        layout.add_widget(sm)
        return layout


class NavigationBar(Screen, BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.Press_Task()
    
    def Press_Task(self):
        if self.ids.task_line.opacity == 0:
            self.ids.task_line.opacity = 1

        if self.ids.reminder_line.opacity == 1:
            self.ids.reminder_line.opacity = 0

        if self.ids.project_line.opacity == 1:
            self.ids.project_line.opacity = 0

        sm.current = 'task'

    def Press_Reminder(self):
        if self.ids.reminder_line.opacity == 0:
            self.ids.reminder_line.opacity = 1

        if self.ids.task_line.opacity == 1:
            self.ids.task_line.opacity = 0

        if self.ids.project_line.opacity == 1:
            self.ids.project_line.opacity = 0

        sm.current = 'reminder'

    def Press_Project(self):
        
        if self.ids.task_line.opacity == 1:
            self.ids.task_line.opacity = 0

        if self.ids.reminder_line.opacity == 1:
            self.ids.reminder_line.opacity = 0

        if self.ids.project_line.opacity == 0:
            self.ids.project_line.opacity = 1
            
        sm.current = 'project'

class Task(Screen):
    def Create_New_Task(self):
        sm.current = 'new_task'

class New_Task(Screen):
    pass

class Reminder(Screen):
    pass

class Project(Screen):
    pass

if __name__ == '__main__':
    MyApp().run()