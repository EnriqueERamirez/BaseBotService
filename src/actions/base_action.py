import asyncio
import logging
from abc import ABC, abstractmethod

# Configura el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BaseAction(ABC):
    @abstractmethod
    async def execute(self, *args, **kwargs):
        pass

class BaseAPITester(BaseAction):
    async def execute(self, *args, **kwargs):
        logger.info("BaseAPITester starting execution")
        # Ejemplo de método asincrónico
        await asyncio.sleep(1)  # Espera por 1 segundo
        logger.info("BaseAPITester executed")

class BaseDBTester(BaseAction):
    async def execute(self, *args, **kwargs):
        logger.info("BaseDBTester starting execution")
        # Ejemplo de método asincrónico
        await asyncio.sleep(1)  # Espera por 1 segundo
        logger.info("BaseDBTester executed")

class BaseUITester(BaseAction):
    async def execute(self, *args, **kwargs):
        logger.info("BaseUITester starting execution")
        # Ejemplo de método asincrónico
        await asyncio.sleep(1)  # Espera por 1 segundo
        logger.info("BaseUITester executed")
