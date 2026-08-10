def crear_peticion_http(prompt_usuario):
    return f"POST /api/v1/generate HTTP/1.1\nHeader: Authorization Bearer TOKEN\nBody: {prompt_usuario}"

def procesar_prompt_llm(prompt):
    print("[Servidor LLM] Procesando tokens y contexto...")
    return f"HTTP/1.1 200 OK\nBody: Respuesta generada por la IA para el prompt: '{prompt}'"

# Programa Principal
print("=== SIMULADOR DE PETICIÓN HTTP A LLM (TALLER 10 - DEBER 7) ===")
prompt = input("Ingrese la consulta/prompt para el modelo de IA: ")

print("\n[Cliente Web] Usuario hizo clic en 'Enviar'.")
peticion_http = crear_peticion_http(prompt)
print("[Cliente Web] Petición HTTP construida con éxito.")

print("[Red] Enviando petición HTTP al servidor backend...")
conexion_exitosa = True

if conexion_exitosa:
    print("[Servidor] Petición recibida correctamente.")
    respuesta_http = procesar_prompt_llm(prompt)
    
    print("\n[Cliente Web] Respuesta HTTP recibida:")
    print(respuesta_http)
    print("[Cliente Web] Mostrando respuesta en la interfaz del usuario.")
else:
    print("[Error] No se pudo establecer conexión con el servidor LLM.")
