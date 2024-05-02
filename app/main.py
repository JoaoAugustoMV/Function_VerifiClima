
import asyncio
from app.service.ClimaAdvisor import ClimaAdvisorService
from app.service.ClimaHGBrasil import ClimaHGBrasil
serviceAdvisor = ClimaAdvisorService()
serviceHG =  ClimaHGBrasil()
async def main():
    await asyncio.gather(
        serviceAdvisor.save_temperatures_predictions(),
        serviceHG.save_temperatures_predictions()
    )
