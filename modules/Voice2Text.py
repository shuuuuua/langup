class Voice2Text:
    @classmethod
    def voice2text(self, voice_audio_uri, lang='us'):
        voice_audio = speech.RecognitionAudio(uri=gcs_uri)

        if lang == 'us':
            lang_code = 'en-US' #@param ["en-US", "ja-JP", "en-IN"]
        model = 'default' #@param ["command_and_search", "phone_call", "video", "default"]

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code=lang_code,
            model=model,
        )

        response = client.recognize(config=config, audio=audio)
        #response = speech_service.speech().recognize(
        #    body={config=config,
        #        audio=voice_audio}
        #).execute()

        #for r in response["results"]:
        #    print('transcript: ', r['alternatives'][0]['transcript'])
        #    print('confidence: ', r['alternatives'][0]['confidence'])

        return text
