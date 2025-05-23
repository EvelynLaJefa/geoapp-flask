from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import gps
import requests

class GeoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.btn = Button(text="Obtener Ubicación", size_hint=(0.8, 0.5))
        self.btn.bind(on_press=self.obtener_ubicacion)
        layout.add_widget(self.btn)
        return layout

    def obtener_ubicacion(self, instance):
        try:
            gps.configure(on_location=self.on_location)
            gps.start()
        except Exception as e:
            print("Error GPS:", e)

    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        print(f"Coordenadas reales: {lat}, {lon}")
        self.enviar_a_servidor(lat, lon)

    def enviar_a_servidor(self, lat, lon):
        try:
            respuesta = requests.post(
                "https://a503-80-224-221-206.ngrok-free.app ->http://localhost:5000",  # ← luego lo cambiamos por una URL real
                json={"latitud": lat, "longitud": lon},
                timeout=10
            )
            print("Respuesta del servidor:", respuesta.text)
        except Exception as e:
            print("Error de conexión:", e)
if __name__ == '__main__':
    GeoApp().run()

