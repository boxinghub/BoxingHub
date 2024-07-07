# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python

EXPOSE 5000

# install pip dependencies
ADD requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
ADD . /app

CMD ["python", "app.py"]