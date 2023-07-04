from processing import *
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


FPS = 10
pause = True
file_path = './pencil.mp4'
Window.maximize()           


class Main_Screen(Screen):
    def start(self):
        global pause
        pause = False
        self.ids.start_btn.disabled = True
        self.ids.start_btn.text = "Resume"
        self.ids.file_path_label.text = file_path
        self.ids.pause_btn.disabled = False

    def pause_and_resum_video(self):
        global pause
        if pause:
            pause = False
            self.ids.start_btn.disabled = True
            self.ids.pause_btn.disabled = False
        else:
            pause = True
            self.ids.start_btn.disabled = False
            self.ids.pause_btn.disabled = True

    def quit(self):
        Pencil_segment_detector.get_running_app().stop()
        Window.close()


class Default_image(Image):
    def __init__(self, capture=None, fps=FPS, **kwargs):
        super(Default_image, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        if not pause:
            ret, frame = open_file(file_path).read()
            if ret:
                processed_frame , treshold_frame = video_processing(frame)
                buf1 = cv2.flip(processed_frame, 0)
                buf = buf1.tobytes()
                image_texture = Texture.create(size=(processed_frame.shape[1], processed_frame.shape[0]), colorfmt='bgr')
                image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                self.texture = image_texture


class Processed_image(Image):
    def __init__(self, capture=None, fps=FPS, **kwargs):
        super(Processed_image, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0 / fps)
    
    def update(self, dt):
        if not pause:
            ret, frame = open_file(file_path).read()
            print('ok')
            if ret:
                processed_frame , treshold_frame = video_processing(frame)
                buf1 = cv2.flip(treshold_frame, 0)
                buf = buf1.tobytes()
                image_texture = Texture.create(size=(treshold_frame.shape[1], treshold_frame.shape[0]), colorfmt='bgr')
                image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                self.texture = image_texture
            else:
                ret, frame = open_file(file_path).read()


class Pencil_segment_detector(MDApp):
    def build(self):
        global SM
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.load_kv('Pencil_segment_detector.kv')
        SM = ScreenManager()
        SM.add_widget(Main_Screen(name='Main_Screen'))
        return SM


if __name__ == '__main__':
    Pencil_segment_detector().run()
