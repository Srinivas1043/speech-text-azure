import azure.cognitiveservices.speech as speechsdk
speech_key, service_region  = "416417cc97d3400ca07c1ec1532a1286", "australiaeast"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region= service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
print("Begin Speaking...")

result = speech_recognizer.recognize_once()
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))