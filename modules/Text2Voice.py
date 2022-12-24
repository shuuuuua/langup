class Text2Voice:
    @classmethod
    def text2voice(self, source_sentence, wpm=140, source_lang='us', speaker_gender='NEUTRAL'):
        #@param ['FEMALE', 'MALE', 'NEUTRAL', 'SSML_VOICE_GENDER_UNSPECIFIED']

        import os
        api_key = os.environ['API_KEY']
\
        from googleapiclient.discovery import build
        service = build('texttospeech', 'v1beta1', developerKey=api_key)

        import textwrap
        if source_lang == 'us':
            lang = "en-US"

        if speaker_gender in ('FEMALE', 'female'):
            gender = 'FEMALE'
        elif speaker_gender in ('MALE', 'male'):
            gender = 'MALE'
        elif speaker_gender in ('NEUTRAL', 'neutral'):
            gender = 'NEUTRAL'
        else:
            gender = 'NEUTRAL'
        audio_encoding = 'MP3' #@param ['OGG_OPUS', 'LINEAR16', 'MP3']
        textwrap.wrap(source_sentence)
        voice_name = 'en-US-Wavenet-A' #@param {type: "string"}

        response = service.text().synthesize(
            body={
                'input': {
                    'text': source_sentence,
                },
                'voice': {
                    'languageCode': source_lang,
                    'ssmlGender': gender,
                    'name': voice_name,
                },
                'audioConfig': {
                    'audioEncoding': audio_encoding,
                    'speakingRate': 1.2,
                },
            }
        ).execute()

        voice = response['audioContent']
        #import base64
        #from IPython.display import Audio
        #Audio(base64.b64decode(voice))

        return voice
