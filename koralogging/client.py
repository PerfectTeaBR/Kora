from koralogging import Kora, logging, clientLogging, clientStatus

client = logging.Kora(clientLogging)

client.logging.initialize(
    # Inicia a SDK
    clientLogging = clientStatus
)
