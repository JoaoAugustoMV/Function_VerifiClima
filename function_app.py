import asyncio
import logging
import azure.functions as func
from app.main import main
app = func.FunctionApp()

@app.schedule(schedule="0 0 6 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def verificlima_etl_function(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')


    logging.info('Começando...')
    asyncio.run(main())
    logging.info('Finalizando a função')

# @app.timer_trigger(schedule="0 0 6 * * *", arg_name="myTimer", run_on_startup=True,
#               use_monitor=False) 
# def verificlima_trigger(myTimer: func.TimerRequest) -> None:
    
#     if myTimer.past_due:
#         logging.info('The timer is past due!')

#     logging.info('Python timer trigger function executed.')