from koralogging import StartLogging, logging

logging.starter (
    start = StartLogging,
    loggingClient = logging,
    on_ready = lambda: logging.info("Kora iniciado!")
)
