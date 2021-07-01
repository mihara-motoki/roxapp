import os
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, ORJSONResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
import ast
from os import scandir
import sys
from pathlib import Path
from subprocess import call
import shutil

app = FastAPI()


templates = Jinja2Templates(directory="templates")

@app.get("/up", response_class=HTMLResponse)
async def fileupload(request: Request):
    '''docstring
    ファイルアップロード（初期表示）
    '''    
    #return templates.TemplateResponse("fileupload.html", {"request": request})
    return templates.TemplateResponse("item.html", {"request": request})



@app.post("/input", response_class=HTMLResponse)
async def post_input(request: Request,file: UploadFile = File(...)):
    print(file.filename)
    try:
        with open("test.pdf", "wb") as buffer:
         shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()
    
    # pdf2txt.py のパス
    py_path = "C:\\Users\\81803\\Documents\\ROX\\appenv\\Scripts\\pdf2txt.py"

    # pdf2txt.py の呼び出し
    #call(["py", str(py_path), "-o extract-sample.txt", "-p 1", file])
    call(["py", str(py_path), "-o test.txt", "-p 1", "test.pdf"])

    f = open(' test.txt', 'r', encoding='UTF-8')
    s= f.read()

    target1 = '⽀払い情報'  # 後にある文字を抽出したい
    idx1 = s.find(target1)
    target2 = '⽀払い⽅法'
    idx2 = s.find(target2)
    r1 = s[idx1+len(target1):idx2]

    target3 = '請求先住所'
    idx3 = s.find(target3)
    r2 = s[idx3+len(target3):idx3+len(target3)+5]
    return templates.TemplateResponse("item.html", {"request": request, "text":s, "text2":r1, "text3":r2})

