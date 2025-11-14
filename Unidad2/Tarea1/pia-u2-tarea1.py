import boto3
import re

# Nos conectamos a los servicios de AWS e iniciamos sesión
session = boto3.Session(profile_name="default")
rekognition = session.client("rekognition")
s3 = session.client("s3")

# Establecemos las variables necesarias
BUCKET_NAME = "pia-bucket"
S3_FOLDER_NAME = "tarea2/"
img_extensions = (".jpg", ".png")
car_labels = {"Car", "Vehicle", "Automobile"}
pattern_car_license_plate = re.compile(r"^(?=.*[A-Z])(?=.*\d)[A-Z0-9\- ]{5,10}$")

# Listamos los objetos en el bucket y carpeta especificados
response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=S3_FOLDER_NAME)
print(response.get("Contents", []))

for obj in response.get("Contents", []):
    key = obj["Key"]

    # filtramos solo imágenes con las extensiones solicitadas en la tarea
    if not key.lower().endswith(img_extensions):
        continue

    print(f"Analizando: {key}")

    # Llamamos a Rekognition detect_labels para saber si hay labels de coches
    rekog_response = rekognition.detect_labels(
        Image={"S3Object": {"Bucket": BUCKET_NAME, "Name": key}},
        MaxLabels=50,
        MinConfidence=70
    )

    # Revisamos si hay alguna etiqueta de coche entre las etiquetas encontradas
    labels_presentes = {label["Name"] 
                        for label in rekog_response["Labels"] 
                        if label["Name"] in car_labels and label["Confidence"] >= 90}

    if car_labels.intersection(labels_presentes):
        print(f"SÍ HAY COCHES >90% en {key}\n")
        # En caso de haber coches, imprimimos su matrícula si la detectamos
        
         # Detectar texto (posible matrícula)
        text_response = rekognition.detect_text(
            Image={"S3Object": {"Bucket": BUCKET_NAME, "Name": key}}
        )
        
        car_license_plates = []

        for text in text_response["TextDetections"]:
            if text["Type"] in ("LINE", "WORD") and text["Confidence"] >= 90:
                textContent = text["DetectedText"].upper()
                if pattern_car_license_plate.fullmatch(textContent):
                    car_license_plates.append(textContent)

        if car_license_plates:
            print("Matrícula detectada:")
            for m in car_license_plates:
                print(f"   - {m}")
            print()
        else:
            print("No se detectó matrícula en esta imagen.\n")
        
    else:
        print(f"NO HAY COCHES en {key}\n")
