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
            print("Error al activar el GPS:", e)

    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        print(f"📍 Coordenadas reales: {lat}, {lon}")
        self.enviar_a_servidor(lat, lon)

    def enviar_a_servidor(self, lat, lon):
        try:
            # ⚠️ Asegúrate de actualizar este enlace cada vez que cambie en Ngrok
            url = "https://16e5-80-224-221-206.ngrok-free.app/recibir_ubicacion"
            datos = {"latitud": lat, "longitud": lon}
            respuesta = requests.post(url, json=datos, timeout=10)
            print("✅ Respuesta del servidor:", respuesta.text)
        except Exception as e:
            print("❌ Error al enviar al servidor:", e)

if __name__ == '__main__':
    GeoApp().run()
