import Text2Voice
import Voice2Text


#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/shuichiro_aiba/langup/.key.json'

source_sentence = """The virus is no more deadly than a cold, but vaccines are essential. Case numbers have plummeted, but most people you know are sick. The death toll is tiny, but there are long lines outside crematoriums. These are just some of the contradictions that Chinese citizens are having to live with, as claims from the government fail to stack up with events on the ground. China began unwinding its stringent zero-Covid policy after nationwide protests saw thousands take to the streets to demand the end of restrictions – and, in some cases, the end of the regime that imposed them."""

voice = Text2Voice.Text2Voice.text2voice(source_sentence, wpm=140, source_lang='us', speaker_gender='NEUTRAL')

with open('test.mp3', 'wb') as f:
    f.write(voice)
