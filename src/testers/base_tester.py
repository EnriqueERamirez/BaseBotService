import asyncio
import logging
from abc import ABC, abstractmethod

# Configura el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BaseTester(ABC):
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    @abstractmethod
    async def run_test(self):
        for action in self.actions:
            await action.execute()
