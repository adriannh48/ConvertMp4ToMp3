from flask import Flask , request , send_file
from helpers import Helpers

app = Flask('teste')

@app.route('/convertMp4ToMp3' , methods=['POST'])
def Convert():
 

    if request.form['url_youtube'] != '':

        FileVideo = Helpers.GetVideoByUrl('https://www.youtube.com/watch?v=vAYwgBY6y-E')

        if FileVideo != False:
            
            nameVideo = Helpers.GetNameFileByVideo(FileVideo)
            convert   = Helpers.ConvertMp4ToMp3(FileVideo , nameVideo[1])

            if convert != False:
                Helpers.RemoveArquive(FileVideo)

                print(convert)

                return { 'status': 200 , 'msg': 'arquivo pronto para ser baixado !!' , 'fileName': convert }

            else:
                return {'status': 400 , 'msg': 'Não foi possível converter o video !'}


@app.route('/dowload' , methods=['GET'])
def downloadMusic():
    
    path = request.args.get('path')

    if path != '' :
        
        return send_file(path, as_attachment=True)
    
    else:

        return {'status': 400 , 'msg': 'Não foi possível fazer dowload da musica !'}

        
app.run()