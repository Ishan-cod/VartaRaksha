import asyncio
import datetime
from aimodels.tts_detector.detector import detect_deepfake
from aimodels.context_finder.detector import getcontext_from_audio
from aimodels.recognition_model.detector import audio_similiarity
from aimodels.recognition_model.store_voice import store_voice

# store_voice("audio_path", "name") 
# use this to store a new voice ... into the directory

async def run_sync(audio_path : str):
    deepfake_task = asyncio.to_thread(detect_deepfake, audio_path)
    context_task = asyncio.to_thread(getcontext_from_audio, audio_path)
    recognition_task = asyncio.to_thread(audio_similiarity, audio_path)

    deepfake_result, context_result, recognition_result = await asyncio.gather(deepfake_task, context_task, recognition_task)

    return {
        "deepfake_result": deepfake_result, 
        "context_result": context_result,
        "recognition_result": recognition_result
    }


while True:
    path = input("Input complete Audio path: ")

    timenow = datetime.datetime.now()
    result = asyncio.run(run_sync(path))

    print(result)
    timeend = datetime.datetime.now()
    print("Time taken:", timeend - timenow)