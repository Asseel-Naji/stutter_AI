"""
Guys, I really wanted to use amazon's transcribe, I REALLY did. But the API requires that every single audio
file be uploaded to s3 before transcribtion, this makes no sense. C'mon!
"""
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    import io
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        # sample_rate_hertz=16000,
        language_code='en-US')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        final_result = final_result + result.alternatives[0].transcript
    return final_result
# transcribe_file("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset_stereo/mixtures/01_amzn_mix.wav")