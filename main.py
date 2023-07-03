from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import html2text
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "localhost:5173",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

ods_list = {
    1: "Fin de la pobreza",
    2: "Hambre cero",
    3: "Salud y bienestar",
    4: "Educación de calidad",
    5: "Igualdad de género",
    6: "Agua limpia y saneamiento",
    7: "Energía asequible y no contaminante",
    8: "Trabajo decente y crecimiento económico",
    9: "Industria, innovación e infraestructura",
    10: "Reducción de las desigualdades",
    11: "Ciudades y comunidades sostenibles",
    12: "Producción y consumo responsables",
    13: "Acción por el clima",
    14: "Vida submarina",
    15: "Vida de ecosistemas terrestres",
    16: "Paz, justicia e instituciones sólidas",
    17: "Alianzas para lograr los objetivos",
}

def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.headless = True

    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    return myDriver

def convert_html_to_markdown(html_content):
    markdown_content = html2text.html2text(html_content)
    return markdown_content


class ODS(BaseModel):
    id: int
    age: int


@app.get("/")
async def root():
    return {"ODS4 FastAPI"}


@app.post("/create-ods-class/")
async def create_ods_class(ods: ODS):
    # Valid id or ods-number
    if ods.id < 1 or ods.id > 17:
        return {f"Error, not recognized ODS {ods.id}"}

    # Init Selenium
    browser = create_driver()
    browser.get("https://www.perplexity.ai/") # Go to PerplexityAI
    
    print("Creating class...")

    # Get textarea for request
    print(len(browser.find_elements(By.XPATH, "//textarea")))
    textarea = browser.find_elements(By.XPATH, "//textarea")[0]
    # Fill textarea with prompt
    textarea.send_keys(
        f"Por favor, desarrolla una clase teórica completa sobre el Objetivo de Desarrollo Sostenible (ODS) número {ods.id}, que trata sobre '{ods_list[ods.id]}'. La clase teorica debe estar dirigida a niños de {ods.age} años.",
        Keys.ENTER,
    )
    time.sleep(25) # Wait 25 seconds until the response is complete

    print("Creating questions...")

    textarea = browser.find_elements(By.XPATH, "//textarea")[0]
    textarea.send_keys(
        "Además, crea un conjunto de 5 preguntas de opción múltiple (la cantidad de opciones debe ser de 4) relacionadas con el tema, y proporciona las respuestas correctas para cada una de ellas.",
        Keys.ENTER,
    )
    time.sleep(25) # Wait 25 seconds until the response is complete

    # Get all responses and convert to markdown
    responses = browser.find_elements(By.CLASS_NAME, "prose")
    ods_class_html_code = responses[0].get_attribute("innerHTML")
    ods_questions_html_code = responses[1].get_attribute("innerHTML")
    ods_class_md = convert_html_to_markdown(ods_class_html_code)
    ods_questions_md = convert_html_to_markdown(ods_questions_html_code)
    browser.quit()
    print("Finish!!")

    return {
        "class": ods_class_md, 
        "questions": ods_questions_md
    }
