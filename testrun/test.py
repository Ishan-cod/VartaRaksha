#### THIS IS FOR TESTING PURPOSES ONLY. DO NOT USE THIS ####


import asyncio
import datetime
from aimodels.tts_detector.detector import detect_deepfake
from aimodels.context_finder.detector import getcontext_from_audio

async def run_sync(audio_path : str):
    deepfake_task = asyncio.to_thread(detect_deepfake, audio_path)
    context_task = asyncio.to_thread(getcontext_from_audio, audio_path)

    deepfake_result, context_result = await asyncio.gather(deepfake_task, context_task)

    return {
        "deepfake_result": deepfake_result, 
        "context_result": context_result
    }


while True:
    path = input("Audio path: ")

    timenow = datetime.datetime.now()
    result = asyncio.run(run_sync(path))

    print(result)
    timeend = datetime.datetime.now()
    print("Time taken:", timeend - timenow)