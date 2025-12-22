# 💻 KoraLogging
  
![Static Badge](https://img.shields.io/badge/Python_Version-v3-blue)


⭐️ Uma Simples SDK Python para fazer o logging(por exemplo: "Usuário 12 se registrou!") de **serviços, microserviços e Clients!**

## 📲 Instalação
```bash
pip install koralogging
```

***
## 🌟 Iniciando
### Iniciando a SDK
```python
from koralogging import Kora, logging, clientLogging, clientStatus

client = logging.Kora(clientLogging)

client.logging.initialize(
    # Inicia a SDK
    clientLogging = logging
)
```
Na Kora, existe o **Client Backend e o Client Frontend**, então temos as documentações sobre como iniciar :D

---
 - [Client Backend](/client-backend/README.md)
 - [Client Frontend](/client-frontend/README.md)
