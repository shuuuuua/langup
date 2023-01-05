class Text2Voice:
    @classmethod
    def text2voice(self, source_sentence, wpm=140, source_lang='us', speaker_gender='NEUTRAL'):
        #@param ['FEMALE', 'MALE', 'NEUTRAL', 'SSML_VOICE_GENDER_UNSPECIFIED']

        #import os
        #api_key = os.environ['API_KEY']
        #from googleapiclient.discovery import build
        #service = build('texttospeech', 'v1beta1', developerKey=api_key)

        from google.cloud import texttospeech
        client = texttospeech.TextToSpeechClient()

        input_text = texttospeech.SynthesisInput(text=source_sentence)

        if source_lang == 'us':
            lang = "en-US"

        voice_name = 'en-US-Wavenet-A' #@param {type: "string"}
        if speaker_gender in ('FEMALE', 'female'):
            gender = texttospeech.SsmlVoiceGender.FEMALE
        elif speaker_gender in ('MALE', 'male'):
            gender = texttospeech.SsmlVoiceGender.MALE
        elif speaker_gender in ('NEUTRAL', 'neutEral'):
            gender = texttospeech.SsmlVoiceGender.NEUTRAL
        else:
            gender = texttospeech.SsmlVoiceGender.NEUTRAL

        voice = texttospeech.VoiceSelectionParams(
            language_code=lang,
            name=voice_name,
            ssml_gender=gender,
	)

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

        return response.audio_content
