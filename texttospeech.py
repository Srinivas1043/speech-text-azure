import azure.cognitiveservices.speech as speechsdk
speech_key, service_region  = "b3a658c8aa694391a20561881d16e101", "australiaeast"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region= service_region)
speech_config.speech_synthesis_voice_name = "en-CA-Linda"
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
print("Type some text that you want to speak...")
text = input()
result = speech_synthesizer.speak_text_async(text).get()
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")