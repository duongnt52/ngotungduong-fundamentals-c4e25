from gmail import GMail, Message
import datetime
import random
while True:
    now = datetime.datetime.now()
    if now.hour == 7 :
        sickness_list = ["thương hàn", "kiết lị", "ebola", "sốt xuất huyết", "hiv"]
        gmail = GMail("Co Bau<codaubo@gmail.com>", "ngotungduongbn1997")
        html_template = ''' 
        <p>Ch&agrave;o sếp,</p>
        <p>S&aacute;ng nay ngủ dậy em thấy <strong>{{symptom}}</strong>,
        b&aacute;c sỹ bảo em bị <strong>{{sickness}}</strong>. Sếp cho em nghỉ l&agrave;m h&ocirc;m nay nh&eacute;.&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
        <p>Em cảm ơn sếp,</p>
        <p><strong>Nh&acirc;n vi&ecirc;n</strong></p>
        '''
        html_content = html_template.replace("{{sickness}}", random.choice(sickness_list)).replace("{{symptom}}", random.choice(sickness_list))
        msg = Message('Nghi Viec',to='codaubo97@gmail.com', html=html_template)
        gmail.send(msg)





       