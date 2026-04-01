# ♻️ Detector Inteligente de Recicláveis com IA

Sistema completo de visão computacional capaz de detectar, classificar e analisar materiais recicláveis em tempo real utilizando Inteligência Artificial com YOLOv8.

---

## 📌 Sobre o Projeto

Este projeto utiliza técnicas modernas de **visão computacional** para identificar objetos recicláveis através de uma webcam, classificando automaticamente os materiais e gerando estatísticas em tempo real.

Além disso, o sistema possui um mecanismo de **rastreamento inteligente**, evitando contagens duplicadas e permitindo a coleta de dados para evolução contínua do modelo.

---

## 🚀 Funcionalidades

✔️ Detecção de objetos em tempo real
✔️ Classificação automática de materiais
✔️ Rastreamento de objetos (ID único por objeto)
✔️ Evita contagem duplicada
✔️ Interface visual com bounding boxes
✔️ Salvamento automático de imagens detectadas
✔️ Separação entre reciclável e não reciclável
✔️ Geração de estatísticas em JSON
✔️ Dashboard em tempo real na tela
✔️ Base pronta para aprendizado contínuo

---

## 🧠 Classes Detectadas

* Plástico
* Metal
* Vidro
* Papel
* Lixo Comum

---

## 🧪 Resultados do Modelo

| Métrica      | Valor |
| ------------ | ----- |
| Precisão (P) | 80.5% |
| Recall (R)   | 62.4% |
| mAP@50       | 73.1% |
| mAP@50-95    | 52.2% |

---

## 🛠️ Tecnologias Utilizadas

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* NumPy
* Pillow (PIL)
* JSON

---

## 📂 Estrutura do Projeto

```
📦 projeto
 ┣ 📜 detector_yolo.py
 ┣ 📜 dataset.yaml
 ┣ 📜 classes.json
 ┣ 📜 estatisticas.json
 ┣ 📂 capturas
 ┃ ┣ 📂 reciclavel
 ┃ ┗ 📂 nao_reciclavel
 ┣ 📂 dataset_yolo
 ┣ 📂 runs
 ┗ 📜 README.md
```

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/detector-reciclaveis-ia.git
cd detector-reciclaveis-ia
```

---

### 2. Instale as dependências

```bash
pip install ultralytics opencv-python numpy pillow
```

---

## ▶️ Como Executar

```bash
python detector_yolo.py
```

📷 O sistema abrirá a webcam e iniciará a detecção automaticamente.

---

## 🧪 Treinamento do Modelo

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="dataset.yaml",
    epochs=30,
    imgsz=640,
    batch=8
)
```

---

## 🔄 Aprendizado Contínuo (IA Auto Evolutiva)

O sistema permite:

* Capturar novos dados automaticamente
* Armazenar imagens detectadas
* Utilizar esses dados para novos treinamentos

📌 Isso possibilita evolução constante da IA.

---

## 💾 Salvamento de Dados

### 📸 Imagens

As imagens detectadas são armazenadas automaticamente:

```
capturas/
 ┣ reciclavel/
 ┗ nao_reciclavel/
```

---

### 📊 Estatísticas

Arquivo gerado automaticamente:

```json
estatisticas.json
```

Exemplo:

```json
{
    "Plástico": 10,
    "Metal": 5,
    "Vidro": 3,
    "Papel": 7,
    "Lixo Comum": 2
}
```

---

## ⚠️ Observações Importantes

🚫 Arquivos pesados não estão incluídos no repositório:

* Modelos `.pt`
* Datasets `.zip`

👉 Utilize links externos para download.

---

## 📥 Dataset e Modelo

📌 Dataset:
(Adicionar link do Roboflow ou Google Drive)

📌 Modelo treinado:
(Adicionar link do modelo .pt)

---

## 🎯 Aplicações

* Coleta seletiva automatizada
* Reciclagem inteligente
* Projetos ambientais
* Smart Cities
* Educação e pesquisa em IA

---

## 🔥 Diferenciais do Projeto

⭐ Rastreamento inteligente (sem duplicação)
⭐ Sistema completo end-to-end
⭐ Interface visual personalizada
⭐ Geração automática de dados
⭐ Base para IA auto evolutiva

---

## 📈 Melhorias Futuras

* Interface gráfica (GUI)
* Deploy em Raspberry Pi
* Integração com IoT
* Aumento da acurácia do modelo
* Aplicativo mobile

---

## 👨‍💻 Autor

William Ruan

---

## 📄 Licença

Este projeto é de uso acadêmico e educacional.

---

# ♻️ Tecnologia aplicada à sustentabilidade
