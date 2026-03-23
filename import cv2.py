import cv2
import numpy as np
import tensorflow as tf

# Modelo pronto
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Função de classificação de material
def classificar_material(objeto):
    objeto = objeto.lower()

    if objeto in ["banana", "apple", "orange"]:
        return "Orgânico", "Não reciclável"

    elif objeto in ["bottle", "plastic bag"]:
        return "Plástico", "Reciclável"

    elif objeto in ["can"]:
        return "Metal", "Reciclável"

    else:
        return "Desconhecido", "Verificar"

# Função que usa IA (OTIMIZADA)
def detectar_objeto(frame):
    frame_small = cv2.resize(frame, (200, 200))  # reduz processamento
    img = cv2.resize(frame_small, (224, 224))

    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)

    preds = model.predict(img, verbose=0)
    resultado = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)

    return resultado[0][0][1]

# Conexão com câmera do celular
cap = cv2.VideoCapture("http://10.122.89.224:8080/video")

# Reduz buffer (menos atraso)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

frame_count = 0
objeto = "..."

while True:
    # Descarta frames antigos (reduz delay)
    for _ in range(5):
        cap.read()

    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Roda IA só a cada 30 frames (muito mais leve)
    if frame_count % 30 == 0:
        objeto = detectar_objeto(frame)

    material, reciclavel = classificar_material(objeto)

    # Reduz resolução para exibir mais rápido
    frame = cv2.resize(frame, (640, 480))

    # Texto na tela
    cv2.putText(frame, f"Objeto: {objeto}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.putText(frame, f"Material: {material}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

    cv2.putText(frame, f"Reciclavel: {reciclavel}", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imshow("Detector de Reciclavel", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()