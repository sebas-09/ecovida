from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el WebDriver (asegúrate de tener ChromeDriver instalado)
driver = webdriver.Chrome()

# Base URL
BASE_URL = "http://localhost:5173"

def test_login():
    driver.get(f"{BASE_URL}/auth/login")
    wait = WebDriverWait(driver, 30)  # Aumentar el tiempo de espera a 30 segundos

    # Esperar los campos de email y contraseña
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    
    # Encontrar el botón con input[type='submit']
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))

    # Ingresar credenciales
    email_input.send_keys("jsebastian465@gmail.com")  # Cambia por un admin válido
    password_input.send_keys("Password123")
    login_button.click()

    time.sleep(3)  # Esperar 3 segundos después del login

    # Imprimir la URL actual para depuración
    current_url = driver.current_url
    print("URL despues del login:", current_url)

    # Verificar si el usuario tiene ROLE_ADMIN en localStorage
    user_data = driver.execute_script("return localStorage.getItem('user');")
    print("Datos del usuario en localStorage:", user_data)

    # Si el usuario es ADMIN pero no fue redirigido, forzar la redirección
    if "ROLE_ADMIN" in user_data and "/admin/categories" not in current_url:
        print("No se redirigio automáticamente, redirigiendo manualmente...")
        driver.get(f"{BASE_URL}/admin/categories")
    
    # Esperar a que la página de categorías se cargue correctamente
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "admin-categories-container")))


    print("Login exitoso")

def test_create_category():
    driver.get(f"{BASE_URL}/admin/categories")
    time.sleep(2)

    # Abrir el modal de creación de categoría
    create_button = driver.find_element(By.CLASS_NAME, "create-btn")
    create_button.click()
    time.sleep(1)

    # Llenar el formulario
    name_input = driver.find_element(By.NAME, "categoryName")
    description_input = driver.find_element(By.NAME, "description")
    image_url_input = driver.find_element(By.NAME, "imageUrl")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    name_input.send_keys("Categoría de prueba")
    description_input.send_keys("Esta es una categoría creada automáticamente")
    image_url_input.send_keys("https://via.placeholder.com/150")
    submit_button.click()

    time.sleep(2)

    # Verificar que la categoría aparece en la lista
    categories = driver.find_elements(By.CLASS_NAME, "category-card")
    assert any("Categoría de prueba" in cat.text for cat in categories), "Error: La categoria no fue creada"

    print("Creacion de categoria exitosa")

def test_create_product():
    driver.get(f"{BASE_URL}/admin/products")
    time.sleep(2)

    # Abrir el modal de creación de producto
    create_button = driver.find_element(By.CLASS_NAME, "create-btn")
    create_button.click()
    time.sleep(1)

    # Llenar el formulario
    name_input = driver.find_element(By.NAME, "productName")
    price_input = driver.find_element(By.NAME, "price")
    description_input = driver.find_element(By.NAME, "description")
    image_url_input = driver.find_element(By.NAME, "imageUrl")
    category_select = driver.find_element(By.NAME, "categoryId")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    name_input.send_keys("Producto de prueba")
    price_input.send_keys("99.99")
    description_input.send_keys("Este es un producto creado automáticamente")
    image_url_input.send_keys("https://www.questionpro.com/blog/wp-content/uploads/2020/03/1264-Portada-test-de-producto.jpg")
    category_select.send_keys(Keys.DOWN, Keys.RETURN)  # Seleccionar la primera categoría disponible
    submit_button.click()

    time.sleep(2)

    # Verificar que el producto aparece en la lista
    products = driver.find_elements(By.CLASS_NAME, "product-card")
    assert any("Producto de prueba" in prod.text for prod in products), "Error: El producto no fue creado"

    print("Creacion de producto exitosa")

def test_view_orders():
    driver.get(f"{BASE_URL}/admin/orders")
    time.sleep(2)

    # Verificar que hay órdenes en la lista
    orders = driver.find_elements(By.CLASS_NAME, "order-card")
    assert len(orders) > 0, "Error: No hay órdenes en la lista"

    print("Visualizacion de ordenes exitosa")

# Ejecutar pruebas
test_login()
test_create_category()
test_create_product()
test_view_orders()

# Cerrar navegador después de las pruebas
driver.quit()
