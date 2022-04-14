# import os
# from flask import Flask, flash, request, redirect, url_for, session, jsonify
# from werkzeug.utils import secure_filename
# from flask_cors import CORS, cross_origin
# import logging
# from flask import jsonify
# from flask_session import Session

# SESSION_TYPE = 'memcache'
# from func import *

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger('HELLO WORLD')

# #UPLOAD_FOLDER = 'F:/Web Projects/Hack-O-Holics-Bajaj-Hackathon-main/src/static'
# UPLOAD_FOLDER = '../static'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# app = Flask(
#     __name__, static_folder='../src/static')

# sess = Session()

# app.secret_key = "super secret key"

# CORS(app)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# fPathDest = ''
# filename = ''


# @app.route('/api/upload', methods=['POST'])
# def handle_form():
#     global fPathDest, filename
#     target = os.path.join(UPLOAD_FOLDER)
#     if not os.path.isdir(target):
#         os.mkdir(target)
#         logger.info("welcome to upload`")

#     print("Fine till here")

#     files = request.files
#     #file = request.files['file']
#     file = files.get('file')

#     print(file) 

#     filename = secure_filename(file.filename)
#     destination = "/".join([target, filename])
#     #print(destination)
#     file.save(destination)

#     fpath = destination

#     print(f"\n\nfpath = {fpath}\n\n")



# if(__name__) == '__main__':
#     app.config['SESSION_TYPE'] = 'filesystem'

#     sess.init_app(app)

#     app.debug = True

#     app.run(5000)