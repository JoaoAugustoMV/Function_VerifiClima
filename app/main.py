
import asyncio
from service.ClimaAdvisor import ClimaAdvisorService
from service.ClimaHGBrasil import ClimaHGBrasil
serviceAdvisor = ClimaAdvisorService()
serviceHG =  ClimaHGBrasil()
async def main():
    await asyncio.gather(
        serviceAdvisor.save_temperatures_predictions(),
        serviceHG.save_temperatures_predictions()
    )
